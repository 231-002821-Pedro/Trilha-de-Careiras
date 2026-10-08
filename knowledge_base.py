from experta import Fact, KnowledgeEngine, Rule, MATCH


TRILHAS = {
    "backend": {
        "nome": "Desenvolvimento Back-end",
        "descricao": "Lógica de servidores, APIs, regras de negócio e bancos de dados.",
    },
    "frontend": {
        "nome": "Desenvolvimento Front-end & UI/UX",
        "descricao": "Interfaces web responsivas, experiência do usuário e frameworks reativos.",
    },
    "dados_ml": {
        "nome": "Ciência de Dados e Machine Learning",
        "descricao": "Estatística, modelagem preditiva, análise de dados e inteligência artificial.",
    },
    "eng_dados": {
        "nome": "Engenharia de Dados",
        "descricao": "Arquitetura de dados, pipelines ETL/ELT e infraestrutura para Data Lakes.",
    },
    "seguranca": {
        "nome": "Cibersegurança (Security / Pentesting)",
        "descricao": "Defesa cibernética, vulnerabilidades, criptografia e redes seguras.",
    },
    "devops": {
        "nome": "DevOps & SRE",
        "descricao": "Automação, integração e entrega contínua (CI/CD) e contêineres.",
    },
    "cloud": {
        "nome": "Computação em Nuvem (Cloud Architecture)",
        "descricao": "Planejamento, migração e gestão de infraestruturas escaláveis (AWS/Azure/GCP).",
    },
    "mobile": {
        "nome": "Desenvolvimento Mobile",
        "descricao": "Ecossistema móvel nativo ou multiplataforma (Flutter/React Native).",
    },
    "qa": {
        "nome": "Engenharia de Qualidade e Testes (QA)",
        "descricao": "Testes automatizados, confiabilidade de software e processos de qualidade.",
    },
    "produto": {
        "nome": "Gestão de Produtos (Product Management)",
        "descricao": "Ponte entre negócio, design e desenvolvimento, metodologias ágeis e priorização.",
    },
}

ORDEM_DESEMPATE = [
    "dados_ml",
    "eng_dados",
    "seguranca",
    "devops",
    "cloud",
    "backend",
    "frontend",
    "mobile",
    "qa",
    "produto",
]


class Perfil(Fact):
    pass


class Voto(Fact):
    pass


class CarreirasEngine(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.votos = []

    def _votar(self, trilha, regra, motivo):
        self.votos.append({"trilha": trilha, "regra": regra, "motivo": motivo})
        self.declare(Voto(trilha=trilha, regra=regra, motivo=motivo))

    @Rule(Perfil(atividade="backend", entrega="infra_sustenta"))
    def r01(self):
        self._votar("backend", "R01", "Preferência por lógica de servidores com entrega em infraestrutura (APIs/bancos).")

    @Rule(Perfil(atividade="backend", ferramenta="python", perfil="logico"))
    def r02(self):
        self._votar("backend", "R02", "Perfil lógico com afinidade em Python para regras de negócio.")

    @Rule(Perfil(atividade="frontend", ferramenta="javascript"))
    def r03(self):
        self._votar("frontend", "R03", "Preferência por interfaces com afinidade em JavaScript.")

    @Rule(Perfil(atividade="frontend", ferramenta="figma_css", perfil="visual"))
    def r04(self):
        self._votar("frontend", "R04", "Perfil visual com afinidade em layout (Figma/CSS).")

    @Rule(Perfil(matematica="alta", atividade="analise_dados", entrega="insights_dados"))
    def r05(self):
        self._votar("dados_ml", "R05", "Alta afinidade matemática com foco em análise e entrega em insights/modelos.")

    @Rule(Perfil(matematica="alta", ferramenta="python", atividade="analise_dados"))
    def r06(self):
        self._votar("dados_ml", "R06", "Alta matemática com Python aplicado à análise de dados.")

    @Rule(Perfil(atividade="pipelines", ferramenta="sql"))
    def r07(self):
        self._votar("eng_dados", "R07", "Preferência por pipelines com afinidade em SQL.")

    @Rule(Perfil(atividade="pipelines", entrega="infra_sustenta", matematica=MATCH.m))
    def r08(self, m):
        if m in ("media", "alta"):
            self._votar("eng_dados", "R08", "Foco em pipelines para sustentar infraestrutura de dados (ETL/Data Lake).")

    @Rule(Perfil(atividade="seguranca", entrega="seguranca_invasoes"))
    def r09(self):
        self._votar("seguranca", "R09", "Preferência por segurança com entrega em proteção contra invasões.")

    @Rule(Perfil(atividade="seguranca", ferramenta="linux_redes"))
    def r10(self):
        self._votar("seguranca", "R10", "Foco em segurança com afinidade em Linux/Redes.")

    @Rule(Perfil(atividade="automacao", ferramenta="docker_ci"))
    def r11(self):
        self._votar("devops", "R11", "Preferência por automação com afinidade em Docker/CI.")

    @Rule(Perfil(atividade="automacao", entrega="infra_sustenta", perfil="infra"))
    def r12(self):
        self._votar("devops", "R12", "Perfil de infraestrutura com foco em automação e CI/CD.")

    @Rule(Perfil(atividade="cloud", entrega="infra_sustenta"))
    def r13(self):
        self._votar("cloud", "R13", "Preferência por nuvem com entrega em infraestrutura escalável.")

    @Rule(Perfil(atividade="cloud", ferramenta="docker_ci"))
    def r14(self):
        self._votar("cloud", "R14", "Foco em nuvem com afinidade em contêineres e cloud.")

    @Rule(Perfil(atividade="mobile", entrega="produto_usuario"))
    def r15(self):
        self._votar("mobile", "R15", "Preferência por apps móveis com entrega no produto final.")

    @Rule(Perfil(atividade="mobile", ferramenta="flutter_rn"))
    def r16(self):
        self._votar("mobile", "R16", "Foco em mobile com afinidade em Flutter/React Native.")

    @Rule(Perfil(atividade="qa", entrega="qualidade_confiabilidade"))
    def r17(self):
        self._votar("qa", "R17", "Preferência por testes com entrega em qualidade e confiabilidade.")

    @Rule(Perfil(atividade="qa", perfil="logico"))
    def r18(self):
        self._votar("qa", "R18", "Perfil lógico aplicado a processos de qualidade.")

    @Rule(Perfil(atividade="produto", entrega="visao_negocio"))
    def r19(self):
        self._votar("produto", "R19", "Preferência por gestão com entrega em visão de negócio.")

    @Rule(Perfil(atividade="produto", perfil="comunicador", ferramenta="nenhuma"))
    def r20(self):
        self._votar("produto", "R20", "Perfil comunicador iniciante voltado a produto e agilidade.")

    @Rule(Perfil(matematica="alta", atividade="analise_dados", ferramenta="sql", entrega=MATCH.e), salience=10)
    def r21(self, e):
        if e == "insights_dados":
            self._votar("dados_ml", "R21", "Desempate DS vs Eng. Dados: análise com SQL voltada a insights favorece Ciência de Dados.")
        else:
            self._votar("eng_dados", "R21", "Desempate DS vs Eng. Dados: análise com SQL voltada a sustentação favorece Engenharia de Dados.")

    @Rule(Perfil(perfil="infra", ferramenta="docker_ci", atividade=MATCH.a), salience=10)
    def r22(self, a):
        if a == "automacao":
            self._votar("devops", "R22", "Desempate DevOps vs Cloud: automação com Docker indica DevOps/SRE.")
        elif a == "cloud":
            self._votar("cloud", "R22", "Desempate DevOps vs Cloud: arquitetura em nuvem indica Cloud.")

    @Rule(Perfil(perfil="logico", ferramenta="python", entrega=MATCH.e), salience=10)
    def r23(self, e):
        if e == "infra_sustenta":
            self._votar("backend", "R23", "Desempate Back vs QA: Python lógico para infraestrutura indica Back-end.")
        elif e == "qualidade_confiabilidade":
            self._votar("qa", "R23", "Desempate Back vs QA: Python lógico para confiabilidade indica QA.")

    @Rule(Perfil(ferramenta="nenhuma", perfil="comunicador"))
    def r24(self):
        self._votar("produto", "R24", "Iniciante com perfil comunicador tende a Gestão de Produtos.")

    @Rule(Perfil(ferramenta="nenhuma", perfil="visual"))
    def r25(self):
        self._votar("frontend", "R25", "Iniciante com perfil visual tende a Front-end.")


def recomendar(respostas):
    engine = CarreirasEngine()
    engine.reset()
    engine.declare(
        Perfil(
            matematica=respostas["matematica"],
            atividade=respostas["atividade"],
            ferramenta=respostas["ferramenta"],
            entrega=respostas["entrega"],
            perfil=respostas["perfil"],
        )
    )
    engine.run()
    if not engine.votos:
        return "produto", [], "Nenhuma regra disparada. Recomendação padrão por perfil generalista."
    contagem = {}
    for v in engine.votos:
        contagem[v["trilha"]] = contagem.get(v["trilha"], 0) + 1
    melhor = sorted(contagem.items(), key=lambda kv: (-kv[1], ORDEM_DESEMPATE.index(kv[0])))[0][0]
    motivos = [v for v in engine.votos if v["trilha"] == melhor]
    resumo = f"{len(motivos)} regra(s) disparada(s) para {TRILHAS[melhor]['nome']}."
    return melhor, motivos, resumo
