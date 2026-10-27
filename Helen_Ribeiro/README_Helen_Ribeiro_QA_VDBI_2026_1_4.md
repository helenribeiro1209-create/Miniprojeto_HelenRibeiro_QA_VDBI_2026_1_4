# Instruções de Execução — Mini-Projeto Varejo

## Aluna

**Helen Ribeiro**

**Turma:** QA VDBI 2026/1 4

## Objetivo

Este arquivo apresenta as instruções para execução do Mini-Projeto Avaliativo de Análise Exploratória de Dados aplicado à base de Varejo.

## Arquivos do projeto

Os arquivos utilizados no projeto são:

- `Miniprojeto_Varejo.py` — script principal da análise;
- `Varejo.csv` — base de dados utilizada;
- `df_limpo.csv` — base de dados após as etapas de limpeza;
- `README.md` — documentação geral do projeto;
- `README_Helen_Ribeiro_QA_VDBI_2026_1_4.md` — instruções de execução e entrega.

## Como executar no Visual Studio Code

1. Abra o projeto no Visual Studio Code.
2. Acesse a pasta:

```text
Helen_Ribeiro
```

3. Verifique se os arquivos `Miniprojeto_Varejo.py` e `Varejo.csv` estão na mesma pasta.
4. Abra o terminal integrado do Visual Studio Code.
5. Execute o comando:

```bash
python Miniprojeto_Varejo.py
```

6. Aguarde a execução completa do script.
7. Ao final, o arquivo `df_limpo.csv` será criado ou atualizado automaticamente.

## Requisito

É necessário possuir Python instalado no computador e a biblioteca pandas disponível no ambiente.

Caso o pandas ainda não esteja instalado, utilize:

```bash
python -m pip install pandas
```

Depois, execute novamente:

```bash
python Miniprojeto_Varejo.py
```

## Execução no Google Colab

O projeto também pode ser executado no Google Colab.

Para isso:

1. Abra um novo notebook no Google Colab.
2. Faça o upload do arquivo `Varejo.csv`.
3. Insira o código do arquivo `Miniprojeto_Varejo.py` em uma célula ou adapte o script para o notebook.
4. Execute todas as células.
5. Ao final, será gerado o arquivo `df_limpo.csv`.

## Resultados da execução

A execução realizada durante o desenvolvimento apresentou:

- **830.000 registros** na base original;
- **14 colunas** inicialmente;
- **4 colunas completamente vazias** removidas;
- **0 valores nulos** nas colunas úteis;
- **0 datas inválidas**;
- **3.650 ocorrências de `#N/D`** identificadas na categoria;
- **96.553 duplicatas exatas** removidas;
- **733.447 registros** na base final.

### Estatística da coluna de número de filhos

A coluna analisada foi `CL_FHL`.

- Média: **1,1460**
- Mediana: **0**
- Desvio padrão: **1,4169**
- Moda: **0**
- Máximo: **4**
- Mínimo: **0**
- Contagem: **733.447**

### Principais agrupamentos

**Gênero:**  
O gênero `F` apresentou a maior quantidade de registros, com **382.427**.

**Categoria:**  
A categoria `ALIMENTOS` apresentou a maior quantidade de registros, com **384.197**.

**Período:**  
O mês com maior quantidade de registros foi **outubro de 2021**, com **28.575 registros**.

## Observação sobre os dados

A base não apresenta uma coluna explícita de preço ou valor da compra. Dessa forma, os agrupamentos realizados no projeto representam **quantidade de registros/compras**, e não faturamento.

A ocorrência de `#N/D` na coluna de categoria foi identificada como uma possível inconsistência remanescente e registrada para avaliação em uma etapa futura.

## Versionamento

O projeto foi organizado para ser enviado a um repositório público no GitHub, dentro da pasta correspondente ao nome da aluna.

A branch utilizada para o desenvolvimento do mini-projeto é:

```text
feat/miniprojeto-varejo
```

## Entrega

A pasta do projeto deve conter o script, a base utilizada, a base limpa e os arquivos de documentação solicitados.

Após a conferência final, os arquivos poderão ser enviados ao repositório GitHub e o link do repositório deverá ser submetido no AVA conforme as orientações da disciplina.
