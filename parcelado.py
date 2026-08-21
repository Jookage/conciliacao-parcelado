import re
from pathlib import Path

import pandas as pd
from openpyxl.styles import Font

PASTA = Path(".")
ARQUIVO_SAIDA = "DIVERGENCIAS_PARCELADO.xlsx"


def eh_registro(linha):
    return re.match(r"^\s*\d{19}", linha) is not None


def ler_txt(caminho):

    registros = []

    with open(caminho, "r", encoding="latin1", errors="ignore") as f:

        for linha in f:

            if not eh_registro(linha):
                continue

            partes = linha.split()

            # Garante que a linha possui todas as colunas
            if len(partes) < 9:
                continue

            try:

                parcela = partes[7]

                # Exemplo: 00/10
                numero_parcela = parcela.split("/")[0]

                # IGNORA parcelas 02,03,04...
                if numero_parcela not in ("00", "01"):
                    continue

                registros.append({

                    "PORTADOR": partes[0],
                    "DATA_COMPRA": partes[1],
                    "VALOR_COMPRA": partes[2],
                    "COD_AUT": partes[3],
                    "NR_REFERENCIA": partes[4],
                    "VLR_PARC": partes[5],
                    "VLR_ORIG": partes[6],
                    "PARCELA_COMPLETA": parcela,
                    "PARCELA": numero_parcela,
                    "TOTAL": parcela.split("/")[1],
                    "OPERADOR": partes[8],
                    "MENSAGEM": " ".join(partes[9:])

                })

            except:
                pass

    return registros


print("Lendo arquivos TXT...")

todos = []

arquivos = sorted(PASTA.glob("*.txt"))

if len(arquivos) == 0:
    print("Nenhum TXT encontrado.")
    exit()

for arquivo in arquivos:

    print(f"Processando {arquivo.name}")

    todos.extend(ler_txt(arquivo))


df = pd.DataFrame(todos)

if df.empty:
    print("Nenhum registro encontrado.")
    exit()


print()
print("Total de registros 00/01:", len(df))


divergencias = []


for referencia, grupo in df.groupby("NR_REFERENCIA"):

    qtd00 = (grupo["PARCELA"] == "00").sum()
    qtd01 = (grupo["PARCELA"] == "01").sum()

    # Se bateu, ignora
    if qtd00 == qtd01:
        continue

    diferenca = abs(qtd00 - qtd01)

    if qtd00 > qtd01:

        status = "FALTA PARCELA 01"

    else:

        status = "FALTA PARCELA 00"

    for _, linha in grupo.iterrows():

        nova = linha.copy()

        nova["QTD_00"] = qtd00
        nova["QTD_01"] = qtd01
        nova["DIFERENCA"] = diferenca
        nova["STATUS"] = status

        divergencias.append(nova)


resultado = pd.DataFrame(divergencias)


with pd.ExcelWriter(
    ARQUIVO_SAIDA,
    engine="openpyxl"
) as writer:

    resultado.to_excel(
        writer,
        sheet_name="Divergencias",
        index=False
    )

    ws = writer.sheets["Divergencias"]

    ws.freeze_panes = "A2"

    ws.auto_filter.ref = ws.dimensions

    for c in ws[1]:
        c.font = Font(bold=True)

    for coluna in ws.columns:

        maior = 0

        for celula in coluna:

            if celula.value:

                maior = max(maior, len(str(celula.value)))

        ws.column_dimensions[coluna[0].column_letter].width = maior + 3


total00 = (df["PARCELA"] == "00").sum()
total01 = (df["PARCELA"] == "01").sum()

print()
print("=" * 60)
print("RESUMO")
print("=" * 60)
print(f"Parcelas 00 : {total00}")
print(f"Parcelas 01 : {total01}")
print(f"Diferença   : {abs(total00-total01)}")
print(f"Referências com divergência : {resultado['NR_REFERENCIA'].nunique()}")
print()
print(f"Arquivo gerado: {ARQUIVO_SAIDA}")