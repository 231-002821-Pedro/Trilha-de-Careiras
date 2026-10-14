"""Consultor Inteligente de Carreiras em TI — Interface Streamlit (Fase 3)."""

import streamlit as st

from knowledge_base import TRILHAS, recomendar
from personas_teste import PERSONAS

st.set_page_config(
    page_title="Consultor de Carreiras em TI",
    page_icon="🧭",
    layout="centered",
)

OPCOES = {
    "matematica": [
        ("Baixa — prefiro evitar cálculos", "baixa"),
        ("Média — me viro bem", "media"),
        ("Alta — gosto de matemática/estatística", "alta"),
    ],
    "atividade": [
        ("Escrever lógica de servidores/APIs", "backend"),
        ("Criar layouts e interfaces visuais", "frontend"),
        ("Analisar dados e criar modelos/IA", "analise_dados"),
        ("Construir pipelines de dados (ETL)", "pipelines"),
        ("Investigar vulnerabilidades/proteger sistemas", "seguranca"),
        ("Automatizar deploys e processos (CI/CD)", "automacao"),
        ("Projetar infraestrutura em nuvem", "cloud"),
        ("Criar aplicativos mobile", "mobile"),
        ("Testar software e garantir qualidade", "qa"),
        ("Gerir produto, priorizar backlog, falar com stakeholders", "produto"),
    ],
    "ferramenta": [
        ("Python", "python"),
        ("JavaScript", "javascript"),
        ("SQL / Banco de dados", "sql"),
        ("Linux / Redes", "linux_redes"),
        ("Docker / CI / Nuvem", "docker_ci"),
        ("Figma / CSS", "figma_css"),
        ("Flutter / React Native", "flutter_rn"),
        ("Nenhuma / Iniciante", "nenhuma"),
    ],
    "entrega": [
        ("O produto final para o usuário", "produto_usuario"),
        ("A infraestrutura que sustenta o sistema", "infra_sustenta"),
        ("Insights e modelos a partir de dados", "insights_dados"),
        ("A segurança contra invasões", "seguranca_invasoes"),
        ("A qualidade e confiabilidade do software", "qualidade_confiabilidade"),
        ("A visão de negócio e evolução do produto", "visao_negocio"),
    ],
    "perfil": [
        ("Lógico — gosto de resolver problemas passo a passo", "logico"),
        ("Visual — penso em telas e experiência", "visual"),
        ("Investigativo — gosto de analisar e descobrir", "investigativo"),
        ("Infra — gosto de servidores e bastidores", "infra"),
        ("Comunicador — gosto de pessoas e organização", "comunicador"),
    ],
}


def _rotulos(opcoes):
    return [rotulo for rotulo, _ in opcoes]


def _codigo(opcoes, rotulo):
    for r, c in opcoes:
        if r == rotulo:
            return c
    raise ValueError(rotulo)


def mostrar_resultado(respostas):
    trilha, motivos, resumo = recomendar(respostas)
    info = TRILHAS[trilha]
    st.success(f"### 🧭 Trilha recomendada: {info['nome']}")
    st.write(info["descricao"])
    st.caption(resumo)
    if motivos:
        st.subheader("Por quê? Regras disparadas")
        for m in motivos:
            st.write(f"- **{m['regra']}**: {m['motivo']}")
    with st.expander("Ver respostas enviadas ao motor"):
        st.json(respostas)


st.title("🧭 Consultor Inteligente de Carreiras em TI")
st.write(
    "Responda à entrevista abaixo. O motor de inferência (Experta, 25 regras) "
    "recomenda **1 das 10 trilhas** e justifica a decisão."
)

aba_entrevista, aba_personas = st.tabs(["Entrevista", "Personas de teste (Fase 4)"])

with aba_entrevista:
    with st.form("entrevista"):
        esc_mat = st.radio("1. Afinidade com matemática e estatística", _rotulos(OPCOES["matematica"]))
        esc_atv = st.selectbox("2. Atividade diária preferida", _rotulos(OPCOES["atividade"]))
        esc_fer = st.selectbox("3. Linguagem/ferramenta de maior afinidade", _rotulos(OPCOES["ferramenta"]))
        esc_ent = st.selectbox("4. Tipo de entrega de valor preferida", _rotulos(OPCOES["entrega"]))
        esc_per = st.radio("5. Perfil de trabalho", _rotulos(OPCOES["perfil"]))
        enviar = st.form_submit_button("Recomendar trilha", type="primary")

    if enviar:
        respostas = {
            "matematica": _codigo(OPCOES["matematica"], esc_mat),
            "atividade": _codigo(OPCOES["atividade"], esc_atv),
            "ferramenta": _codigo(OPCOES["ferramenta"], esc_fer),
            "entrega": _codigo(OPCOES["entrega"], esc_ent),
            "perfil": _codigo(OPCOES["perfil"], esc_per),
        }
        mostrar_resultado(respostas)

with aba_personas:
    st.write("Valide o sistema com personas prontas (mesmas de `test_motor.py`).")
    escolha = st.selectbox(
        "Escolha uma persona",
        [p["nome"] for p in PERSONAS],
    )
    persona = next(p for p in PERSONAS if p["nome"] == escolha)
    st.info(persona["descricao"])
    if st.button("Diagnosticar persona"):
        mostrar_resultado(persona["respostas"])
        st.caption(f"Trilha esperada: {TRILHAS[persona['esperado']]['nome']}")

    if st.button("Rodar todas as personas"):
        linhas = []
        for p in PERSONAS:
            obtido, votos, _ = recomendar(p["respostas"])
            linhas.append(
                {
                    "Persona": p["nome"],
                    "Esperado": TRILHAS[p["esperado"]]["nome"],
                    "Obtido": TRILHAS[obtido]["nome"],
                    "Acertou": "✅" if obtido == p["esperado"] else "❌",
                    "Regras": len(votos),
                }
            )
        st.dataframe(linhas, use_container_width=True)
