"""
Gera um arquivo TXT fictício no mesmo layout esperado pelo script de
conciliação (19 dígitos no início da linha + 9+ colunas separadas por
espaço). Use este arquivo para testar/demonstrar o projeto no GitHub,
nunca um arquivo real de produção.
"""

import random
from datetime import datetime, timedelta

ARQUIVO_SAIDA = "exemplo_fake.txt"
QTD_REFERENCIAS = 30


def gerar_portador():
    # 19 dígitos fictícios (não é um número de cartão real)
    return "".join(str(random.randint(0, 9)) for _ in range(19))


def gerar_linha(referencia, parcela_num, parcela_total, data):
    portador = gerar_portador()
    data_compra = data.strftime("%d%m%Y")
    valor_compra = f"{random.randint(1000, 99999)}"
    cod_aut = f"{random.randint(100000, 999999)}"
    vlr_parc = f"{random.randint(100, 9999)}"
    vlr_orig = f"{random.randint(1000, 99999)}"
    parcela = f"{parcela_num:02d}/{parcela_total:02d}"
    operador = f"OP{random.randint(1, 20):03d}"
    mensagem = "TESTE SIMULADO"

    return (
        f"{portador} {data_compra} {valor_compra} {cod_aut} "
        f"{referencia} {vlr_parc} {vlr_orig} {parcela} {operador} {mensagem}\n"
    )


def main():
    linhas = []
    base_data = datetime(2026, 1, 1)

    for i in range(QTD_REFERENCIAS):
        referencia = f"REF{i:06d}"
        data = base_data + timedelta(days=random.randint(0, 200))
        total_parcelas = random.choice([2, 3, 6, 10, 12])

        # Sempre gera a parcela 00
        linhas.append(gerar_linha(referencia, 0, total_parcelas, data))

        # Em ~70% dos casos gera a parcela 01 também (simula os casos OK)
        # Nos outros ~30%, "esquece" de gerar -> simula a divergência real
        if random.random() < 0.7:
            linhas.append(gerar_linha(referencia, 1, total_parcelas, data))

    with open(ARQUIVO_SAIDA, "w", encoding="latin1") as f:
        f.writelines(linhas)

    print(f"Arquivo gerado: {ARQUIVO_SAIDA} ({len(linhas)} linhas)")


if __name__ == "__main__":
    main()