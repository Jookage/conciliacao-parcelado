Conciliação de Parcelamentos — Detecção de Divergências

Automação desenvolvida em Python para conferir grandes volumes de registros em arquivos TXT posicionais e identificar divergências entre parcelas relacionadas.

O script aplica uma regra de negócio segundo a qual cada registro de parcela inicial "00" deve possuir uma parcela subsequente "01" correspondente. Quando o par não é encontrado, a ocorrência é separada automaticamente para análise.

«Este projeto utiliza exclusivamente dados fictícios e anonimizados. Nomes, números, referências, valores e demais informações não possuem relação com dados reais.»

O problema

Arquivos de retorno podem conter milhares de linhas, além de cabeçalhos, rodapés, registros inválidos e informações que não fazem parte da análise.

Durante a conferência manual, seria necessário:

- Localizar os registros válidos;
- Identificar as parcelas "00" e "01";
- Relacionar os registros pela referência;
- Comparar a quantidade de cada parcela;
- Encontrar pares incompletos;
- Organizar as divergências para análise.

Além de repetitivo, esse processo consome tempo que poderia ser direcionado à investigação das inconsistências encontradas.

A solução

A automação percorre todos os arquivos TXT de uma pasta, extrai somente os registros relevantes, aplica as regras de validação e compara automaticamente as parcelas relacionadas.

Ao final, é gerada uma planilha Excel contendo apenas as referências divergentes, já classificadas conforme o tipo de inconsistência identificada.

Assim, a procura manual é substituída por um fluxo automatizado, enquanto a decisão sobre o tratamento permanece sob responsabilidade humana.

Regra de negócio

A validação considera a relação esperada entre dois registros:

Parcela 00 → Parcela 01 correspondente

Quando a relação está completa:

Referência A
├── Parcela 00
└── Parcela 01

O registro é considerado consistente e não aparece no relatório final.

Quando uma das partes está ausente:

Referência B
├── Parcela 00
└── Parcela 01 ausente

A referência é classificada como divergente e enviada para a planilha de saída.

Como funciona

O processamento acontece nas seguintes etapas:

1. Localiza todos os arquivos ".txt" da pasta definida;
2. Realiza a leitura dos arquivos;
3. Descarta cabeçalhos, rodapés e linhas fora do padrão;
4. Valida os registros por meio de expressões regulares;
5. Extrai os campos necessários para a conciliação;
6. Identifica as parcelas "00" e "01";
7. Agrupa os registros por uma referência comum;
8. Compara a quantidade de parcelas de cada grupo;
9. Classifica as divergências encontradas;
10. Gera uma planilha Excel pronta para análise.

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
Comparação entre 00 e 01
      ↓
Identificação das divergências
      ↓
Relatório Excel

Recursos do projeto

- Processamento de múltiplos arquivos TXT;
- Tratamento de grandes volumes de registros;
- Validação de linhas com expressões regulares;
- Extração de dados em formato posicional;
- Agrupamento por referência;
- Comparação automática entre parcelas;
- Identificação de pares incompletos;
- Classificação do tipo de divergência;
- Exportação apenas das exceções encontradas;
- Cabeçalho formatado em negrito;
- Filtros automáticos;
- Ajuste da largura das colunas;
- Base sintética para testes seguros.

Tecnologias utilizadas

Tecnologia| Aplicação
Python 3| Desenvolvimento da automação
pandas| Organização, agrupamento e comparação dos registros
openpyxl| Geração e formatação da planilha Excel
Regex ("re")| Validação e extração dos registros
pathlib| Localização e manipulação dos arquivos

Estrutura do projeto

conciliacao-parcelamentos/
├── parcelado.py
├── gerar_dados_fake.py
├── exemplo_fake.txt
├── requirements.txt
└── README.md

Arquivo| Descrição
"parcelado.py"| Executa a conciliação e gera o relatório
"gerar_dados_fake.py"| Cria uma base inteiramente sintética para testes
"exemplo_fake.txt"| Exemplo fictício de arquivo de entrada
"requirements.txt"| Dependências necessárias para execução
"README.md"| Documentação do projeto

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

Ou, caso o projeto possua o arquivo de dependências:

pip install -r requirements.txt

5. Gere uma base fictícia

python gerar_dados_fake.py

Esse comando cria um arquivo de exemplo com registros sintéticos, incluindo casos consistentes e divergentes.

6. Execute a conciliação

python parcelado.py

Resultado

Após o processamento, o programa gera o arquivo:

DIVERGENCIAS_PARCELADO.xlsx

A planilha contém somente as referências que não atenderam à regra de conciliação, permitindo que a análise seja concentrada nas exceções.

Exemplo conceitual:

Referência| Parcela 00| Parcela 01| Resultado
REF-0001| 1| 1| Consistente
REF-0002| 1| 0| Falta parcela 01
REF-0003| 0| 1| Falta parcela 00

Os nomes, valores e referências apresentados acima são exclusivamente ilustrativos.

Sobre os dados de exemplo

O arquivo "exemplo_fake.txt", criado por "gerar_dados_fake.py", contém dados inteiramente sintéticos.

Embora preserve uma estrutura compatível com o funcionamento do algoritmo, ele não reproduz:

- Dados pessoais;
- Números de contas ou cartões reais;
- Referências internas;
- Valores de produção;
- Nomes de empresas ou instituições;
- Arquivos operacionais reais;
- Informações confidenciais de terceiros.

O projeto foi reconstruído para fins de portfólio e demonstração técnica, mantendo apenas a lógica genérica de processamento, conciliação e detecção de divergências.

Conhecimentos demonstrados

Este projeto demonstra a aplicação prática de:

- Leitura e tratamento de arquivos semiestruturados;
- Processamento de dados em lote;
- Expressões regulares;
- Regras de negócio;
- Validação e conciliação de registros;
- Detecção de inconsistências;
- Manipulação de dados com pandas;
- Geração automatizada de relatórios;
- Separação entre processamento automático e análise humana.

Possíveis melhorias

- Suporte a arquivos CSV e outros layouts posicionais;
- Parametrização das regras de conciliação;
- Processamento de arquivos em subpastas;
- Criação de logs estruturados;
- Registro de arquivos processados e rejeitados;
- Geração de resumo executivo;
- Painel com indicadores de divergência;
- Testes automatizados;
- Interface para seleção dos arquivos;
- Integração com outros relatórios complementares.

Aviso de privacidade

Este repositório não contém código proprietário, dados operacionais reais ou informações capazes de identificar pessoas, empresas ou instituições.

Todos os exemplos foram criados exclusivamente para demonstrar conhecimentos em Python, tratamento de dados e automação de processos.