# Hexápode — Design System Canônico

Este diretório concentra os valores visuais compartilhados por todos os ativos
e pelos atlas consumidores. É a fonte única do design system: cor, tipografia,
canvas e cabeçalho vivem aqui, não copiados em cada SVG.

## Arquivos

- [`tokens.yml`](./tokens.yml) — tokens canônicos: paleta semântica, tints de
  preenchimento, escala tipográfica, dimensões de canvas e formatos de
  cabeçalho/rodapé.

## Paleta

A paleta se divide em famílias semânticas:

| Família      | Uso                                                    |
|--------------|--------------------------------------------------------|
| `surface-*`  | fundos de prancha e cartões                            |
| `ink-*`      | texto e traços                                         |
| `border-*`   | réguas e contornos                                     |
| `brand-*`    | azul da marca e variações                              |
| `accent-*`   | ciano, verde e âmbar de destaque                       |
| `anatomy-*`  | vermelho de sangue, terracota, roxo neural             |
| `tint-*`     | preenchimentos suaves derivados das matizes centrais   |

Os valores foram extraídos da produção canônica G001–G019 e representam o
padrão que toda nova prancha deve seguir.

## Validação

O validador [`tools/validate.py`](../../tools/validate.py) usa `tokens.yml`
como paleta canônica. Cores em um `base-art.svg` que não constem da lista
`palette` geram **aviso** (não bloqueiam), sinalizando ao revisor uma cor
one-off para conferência. A checagem roda automaticamente na
[GitHub Action de validação](../../.github/workflows/validate.yml).

```bash
python3 tools/validate.py           # relatório completo
python3 tools/validate.py --strict  # trata avisos de paleta como falha
```

## Como consumir

Atlas consumidores (Respira, Ventila, Cardio, Trauma, Neuro, Nefro, USG,
Farmacologia) devem referenciar os tokens deste arquivo em vez de redeclarar
cores. Ao alterar um valor canônico, altere-o **apenas** aqui; os SVGs de
produção que ainda embutem o valor literal devem ser migrados progressivamente
para casar com o token.
