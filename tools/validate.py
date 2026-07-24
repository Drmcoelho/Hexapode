#!/usr/bin/env python3
"""Validador de integridade do repositório-mãe Hexápode.

Garante que o manifesto (manifests/assets.yml) seja de fato a fonte de verdade:
que ele descreva exatamente o que existe em disco, que os identificadores sigam
o padrão canônico e que cada ativo carregue os metadados mínimos.

Arquitetura da verificação
--------------------------
A espinha autoritativa é `cycle_index`: uma linha por ciclo com `id`, `range`,
`theme`, `status` e `source_root`. O conteúdo de cada ciclo é o que existe em
disco sob o seu `source_root`. O bloco `cycles:` detalha ativos individuais
(usado para o ciclo ativo) e é validado por sobreposição quando presente.

Assim o manifesto não precisa repetir 600 linhas de ativo: ele indexa ciclos, e
o validador reconcilia índice × disco × plano.

Erros (saída != 0) cobrem integridade estrutural. Avisos (saída 0) cobrem
desvios de paleta em relação a docs/design-system/tokens.yml.

Uso:
    python3 tools/validate.py            # valida e imprime o relatório
    python3 tools/validate.py --strict   # trata avisos como erros também
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "manifests" / "assets.yml"
TOKENS = ROOT / "docs" / "design-system" / "tokens.yml"
ASSETS_DIR = ROOT / "assets"

ID_RE = re.compile(r"^HEX-([GAX])(\d{3})-(\d{3})$")
RANGE_RE = re.compile(r"^(\d+)-(\d+)$")
HEX_RE = re.compile(r"#[0-9A-Fa-f]{6}")

REQUIRED_ASSET_FIELDS = ("id", "concept", "status", "prompt", "alt", "consumers")
SOURCE_FILES = ("base-art.svg", "asset.yml")

LAYER_RANGES = {"G": (1, 200), "A": (201, 400), "X": (401, 600)}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def parse_range(text: str) -> tuple[int, int] | None:
    m = RANGE_RE.match(str(text).strip())
    if not m:
        return None
    return int(m.group(1)), int(m.group(2))


def check_id(asset_id: str, cycle_id: str, layer: str, rng: tuple[int, int],
             rep: Report) -> None:
    m = ID_RE.match(asset_id)
    if not m:
        rep.error(f"ID fora do padrão HEX-<layer><NNN>-<NNN>: {asset_id}")
        return
    id_layer, cycle_no, seq_no = m.group(1), int(m.group(2)), int(m.group(3))
    if id_layer != layer:
        rep.error(f"{asset_id}: camada '{id_layer}' diverge do ciclo {cycle_id} ('{layer}')")
    expected_cycle_no = int(cycle_id[1:])
    if cycle_no != expected_cycle_no:
        rep.error(
            f"{asset_id}: número de ciclo {cycle_no:03d} não corresponde a {cycle_id}"
        )
    lo, hi = rng
    if not lo <= seq_no <= hi:
        rep.error(
            f"{asset_id}: sequência {seq_no:03d} fora do intervalo do ciclo "
            f"{cycle_id} ({lo}-{hi})"
        )
    layer_lo, layer_hi = LAYER_RANGES.get(layer, (0, 0))
    if not layer_lo <= seq_no <= layer_hi:
        rep.error(
            f"{asset_id}: sequência {seq_no:03d} fora do intervalo da camada "
            f"{layer} ({layer_lo}-{layer_hi})"
        )


def validate_asset_metadata(asset_id: str, meta_path: Path, statuses: set[str],
                            rep: Report) -> None:
    try:
        meta = load_yaml(meta_path)
    except yaml.YAMLError as exc:
        rep.error(f"{asset_id}: YAML inválido em {meta_path.name}: {exc}")
        return
    if not isinstance(meta, dict):
        rep.error(f"{asset_id}: metadata não é um mapa YAML")
        return
    for field in REQUIRED_ASSET_FIELDS:
        if field not in meta or meta[field] in (None, "", []):
            rep.error(f"{asset_id}: campo obrigatório ausente/vazio: '{field}'")
    if meta.get("id") != asset_id:
        rep.error(
            f"{asset_id}: 'id' interno ({meta.get('id')}) não bate com a pasta"
        )
    if statuses and meta.get("status") not in statuses:
        rep.error(
            f"{asset_id}: status '{meta.get('status')}' fora da lista canônica"
        )


def validate_cycles(manifest: dict, rep: Report) -> int:
    """Reconcilia cycle_index × disco. Retorna a contagem real de ativos."""
    statuses = set(manifest.get("statuses", []) or [])
    index = manifest.get("cycle_index", []) or []
    seen_dirs: set[Path] = set()
    total = 0

    for entry in index:
        cycle_id = entry.get("id", "?")
        layer = cycle_id[0] if cycle_id else "?"
        rng = parse_range(entry.get("range", ""))
        source_root = entry.get("source_root")
        if rng is None:
            rep.error(f"{cycle_id}: range inválido no cycle_index: {entry.get('range')}")
            continue
        if not source_root:
            rep.error(f"{cycle_id}: cycle_index sem 'source_root'")
            continue

        root = ROOT / source_root
        if not root.is_dir():
            rep.error(f"{cycle_id}: source_root ausente em disco: {source_root}")
            continue

        lo, hi = rng
        for seq in range(lo, hi + 1):
            asset_id = f"HEX-{cycle_id}-{seq:03d}"
            asset_dir = root / asset_id
            seen_dirs.add(asset_dir)
            total += 1
            if not asset_dir.is_dir():
                rep.error(f"{cycle_id}: ativo esperado ausente em disco: {asset_id}")
                continue
            check_id(asset_id, cycle_id, layer, rng, rep)
            for required in SOURCE_FILES:
                if not (asset_dir / required).exists():
                    rep.error(f"{asset_id}: arquivo obrigatório ausente: {required}")
            meta_path = asset_dir / "asset.yml"
            if meta_path.exists():
                validate_asset_metadata(asset_id, meta_path, statuses, rep)

    # Todo diretório de ativo em disco precisa pertencer a um ciclo indexado.
    for asset_dir in sorted(ASSETS_DIR.rglob("HEX-*")):
        if asset_dir.is_dir() and asset_dir not in seen_dirs:
            rep.error(
                f"Ativo em disco fora de qualquer ciclo indexado: "
                f"{asset_dir.relative_to(ROOT)}"
            )

    return total


def validate_detailed_cycles(manifest: dict, rep: Report) -> None:
    """Valida o bloco `cycles:` (detalhe do ciclo ativo) contra o índice."""
    index_ids = {c.get("id") for c in manifest.get("cycle_index", []) or []}
    index_ranges = {
        c.get("id"): parse_range(c.get("range", ""))
        for c in manifest.get("cycle_index", []) or []
    }
    for cycle_id, cycle in (manifest.get("cycles", {}) or {}).items():
        if cycle_id not in index_ids:
            rep.error(f"Ciclo detalhado '{cycle_id}' ausente do cycle_index")
        rng = index_ranges.get(cycle_id)
        listed = cycle.get("assets", []) or []
        if rng:
            expected = rng[1] - rng[0] + 1
            if len(listed) != expected:
                rep.error(
                    f"{cycle_id}: bloco detalhado lista {len(listed)} ativos, "
                    f"esperado {expected} pelo range {rng[0]}-{rng[1]}"
                )
        for asset in listed:
            src = asset.get("source")
            meta = asset.get("metadata")
            if src and not (ROOT / src).exists():
                rep.error(f"{asset.get('id')}: source detalhado ausente: {src}")
            if meta and not (ROOT / meta).exists():
                rep.error(f"{asset.get('id')}: metadata detalhado ausente: {meta}")


def validate_counts(manifest: dict, real_count: int, rep: Report) -> None:
    production = manifest.get("production", {}) or {}
    declared = production.get("completed_assets")
    if declared is not None and declared != real_count:
        rep.error(
            f"production.completed_assets={declared} diverge da contagem real "
            f"em disco/índice ({real_count})"
        )


def validate_palette(rep: Report) -> None:
    if not TOKENS.exists():
        rep.warn("docs/design-system/tokens.yml ausente; pulei checagem de paleta")
        return
    tokens = load_yaml(TOKENS)
    canonical = {
        entry["hex"].upper() for entry in tokens.get("palette", []) if "hex" in entry
    }
    for svg in sorted(ASSETS_DIR.rglob("base-art.svg")):
        used = {c.upper() for c in HEX_RE.findall(svg.read_text(encoding="utf-8"))}
        stray = used - canonical
        if stray:
            rep.warn(
                f"{svg.parent.name}: {len(stray)} cor(es) fora dos tokens "
                f"canônicos: {', '.join(sorted(stray))}"
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict", action="store_true", help="tratar avisos como falha"
    )
    args = parser.parse_args()

    rep = Report()

    if not MANIFEST.exists():
        print(f"ERRO: manifesto não encontrado em {MANIFEST}", file=sys.stderr)
        return 2

    manifest = load_yaml(MANIFEST)
    real_count = validate_cycles(manifest, rep)
    validate_detailed_cycles(manifest, rep)
    validate_counts(manifest, real_count, rep)
    validate_palette(rep)

    print("Hexápode · validação do repositório-mãe")
    print(f"  ativos reconciliados (índice × disco): {real_count}")
    print(f"  erros:  {len(rep.errors)}")
    print(f"  avisos: {len(rep.warnings)}")
    print()

    for msg in rep.warnings:
        print(f"  AVISO  {msg}")
    for msg in rep.errors:
        print(f"  ERRO   {msg}")

    if rep.errors:
        return 1
    if args.strict and rep.warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
