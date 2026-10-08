# Fase 1 — Engenharia de Conhecimento e Matriz de Decisão

## 1. Lógica escolhida: Dedutiva

Conforme matriz de referência (Geral → Específico, pergunta central "o que essa regra dita sobre este caso?", cenário ideal "problemas rígidos e bem definidos"), o sistema usa lógica **dedutiva** com encadeamento para frente (Experta).

Regras no formato SE-ENTÃO partem de fatos gerais coletados na entrevista e derivam uma conclusão específica (1 das 10 trilhas). Não se usa lógica indutiva (inferir padrão de grandes volumes de dados), abdutiva (diagnosticar causa a partir de sintoma isolado) nem CBR (comparar com histórico de casos), porque o domínio é rígido: perfis mapeáveis em regras explícitas e justificáveis.

## 2. Fatos coletados na entrevista

| ID | Pergunta | Valores possíveis |
|----|----------|-------------------|
| Q1 | Afinidade com matemática e estatística | `baixa`, `media`, `alta` |
| Q2 | Atividade diária preferida | `backend`, `frontend`, `analise_dados`, `pipelines`, `seguranca`, `automacao`, `cloud`, `mobile`, `qa`, `produto` |
| Q3 | Linguagem / ferramenta de maior afinidade | `python`, `javascript`, `sql`, `linux_redes`, `docker_ci`, `figma_css`, `flutter_rn`, `nenhuma` |
| Q4 | Tipo de entrega de valor preferida | `produto_usuario`, `infra_sustenta`, `insights_dados`, `seguranca_invasoes`, `qualidade_confiabilidade`, `visao_negocio` |
| Q5 | Perfil de trabalho | `logico`, `visual`, `investigativo`, `infra`, `comunicador` |

Q2 cobre "preferência de atuação diária", Q3 cobre "linguagem/ferramenta", Q4 cobre "entrega de valor", Q1 cobre "afinidade matemática", Q5 fecha ambiguidade entre perfis próximos.

## 3. Matriz de decisão (resposta → trilha)

| Trilha | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|----|----|----|----|----|
| 1. Back-end | media, alta | backend | python, sql | infra_sustenta | logico |
| 2. Front-end & UI/UX | baixa, media | frontend | javascript, figma_css | produto_usuario | visual |
| 3. Ciência de Dados / ML | alta | analise_dados | python | insights_dados | investigativo |
| 4. Engenharia de Dados | media, alta | pipelines | sql, python | infra_sustenta, insights_dados | infra, logico |
| 5. Cibersegurança | media | seguranca | linux_redes | seguranca_invasoes | investigativo |
| 6. DevOps & SRE | media | automacao | docker_ci, linux_redes | infra_sustenta | infra |
| 7. Cloud Architecture | media | cloud | docker_ci, linux_redes | infra_sustenta | infra |
| 8. Mobile | baixa, media | mobile | flutter_rn, javascript | produto_usuario | logico, visual |
| 9. QA | baixa, media | qa | nenhuma, python, javascript | qualidade_confiabilidade | logico |
| 10. Product Management | baixa, media | produto | nenhuma | visao_negocio | comunicador |

Diferenciações críticas:

- **DS (3) vs Eng. Dados (4):** ambos usam Python e matemática, mas DS tem `Q2=analise_dados + Q4=insights_dados + Q5=investigativo`; Eng. Dados tem `Q2=pipelines + Q3=sql + Q4=infra_sustenta`. Regras de desempate priorizam Q2 e Q4.
- **DevOps (6) vs Cloud (7):** ambos infra, mas DevOps tem `Q2=automacao + Q3=docker_ci + foco em CI/CD`; Cloud tem `Q2=cloud + foco em migração/arquitetura escalável`.
- **Back-end (1) vs QA (9):** ambos lógicos, mas Back-end entrega `infra_sustenta` (APIs/banco) e QA entrega `qualidade_confiabilidade` (testes).
- **Front-end (2) vs Mobile (8) vs PM (10):** Front e Mobile entregam `produto_usuario`, mas Front usa `javascript/figma_css + visual`, Mobile usa `flutter_rn + mobile`, PM entrega `visao_negocio + comunicador`.

## 4. Mapeamento em 25 regras (a implementar na Fase 2)

| Regra | Conclusão | Condição (SE) |
|-------|-----------|---------------|
| R01 | Back-end | Q2=backend AND Q4=infra_sustenta |
| R02 | Back-end | Q2=backend AND Q3=python AND Q5=logico |
| R03 | Front-end | Q2=frontend AND Q3=javascript |
| R04 | Front-end | Q2=frontend AND Q3=figma_css AND Q5=visual |
| R05 | DS / ML | Q1=alta AND Q2=analise_dados AND Q4=insights_dados |
| R06 | DS / ML | Q1=alta AND Q3=python AND Q2=analise_dados |
| R07 | Eng. Dados | Q2=pipelines AND Q3=sql |
| R08 | Eng. Dados | Q2=pipelines AND Q4=infra_sustenta AND Q1!=baixa |
| R09 | Cibersegurança | Q2=seguranca AND Q4=seguranca_invasoes |
| R10 | Cibersegurança | Q2=seguranca AND Q3=linux_redes |
| R11 | DevOps & SRE | Q2=automacao AND Q3=docker_ci |
| R12 | DevOps & SRE | Q2=automacao AND Q4=infra_sustenta AND Q5=infra |
| R13 | Cloud | Q2=cloud AND Q4=infra_sustenta |
| R14 | Cloud | Q2=cloud AND Q3=docker_ci |
| R15 | Mobile | Q2=mobile AND Q4=produto_usuario |
| R16 | Mobile | Q2=mobile AND Q3=flutter_rn |
| R17 | QA | Q2=qa AND Q4=qualidade_confiabilidade |
| R18 | QA | Q2=qa AND Q5=logico |
| R19 | Product Management | Q2=produto AND Q4=visao_negocio |
| R20 | Product Management | Q2=produto AND Q5=comunicador AND Q3=nenhuma |
| R21 | Desempate DS vs Eng. Dados | Q1=alta AND Q2=analise_dados AND Q3=sql → prioriza DS se Q4=insights_dados, senão Eng. Dados |
| R22 | Desempate DevOps vs Cloud | Q5=infra AND Q3=docker_ci → DevOps se Q2=automacao, Cloud se Q2=cloud |
| R23 | Desempate Back vs QA | Q5=logico AND Q3=python → Back se Q4=infra_sustenta, QA se Q4=qualidade_confiabilidade |
| R24 | Fallback iniciante-produto | Q3=nenhuma AND Q5=comunicador → Product Management |
| R25 | Fallback iniciante-visual | Q3=nenhuma AND Q5=visual → Front-end |

Cada recomendação registra as regras disparadas para exibição da justificativa na interface.
