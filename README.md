# Hexápode

Repositório-mãe do ecossistema Hexápode.

O Hexápode concentra a infraestrutura visual, didática e operacional compartilhada pelos atlas Respira, Ventila, Cardio, Trauma, Neuro, Nefro, USG, Farmacologia e projetos futuros.

## Responsabilidades

- design system médico canônico;
- biblioteca visual de 600 ativos;
- prompts e metadados;
- componentes SVG e Canvas;
- templates editoriais;
- manifestos de produção;
- regras de integração e revisão;
- recursos reutilizáveis pelos atlas consumidores.

## Estrutura

```text
docs/
design-system/
assets/
  canonical/
  advanced/
  applied/
  components/
prompts/
manifests/
templates/
generators/
shared/
```

## Modelo de 600 ativos

A matriz contém 200 conceitos, cada um produzido em três camadas:

- `G`: canônica, ativos 001–200;
- `A`: aprofundada, ativos 201–400;
- `X`: aplicada, ativos 401–600.

Cada ciclo produz exatamente 10 imagens. O programa completo contém 60 ciclos.

## Repositórios consumidores

Respira e Ventila deram origem histórica ao projeto, mas não possuem prioridade estrutural sobre os demais braços. O Hexápode é a fonte canônica comum.

## Design system

Os valores visuais canônicos (paleta, tipografia, canvas, cabeçalho) vivem em [`docs/design-system/`](docs/design-system/README.md). São a fonte única de cor e tipo; os SVGs devem convergir para esses tokens em vez de redeclará-los.

## Validação

O manifesto (`manifests/assets.yml`) é a fonte de verdade do estado de produção. O validador garante que ele descreva exatamente o que existe em disco:

```bash
python3 tools/validate.py
```

Ele reconcilia `cycle_index` × disco, confere o padrão dos identificadores, os metadados mínimos de cada ativo e a contagem de ativos concluídos, e sinaliza cores fora dos tokens canônicos. A checagem roda automaticamente em cada push e pull request via [GitHub Actions](.github/workflows/validate.yml).