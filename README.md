# Consultor de Carreiras em TI

Trabalho da disciplina de Inteligência Artificial (UNIPAC Barbacena).

O programa faz algumas perguntas sobre gostos e afinidades do usuário
(matemática, atividade do dia a dia, ferramenta, tipo de entrega e perfil)
e indica uma das 10 trilhas de TI, mostrando quais regras levaram a
essa resposta. O motor de regras foi feito com a biblioteca Experta
e a interface com Streamlit.

Trilhas: Back-end, Front-end e UI/UX, Ciência de Dados e ML, Engenharia
de Dados, Cibersegurança, DevOps e SRE, Cloud, Mobile, QA e Gestão
de Produtos.

## O que precisa

- Python 3.10 ou mais novo
- Git só para baixar o repositório

## Instalação

```bash
git clone <url-do-repositorio>
cd Trilha-de-Careiras
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
pip install -r requirements.txt
```

No Linux/Mac:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

## Rodando o programa

Com o venv ativado, na pasta do projeto:

```bash
streamlit run app.py
```

O terminal vai mostrar um endereço, normalmente http://localhost:8501.
É só abrir no navegador.

Na primeira aba dá para responder a entrevista e clicar em
"Recomendar trilha". Na segunda aba "Personas de teste" tem
exemplos prontos para ver se o sistema está acertando.

## Testando o motor sem abrir a interface

```bash
python test_motor.py
```

Ele passa pelas 10 personas de exemplo e confere se a trilha
recomendada é a esperada. Se estiver tudo certo, aparece
"10/10 personas passaram" no final.

## Arquivos

- `matriz_decisao.md` - tabela explicando como cada resposta
  pesa para cada trilha (fase 1 do trabalho).
- `knowledge_base.py` - base de fatos e as 25 regras do Experta,
  mais a função `recomendar()`.
- `app.py` - interface web feita em Streamlit.
- `personas_teste.py` - as 10 personas usadas na validação.
- `test_motor.py` - script que roda as personas e confere o resultado.
- `requirements.txt` - `experta`, `schema` e `streamlit`.

## Observações

- As perguntas da entrevista estão em `app.py`, nas opções de cada
  campo. Os valores internos (`backend`, `frontend`, etc.) seguem
  o padrão definido em `matriz_decisao.md`.
- Em caso de empate entre trilhas, o desempate segue a ordem
  definida em `ORDEM_DESEMPATE` no `knowledge_base.py`, além das
  regras R21, R22 e R23 que tratam os casos mais parecidos
  (Dados x Engenharia de Dados, DevOps x Cloud e Back-end x QA).
