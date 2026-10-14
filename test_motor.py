"""Validação automatizada do motor de inferência (Fase 4).

Executa todas as personas de `personas_teste.py` e verifica se a trilha
recomendada é a esperada. Uso:
    python test_motor.py
Retorna exit code 0 se todas passarem, 1 caso contrário.
"""

from knowledge_base import recomendar, TRILHAS
from personas_teste import PERSONAS


def main():
    falhas = 0
    print(f"{'Persona':<45} {'Esperado':<12} {'Obtido':<12} Resultado")
    print("-" * 90)
    for p in PERSONAS:
        obtido, votos, resumo = recomendar(p["respostas"])
        ok = obtido == p["esperado"]
        falhas += 0 if ok else 1
        print(
            f"{p['nome']:<45} {p['esperado']:<12} {obtido:<12} "
            f"{'OK' if ok else 'FALHOU'} ({len(votos)} voto(s))"
        )
        if not ok:
            print(f"  Respostas: {p['respostas']}")
            print(f"  Resumo: {resumo}")
    print("-" * 90)
    print(f"{len(PERSONAS) - falhas}/{len(PERSONAS)} personas passaram.")
    if falhas:
        raise SystemExit(1)
    print("Motor validado com sucesso.")


if __name__ == "__main__":
    main()
