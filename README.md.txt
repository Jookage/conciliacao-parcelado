# Conciliação de Parcelamento — Detecção de Divergências

Script em Python que automatiza a conferência de arquivos de retorno de
parcelamento (formato posicional/TXT), identificando registros que quebram
uma regra de negócio: toda parcela inicial (00) deve possuir sua
parcela subsequente (01) correspondente. Quando isso não acontece, é
sinal de inconsistência no processamento que precisa ser tratada.

## Problema que resolve

Em operações de meios de pagamento, arquivos de retorno diário podem
conter milhares de linhas, valores, cabeçalhos e rodapés no momento da 
extração. Visando esse cenário, eu busquei simplificar esse processo, 
sabendo que no processamento e abertura de contratos parcelados, 
sempre são embarcados os registros 00 e 01, que para quem esse problema
pode vir a ocorrer, entende bem do que estou dizendo.
Esse processo nada mais é que separar todas essas partes faltantes, assim poupando
o tempo da procura e colocando esse tempo na análise.

## Como funciona

1. Lê todos os arquivos `.txt` de uma pasta
2. Filtra apenas as linhas que representam registros válidos (via regex)
3. Extrai os campos relevantes de cada linha (portador, valor, parcela, referência etc.)
4. Agrupa os registros por referência e compara a contagem de parcelas 00 vs 01
5. Gera uma planilha Excel formatada (cabeçalho em negrito, filtro automático,
   colunas ajustadas) somente com as referências divergentes, já indicando
   o tipo de falta

## Tecnologias

- Python 3
- pandas — agregação e comparação dos registros
- openpyxl — geração da planilha formatada
- re (regex) — validação de linhas

## Como rodar

```bash
pip install pandas openpyxl

# gera um arquivo de exemplo fictício para testar sem dados reais
python gerar_dados_fake.py

# roda a conciliação
python parcelado.py
```

O resultado é salvo em `DIVERGENCIAS_PARCELADO.xlsx`.

## Sobre os dados de exemplo

O arquivo `exemplo_fake.txt` (gerado por `gerar_dados_fake.py`) contém
dados **inteiramente sintéticos**, no mesmo layout estrutural usado pelo
script, sem qualquer relação com dados reais de produção. Este projeto
foi adaptado a partir de um script usado profissionalmente, com toda
informação sensível removida.

## Possíveis melhorias futuras

- Suporte a múltiplos formatos de entrada (CSV, largura fixa)
- Log estruturado
- Integração com outros relatórios que podem agregar valor ao que
estamos extraindo.
