Conciliação de Parcelamentos — Detecção de Divergências

Automação desenvolvida em Python para processar grandes volumes de registros em arquivos TXT posicionais e identificar divergências entre parcelas relacionadas.

O script localiza os registros válidos, extrai os campos necessários e aplica uma regra de negócio: cada parcela inicial "00" deve possuir uma parcela "01" correspondente. As inconsistências encontradas são organizadas automaticamente em uma planilha Excel pronta para análise.

Objetivo

Substituir a procura manual por parcelas ausentes por um fluxo automatizado de leitura, validação e conciliação.

Dessa forma, o tempo deixa de ser gasto localizando registros em arquivos extensos e passa a ser direcionado à análise das divergências encontradas.

Funcionalidades

- Leitura de múltiplos arquivos TXT;
- Processamento de grandes volumes de registros;
- Remoção de cabeçalhos, rodapés e linhas inválidas;
- Validação dos registros com expressões regulares;
- Extração de campos em layout posicional;
- Identificação das parcelas "00" e "01";
- Agrupamento dos registros por referência;
- Comparação automática entre parcelas relacionadas;
- Detecção de pares incompletos;
- Classificação do tipo de divergência;
- Geração de uma planilha somente com as exceções;
- Formatação automática do arquivo Excel;
- Geração de dados fictícios para testes.

Fluxo do processamento

Arquivos TXT
    ↓
Leitura dos registros
    ↓
Validação com Regex
    ↓
Extração dos campos
    ↓
Agrupamento por referência
    ↓
Comparação entre parcelas 00 e 01
    ↓
Identificação das divergências
    ↓
Geração do Excel

Regra de negócio

Para cada referência processada, o programa verifica a existência das parcelas relacionadas.

O comportamento esperado é:

Parcela 00 → Parcela 01 correspondente

Exemplo de registro consistente:

Referência A
├── Parcela 00
└── Parcela 01

Exemplo de divergência:

Referência B
├── Parcela 00
└── Parcela 01 ausente

Quando a quantidade de parcelas "00" e "01" não corresponde, a referência é classificada como divergente e adicionada ao relatório final.

Etapas do tratamento

Durante o processamento, o script:

1. Localiza os arquivos ".txt" na pasta definida;
2. Lê e percorre os registros encontrados;
3. Ignora cabeçalhos, rodapés e linhas fora do padrão;
4. Valida cada linha com expressões regulares;
5. Extrai os campos necessários para a conciliação;
6. Identifica o número da parcela;
7. Agrupa os registros pela referência correspondente;
8. Compara a quantidade de parcelas "00" e "01";
9. Separa somente as referências divergentes;
10. Gera a planilha Excel formatada.

Tecnologias utilizadas

- Python
- pandas
- openpyxl
- Expressões regulares — Regex
- pathlib

Estrutura do projeto

projeto/
├── parcelado.py
├── gerar_dados_fake.py
├── exemplo_fake.txt
├── requirements.txt
└── README.md

Como executar

1. Clone o repositório

git clone URL_DO_REPOSITORIO
cd NOME_DO_REPOSITORIO

2. Crie um ambiente virtual

python -m venv .venv

3. Ative o ambiente

No Windows:

.venv\Scripts\activate

No Linux ou macOS:

source .venv/bin/activate

4. Instale as dependências

pip install pandas openpyxl

Ou utilize o arquivo de dependências:

pip install -r requirements.txt

5. Gere o arquivo de exemplo

python gerar_dados_fake.py

Esse comando cria o arquivo "exemplo_fake.txt", contendo registros sintéticos para demonstrar o funcionamento da conciliação.

6. Execute o processamento

python parcelado.py

Resultado

O programa gera automaticamente o arquivo:

DIVERGENCIAS_PARCELADO.xlsx

A planilha apresenta somente as referências que quebraram a regra de conciliação.

Exemplo:

Referência| Parcela 00| Parcela 01| Divergência
REF-0001| 1| 0| Parcela 01 ausente
REF-0002| 0| 1| Parcela 00 ausente
REF-0003| 2| 1| Quantidade incompatível

A saída também inclui:

- Cabeçalhos destacados;
- Filtros automáticos;
- Colunas ajustadas ao conteúdo;
- Indicação do tipo de divergência;
- Apenas os registros que precisam de análise.

Diferenciais técnicos

O projeto combina processamento em lote, expressões regulares e regras de negócio para transformar arquivos TXT extensos em uma lista objetiva de exceções.

Em vez de exigir a conferência manual de todos os registros, a automação filtra os casos consistentes e direciona para análise humana somente as referências que apresentam divergências.

Sobre os dados

Todos os arquivos utilizados neste repositório contêm dados inteiramente sintéticos e anonimizados.

O arquivo "exemplo_fake.txt", gerado pelo script "gerar_dados_fake.py", mantém apenas uma estrutura fictícia compatível com o funcionamento da automação.

O projeto não contém:

- Dados pessoais reais;
- Números de contas ou cartões;
- Referências internas;
- Valores de produção;
- Nomes de empresas ou instituições;
- Arquivos operacionais;
- Informações confidenciais de terceiros.

Possíveis melhorias

- Suporte a arquivos CSV e outros layouts posicionais;
- Parametrização das regras de conciliação;
- Geração de logs estruturados;
- Testes automatizados;
- Resumo executivo do processamento;
- Painel com indicadores de divergências;
- Interface para seleção dos arquivos;
- Integração com relatórios complementares.

Aviso

Este projeto foi reconstruído exclusivamente para fins educacionais e de portfólio. Sua lógica foi generalizada, e todos os dados, nomes, formatos e referências apresentados são fictícios ou anonimizados.