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