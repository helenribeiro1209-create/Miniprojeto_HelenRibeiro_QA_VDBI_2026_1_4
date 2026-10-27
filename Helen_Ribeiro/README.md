# Mini-Projeto Avaliativo — Análise Exploratória de Dados de Varejo

## 👩‍💻 Aluna

**Helen Ribeiro**  
**Turma:** QA VDBI 2026/1 4

## 📌 Sobre o projeto

Este projeto apresenta uma **Análise Exploratória de Dados (AED)** aplicada a uma base de dados de varejo.

O objetivo é transformar dados brutos de compras em informações úteis por meio de etapas de importação, validação, limpeza, transformação, estatística descritiva e agrupamento dos dados.

A análise foi desenvolvida utilizando **Python e pandas**, seguindo as etapas propostas no Mini-Projeto Avaliativo.

## 🎯 Objetivos

- Importar a base de dados de varejo;
- Identificar problemas de qualidade nos dados;
- Verificar valores nulos e duplicados;
- Identificar possíveis inconsistências;
- Converter os tipos de dados necessários;
- Realizar limpeza e transformação dos dados;
- Calcular estatísticas descritivas;
- Analisar agrupamentos para identificar padrões;
- Registrar os principais resultados encontrados.

## 🛠️ Tecnologias utilizadas

- Python
- Pandas
- Visual Studio Code
- Git e GitHub

## 📂 Estrutura do projeto

```text
Miniprojeto_HelenRibeiro_QA_VDBI_2026_1_4/
└── Helen_Ribeiro/
    ├── Miniprojeto_Varejo.py
    ├── Varejo.csv
    ├── df_limpo.csv
    ├── README.md
    └── README_Helen_Ribeiro_QA_VDBI_2026_1_4.md
```

## 🔄 Sprints realizadas

### Sprint 1 — Importação dos dados

A base `Varejo.csv` foi carregada utilizando a função `read_csv()` do pandas.

Foram apresentados:

- número de registros;
- número de colunas;
- nomes das colunas;
- tipos de dados originais.

A base inicial possui **830.000 registros e 14 colunas**.

### Sprint 2 — Transformação dos dados

Foram realizadas transformações para preparar a base para análise:

- remoção de colunas completamente vazias;
- limpeza de espaços em campos de texto;
- normalização de espaços utilizando expressão regular;
- conversão de campos numéricos;
- conversão da coluna `DATA` para o tipo `datetime`.

As colunas `Unnamed: 10`, `Unnamed: 11`, `Unnamed: 12` e `Unnamed: 13` foram identificadas como completamente vazias e removidas.

### Sprint 3 — Limpeza de nulos e duplicatas

Foram realizadas verificações de:

- valores nulos;
- datas inválidas;
- categorias vazias;
- registros contendo `#N/D`;
- duplicatas exatas.

Não foram encontrados valores nulos nas colunas úteis da base e não foram encontradas datas inválidas.

Foram identificadas **96.553 duplicatas exatas**, que foram removidas.

Após a limpeza, a base passou de **830.000 para 733.447 registros**.

Também foram identificadas **3.650 ocorrências de `#N/D` na categoria** antes da remoção das duplicatas. Essa inconsistência foi registrada como um ponto de atenção para uma possível etapa futura de tratamento e padronização.

### Sprint 4 — Estatística descritiva

Foi realizada uma análise estatística da coluna `CL_FHL`, que representa o número de filhos do cliente.

| Estatística   | Resultado |
| ------------- | --------: |
| Média         |    1,1460 |
| Mediana       |         0 |
| Desvio padrão |    1,4169 |
| Moda          |         0 |
| Máximo        |         4 |
| Mínimo        |         0 |
| Contagem      |   733.447 |

### Sprint 5 — Agrupamentos e relatório

Foram utilizados agrupamentos com `groupby()` para observar padrões na base.

#### Gênero

O gênero com maior quantidade de registros foi **F**, com **382.427 registros**.

#### Categoria

A categoria com maior quantidade de registros foi **ALIMENTOS**, com **384.197 registros**.

#### Período

O mês com maior quantidade de registros foi **outubro de 2021**, representado por `2021-10`, com **28.575 registros**.

### Sprint 6 — Versionamento

Os arquivos do projeto foram organizados para envio ao repositório público do GitHub.

## 📊 Principais conclusões

1. A base possui grande volume de dados, com 830.000 registros inicialmente.
2. Foram identificadas e removidas 96.553 duplicatas exatas.
3. Não foram encontrados valores nulos ou datas inválidas nas colunas úteis.
4. O gênero `F` apresentou a maior quantidade de registros.
5. A categoria `ALIMENTOS` apresentou a maior quantidade de registros.
6. A categoria `#N/D` representa uma inconsistência de classificação que pode ser tratada em uma etapa futura.

## ⚠️ Observação sobre os agrupamentos

A base analisada não possui uma coluna explícita de valor ou preço da compra.

Por esse motivo, os agrupamentos realizados representam **quantidade de registros/compras**, e não faturamento ou valor total de vendas em reais.

## ▶️ Como executar

### Visual Studio Code

1. Abra a pasta do projeto no Visual Studio Code.
2. Abra o terminal na pasta `Helen_Ribeiro`.
3. Certifique-se de que o arquivo `Varejo.csv` está na mesma pasta do script.
4. Execute:

```bash
python Miniprojeto_Varejo.py
```

5. O script realizará a análise e criará automaticamente o arquivo:

```text
df_limpo.csv
```

### Google Colab

O script também pode ser executado no Google Colab, desde que o arquivo `Varejo.csv` seja disponibilizado no ambiente de execução.

## 📝 Nota de alinhamento técnico

Os critérios de avaliação que mencionam `csv.DictReader`, `if/else` e `datetime` são considerados neste projeto como referência aos conceitos de leitura estruturada de dados, lógica condicional e conversão de tipos.

A implementação utiliza as abordagens equivalentes disponíveis no pandas, incluindo:

- `pd.read_csv()`;
- `if/else`;
- `pd.to_datetime()`;
- `pd.to_numeric()`;
- `groupby()`.

Essa abordagem permite realizar as etapas de tratamento, validação e análise de forma reproduzível e adequada ao objetivo do projeto.

```

Esse é o **README principal**. Ele já está baseado nos resultados reais que você obteve no terminal, inclusive os **830.000 registros**, **96.553 duplicatas** e **733.447 registros finais**.

O próximo arquivo será o **`README_Helen_Ribeiro_QA_VDBI_2026_1_4.md`**, que podemos deixar mais focado nas **instruções de entrega e execução**, conforme o requisito do professor.
```
