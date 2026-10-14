"""Fase 4 — Personas de teste para validação do sistema.

Cada persona representa um perfil distinto e possui a trilha esperada.
Usado pela interface Streamlit (demonstração) e por test_motor.py
(validação automatizada).
"""

PERSONAS = [
    {
        "id": "analitica_ds",
        "nome": "Ana — Perfil Analítico (Ciência de Dados)",
        "descricao": "Gosta de matemática, Python e descobrir padrões em dados.",
        "respostas": {
            "matematica": "alta",
            "atividade": "analise_dados",
            "ferramenta": "python",
            "entrega": "insights_dados",
            "perfil": "investigativo",
        },
        "esperado": "dados_ml",
    },
    {
        "id": "engenheiro_dados",
        "nome": "Bruno — Perfil Dados/Infra (Engenharia de Dados)",
        "descricao": "Prefere construir pipelines e sustentar Data Lakes com SQL.",
        "respostas": {
            "matematica": "media",
            "atividade": "pipelines",
            "ferramenta": "sql",
            "entrega": "infra_sustenta",
            "perfil": "infra",
        },
        "esperado": "eng_dados",
    },
    {
        "id": "infra_seguranca",
        "nome": "Carla — Perfil Infra/Segurança (Cibersegurança)",
        "descricao": "Curte Linux, redes e proteger sistemas contra invasões.",
        "respostas": {
            "matematica": "media",
            "atividade": "seguranca",
            "ferramenta": "linux_redes",
            "entrega": "seguranca_invasoes",
            "perfil": "investigativo",
        },
        "esperado": "seguranca",
    },
    {
        "id": "automacao_devops",
        "nome": "Diego — Perfil Automação (DevOps & SRE)",
        "descricao": "Gosta de automatizar deploys com Docker e CI/CD.",
        "respostas": {
            "matematica": "media",
            "atividade": "automacao",
            "ferramenta": "docker_ci",
            "entrega": "infra_sustenta",
            "perfil": "infra",
        },
        "esperado": "devops",
    },
    {
        "id": "visual_frontend",
        "nome": "Elisa — Perfil Visual (Front-end & UI/UX)",
        "descricao": "Apaixonada por layouts, interfaces e experiência do usuário.",
        "respostas": {
            "matematica": "baixa",
            "atividade": "frontend",
            "ferramenta": "figma_css",
            "entrega": "produto_usuario",
            "perfil": "visual",
        },
        "esperado": "frontend",
    },
    {
        "id": "negocios_produto",
        "nome": "Fabio — Perfil Negócios (Product Management)",
        "descricao": "Iniciante em código, comunicativo, focado em visão de negócio.",
        "respostas": {
            "matematica": "baixa",
            "atividade": "produto",
            "ferramenta": "nenhuma",
            "entrega": "visao_negocio",
            "perfil": "comunicador",
        },
        "esperado": "produto",
    },
    {
        "id": "logico_backend",
        "nome": "Gabi — Perfil Lógico (Back-end)",
        "descricao": "Gosta de APIs, regras de negócio e banco de dados com Python.",
        "respostas": {
            "matematica": "media",
            "atividade": "backend",
            "ferramenta": "python",
            "entrega": "infra_sustenta",
            "perfil": "logico",
        },
        "esperado": "backend",
    },
    {
        "id": "cloud_infra",
        "nome": "Henrique — Perfil Nuvem (Cloud Architecture)",
        "descricao": "Quer projetar infraestruturas escaláveis em AWS/Azure/GCP.",
        "respostas": {
            "matematica": "media",
            "atividade": "cloud",
            "ferramenta": "docker_ci",
            "entrega": "infra_sustenta",
            "perfil": "infra",
        },
        "esperado": "cloud",
    },
    {
        "id": "mobile_apps",
        "nome": "Igor — Perfil Apps (Desenvolvimento Mobile)",
        "descricao": "Quer entregar apps com Flutter/React Native ao usuário final.",
        "respostas": {
            "matematica": "media",
            "atividade": "mobile",
            "ferramenta": "flutter_rn",
            "entrega": "produto_usuario",
            "perfil": "visual",
        },
        "esperado": "mobile",
    },
    {
        "id": "qa_qualidade",
        "nome": "Julia — Perfil Detalhista (QA)",
        "descricao": "Perfil lógico focado em testes e confiabilidade de software.",
        "respostas": {
            "matematica": "media",
            "atividade": "qa",
            "ferramenta": "python",
            "entrega": "qualidade_confiabilidade",
            "perfil": "logico",
        },
        "esperado": "qa",
    },
]
