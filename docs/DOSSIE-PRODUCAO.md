# Hexápode — Dossiê de Produção

Documento vivo de análise da biblioteca visual. Registra o estado, a qualidade
e a dívida de consistência dos projetos de desenho gerados, ciclo a ciclo.

> **Natureza dos ativos.** Cada `base-art.svg` é um **projeto de desenho**
> (blueprint de composição), não a lâmina final. O `base-art.png` listado em
> `exports_pending` é a lâmina a ser produzida; o `prompt` é o briefing de
> geração. A análise abaixo avalia os **projetos**.

- **Última atualização:** camada G completa (200/200).
- **Método:** leitura direta dos 200 SVGs e `asset.yml`, mais métricas
  automatizadas (elementos, viewBox, acessibilidade, dialeto de metadados) e o
  validador `tools/validate.py`.

---

## 1. Estado atual

| Métrica | Valor |
|---|---|
| Camada canônica (G) | **200/200 — completa** |
| Ciclos concluídos | G001–G020 |
| Próximo ciclo | A021 (camada aprofundada) |
| Validador | 0 erros · 23 avisos de paleta |
| Total do programa | 200/600 (33%) |

A camada G fecha 20 ciclos temáticos, de Identidade Visual (G001) a Biblioteca
Universal (G020). O conteúdo clínico/biológico é, em geral, **correto**; a
dívida é de **forma e consistência**, não de fundo.

---

## 2. Estratificação por geração (achado central)

A biblioteca foi construída em passes sucessivos que nunca foram reconciliados.
Um consumidor que puxa G003 recebe algo visivelmente diferente de G016.

| Geração | Ciclos | Cabeçalho de marca | viewBox | Fontes | Metadados | Acessibilidade |
|---|---|---|---|---|---|---|
| **Proto** | G001–G003 | ✗ | 1600×1200 + **7 sem viewBox** | mistas | mínimo (7 chaves) | irregular (23/30) |
| **Corpo** | G004–G011 | ✗ | 1600×1200 | Arial/Georgia | `review` + `source` + `overlay` | completa |
| **Ilha G012** | G012 | ✗ | **1200×900** (único) | genéricas (serif/sans/mono) | `review` + `source` | completa |
| **Marca** | G013–G017, G019 | ✓ `HEXÁPODE · TEMA` | 1600×1200 | Arial/Georgia | `review_gates` + `overlay` | completa |
| **Fora do padrão** | G018 | ✗ (tardio) | 1600×1200 | — | sem `review` | parcial |
| **Consolidação** | G020 | ✗ (só rodapé de marca) | 1600×1200 | Arial/Georgia | `review_gates` + `overlay` | **completa (10/10 TDA)** |

Observação sobre G020: adota a acessibilidade mais rica de toda a biblioteca
(title + desc + aria em todos os 10) e o formato de **rodapé** de marca
(`HEX-… · Hexápode · Tema`), mas **não** o cabeçalho-eyebrow `HEXÁPODE ·`.

---

## 3. Registro de dívida de consistência (quantificado)

| # | Defeito | Alcance | Severidade |
|---|---|---|---|
| D1 | Cabeçalho de marca (`HEXÁPODE ·`) ausente | 160/200 (só G013-17, G019 têm) | média — identidade visual fragmentada |
| D2 | SVG sem `viewBox` (usa `width/height`) | 7 (G003-024…030) | **alta** — quebra escala responsiva |
| D3 | viewBox fora do padrão 1600×1200 | 10 (G012 em 1200×900) | alta — desalinha em grid canônico |
| D4 | `<title>` ausente | ~89/200 | média — acessibilidade |
| D5 | `<desc>` ausente | ~63/200 | média — acessibilidade |
| D6 | 3 dialetos de metadados (`review` / `review_gates` / ausente) | todo o repo | média — contrato de dados instável |
| D7 | `source` presente só em G005–G012 | ~70 | baixa — campo opcional inconsistente |
| D8 | `alt_text` em vez de `alt` | G007 (10) | **resolvido** nesta branch |
| D9 | 23 cores fora dos tokens canônicos | 23 SVGs (avisos) | baixa — tints one-off para revisão |

---

## 4. Qualidade de conteúdo (o lado forte)

Os projetos maduros são didaticamente competentes e tecnicamente corretos.
Exemplos verificados:

- **G012-119 (Ânion Gap):** fórmula `AG = Na⁺ − (Cl⁻ + HCO₃⁻)`, comparação
  gap-alto vs. gap-normal com causas corretas, correção pela albumina destacada.
- **G020-198 (Microrganismos):** quatro categorias taxonômicas com descritores
  exatos (bactéria procariótica; vírus = genoma + cápside; fungo = levedura/hifa;
  protozoário = eucarioto unicelular).
- **G020-199 (Escalas visuais):** escada corpo→órgão→tecido→célula→organela→
  molécula alinhada à escala métrica (metros→nanômetros).
- **G020-200 (Biblioteca mestre):** catálogo de componentes reutilizáveis
  (cards, setas, status, ícones, gráficos, anatomia esquemática) — cumpre o
  papel de "componente mestre" previsto no plano.

Complexidade crescente e coerente com blueprints esquemáticos: de ~13 elementos
(G001) a 63 (G020-200), sem virar arte final — fiel à intenção.

---

## 5. Log por ciclo

Preenchido conforme a análise avança. `✓` = conforme ao padrão canônico atual
(Marca); `~` = funcional com desvio; `✗` = defeito estrutural.

| Ciclo | Tema | Marca | viewBox | a11y | Metadados | Nota |
|---|---|---|---|---|---|---|
| G001 | Identidade Visual | ✗ | ✓ | ~ | mínimo | proto; base da paleta |
| G002 | Anatomia Respiratória I | ✗ | ✓ | ✓ | review | — |
| G003 | Anatomia Respiratória II | ✗ | ✗ (7 sem vb) | ~ | review | **D2** |
| G004 | Mecânica Respiratória | ✗ | ✓ | ✓ | review | — |
| G005 | Fisiologia | ✗ | ✓ | ✓ | review+source | — |
| G006 | Equipamentos | ✗ | ✓ | ✓ | review+source | — |
| G007 | Curvas | ✗ | ✓ | ✓ | review+source | `alt_text`→`alt` corrigido |
| G008 | Modos Ventilatórios | ✗ | ✓ | ✓ | review+source | mais densos (~24 elem) |
| G009 | Assincronias | ✗ | ✓ | ✓ | review+source | — |
| G010 | Patologias Respiratórias | ✗ | ✓ | ✓ | review_gates | — |
| G011 | Via Aérea | ✗ | ✓ | ✓ | review+source | — |
| G012 | Gasometria | ✗ | ✗ (1200×900) | ✓ | review+source | **D3**; fontes genéricas |
| G013 | Hemodinâmica | ✓ | ✓ | ✓ | review_gates | 1ª geração Marca |
| G014 | Emergências | ✓ | ✓ | ✓ | review_gates | — |
| G015 | Farmacologia | ✓ | ✓ | ✓ | review_gates | — |
| G016 | Nefrologia | ✓ | ✓ | ✓ | review_gates | — |
| G017 | Neurologia | ✓ | ✓ | ✓ | review_gates | — |
| G018 | Cardiologia | ✗ | ✓ | ~ | sem review | **D1** tardio |
| G019 | Ultrassom | ✓ | ✓ | ✓ | review_gates | — |
| G020 | Biblioteca Universal | ~ (rodapé) | ✓ | ✓✓ | review_gates | a11y mais rica; fecha camada G |

---

## 6. Ações recomendadas

Ordem por retorno/risco:

1. **Padronizar viewBox** (D2, D3) — 7 do G003 + 10 do G012 para 1600×1200.
   Alto retorno, baixo risco. Candidato a erro de CI.
2. **Unificar dialeto de metadados** (D6, D7) para `review_gates` + `overlay`
   (o mais novo). Depois o validador passa a exigi-lo.
3. **Retro-aplicar cabeçalho de marca** (D1) às gerações Proto/Corpo/G012/G018/
   G020, para os 200 falarem a mesma língua visual.
4. **Fechar acessibilidade** (D4, D5) nos que faltam `<title>`/`<desc>`.
5. **Estender o validador** para transformar D1–D5 em verificações de convenção
   (hoje ele cobre integridade estrutural, não convenção visual).

---

## 7. Camada A (aprofundada) — próxima

O ciclo A021 inicia os ativos 201–400, que aprofundam os mesmos 200 conceitos.
Recomendação: **fixar o template canônico (Marca + a11y completa + dialeto
único) antes de iniciar A021**, para a camada aprofundada nascer consistente e
não herdar a estratificação da camada G.
