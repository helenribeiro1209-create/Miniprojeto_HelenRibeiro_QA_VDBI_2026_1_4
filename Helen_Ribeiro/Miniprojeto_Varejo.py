import pandas as pd

ARQUIVO_ENTRADA = "Varejo.csv"
ARQUIVO_SAIDA = "df_limpo.csv"

# SPRINT 1 - IMPORTAÇÃO DOS DADOS

print("=" * 75)
print("SPRINT 1 - IMPORTAÇÃO DOS DADOS")
print("=" * 75)

# Leitura estruturada da base utilizando pandas.
df = pd.read_csv(
    ARQUIVO_ENTRADA,
    sep=";",
    encoding="utf-8"
)

print(f"Número de registros: {len(df):,}")
print(f"Número de colunas: {len(df.columns)}")

print("\nColunas:")
print(df.columns.tolist())

print("\nTipos de dados originais:")
print(df.dtypes)

# SPRINT 2 - TRANSFORMAÇÃO DE STRINGS, INTEGER E DATETIME

print("\n" + "=" * 75)
print("SPRINT 2 - TRANSFORMAÇÃO DOS DADOS")
print("=" * 75)

# Remove colunas completamente vazias.
colunas_vazias = [
    coluna
    for coluna in df.columns
    if df[coluna].isna().all()
]

if colunas_vazias:
    print("Colunas completamente vazias removidas:")
    print(colunas_vazias)
    df = df.drop(columns=colunas_vazias)
else:
    print("Não existem colunas completamente vazias.")


# Limpeza de strings e normalização de espaços.
# A expressão regular r"\s+" identifica um ou mais espaços.
colunas_texto = [
    coluna
    for coluna in [
        "CL_ID",
        "CL_GENERO",
        "CL_EC",
        "CL_SEG",
        "PR_ID",
        "PR_CAT",
        "PR_NOME"
    ]
    if coluna in df.columns
]

for coluna in colunas_texto:
    df[coluna] = (
        df[coluna]
        .astype("string")
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )


# Conversão dos campos que representam números inteiros.
for coluna in ["CL_FHL", "CO_ID"]:
    if coluna in df.columns:
        df[coluna] = pd.to_numeric(
            df[coluna],
            errors="coerce"
        ).astype("Int64")


# Conversão da coluna DATA para datetime.
# dayfirst=True considera o formato brasileiro dd/mm/aaaa.
df["DATA"] = pd.to_datetime(
    df["DATA"],
    errors="coerce",
    dayfirst=True
)

print("\nTipos de dados após as transformações:")
print(df.dtypes)

# SPRINT 3 - LIMPEZA DE NULOS E DUPLICATAS

print("\n" + "=" * 75)
print("SPRINT 3 - LIMPEZA DE NULOS E DUPLICATAS")
print("=" * 75)


# Verifica os valores nulos por coluna.
nulos_por_coluna = df.isna().sum()
total_nulos = int(nulos_por_coluna.sum())

print("Valores nulos por coluna:")
print(nulos_por_coluna)

if total_nulos > 0:
    print(f"\nForam encontrados {total_nulos:,} valores nulos.")
else:
    print("\nNão foram encontrados valores nulos.")


# Verifica datas inválidas após a conversão.
datas_invalidas = int(df["DATA"].isna().sum())

if datas_invalidas > 0:
    print(
        f"Datas inválidas após conversão: "
        f"{datas_invalidas:,}"
    )
else:
    print("Não foram encontradas datas inválidas.")


# Verifica categorias vazias.
categorias_vazias = (
    df["PR_CAT"].isna()
    | (df["PR_CAT"].astype("string").str.strip() == "")
)

quantidade_categorias_vazias = int(
    categorias_vazias.sum()
)

if quantidade_categorias_vazias > 0:
    print(
        f"Categorias vazias/nulas: "
        f"{quantidade_categorias_vazias:,}"
    )
else:
    print("Não foram encontradas categorias vazias/nulas.")


# Verifica a possível inconsistência #N/D.
categoria_nd = (
    df["PR_CAT"]
    .astype("string")
    .str.strip()
    .str.upper()
    == "#N/D"
)

quantidade_categoria_nd = int(categoria_nd.sum())

print(
    f"Categorias contendo '#N/D': "
    f"{quantidade_categoria_nd:,}"
)


# Verifica e remove duplicatas exatas.
duplicatas = int(df.duplicated().sum())

print(
    f"\nDuplicatas exatas encontradas: "
    f"{duplicatas:,}"
)

if duplicatas > 0:
    df_limpo = df.drop_duplicates().copy()

    print(
        f"Duplicatas removidas: "
        f"{duplicatas:,}"
    )
else:
    df_limpo = df.copy()

    print("Nenhuma duplicata foi removida.")


# Justificativa do tratamento de nulos.
# A verificação é realizada antes da decisão de remover ou imputar.
# Se não houver nulos, não há necessidade de utilizar fillna().
if total_nulos == 0:
    print(
        "\nTratamento de nulos: não foi necessária "
        "imputação nem remoção de registros por "
        "valores ausentes."
    )
else:
    print(
        "\nTratamento de nulos: os campos encontrados "
        "devem ser avaliados individualmente antes "
        "de uma imputação."
    )


# Gera a base limpa.
df_limpo.to_csv(
    ARQUIVO_SAIDA,
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

print(
    f"\nRegistros antes da limpeza: "
    f"{len(df):,}"
)

print(
    f"Registros após a limpeza: "
    f"{len(df_limpo):,}"
)

print(
    f"Arquivo gerado: "
    f"{ARQUIVO_SAIDA}"
)

# SPRINT 4 - ESTATÍSTICA DESCRITIVA


print("\n" + "=" * 75)
print("SPRINT 4 - ESTATÍSTICA DESCRITIVA")
print("=" * 75)

# CL_FHL representa o número de filhos do cliente.
filhos = pd.to_numeric(
    df_limpo["CL_FHL"],
    errors="coerce"
)

print(
    "\nEstatísticas da coluna CL_FHL "
    "- Número de filhos:"
)

print(f"Média: {filhos.mean():.4f}")
print(f"Mediana: {filhos.median():.4f}")
print(f"Desvio padrão: {filhos.std():.4f}")
print(f"Moda: {filhos.mode().iloc[0]:.4f}")
print(f"Máximo: {filhos.max():.4f}")
print(f"Mínimo: {filhos.min():.4f}")
print(f"Contagem: {filhos.count():,}")

# SPRINT 5 - AGRUPAMENTOS E RELATÓRIO

print("\n" + "=" * 75)
print("SPRINT 5 - AGRUPAMENTOS E RELATÓRIO")
print("=" * 75)


# Agrupamento 1: gênero.
# Mostra a quantidade de registros por gênero.
por_genero = (
    df_limpo
    .groupby("CL_GENERO")
    .size()
    .sort_values(ascending=False)
)

print(
    "\n1) Quantidade de registros/compras "
    "por gênero:"
)

print(por_genero)


# Agrupamento 2: categoria.
# Mostra a quantidade de registros por categoria.
por_categoria = (
    df_limpo
    .groupby("PR_CAT")
    .size()
    .sort_values(ascending=False)
)

print(
    "\n2) Quantidade de registros/compras "
    "por categoria:"
)

print(por_categoria)


# Agrupamento 3: mês.
# Permite observar a variação das compras ao longo do tempo.
por_mes = (
    df_limpo
    .groupby(df_limpo["DATA"].dt.to_period("M"))
    .size()
    .sort_values(ascending=False)
)

print(
    "\n3) Quantidade de registros/compras "
    "por mês:"
)

print(por_mes)

# CONCLUSÕES


print("\n" + "=" * 75)
print("CONCLUSÕES")
print("=" * 75)

print(
    f"1. O gênero com maior quantidade de "
    f"registros/compras foi {por_genero.index[0]}, "
    f"com {por_genero.iloc[0]:,} registros."
)

print(
    f"2. A categoria com maior quantidade de "
    f"registros/compras foi {por_categoria.index[0]}, "
    f"com {por_categoria.iloc[0]:,} registros."
)

print(
    f"3. O mês com maior quantidade de "
    f"registros/compras foi {por_mes.index[0]}, "
    f"com {por_mes.iloc[0]:,} registros."
)

print(
    f"4. Após a limpeza, a base passou de "
    f"{len(df):,} para {len(df_limpo):,} registros."
)

print(
    "5. A análise de nulos foi realizada antes "
    "do tratamento; não houve necessidade de "
    "imputação nas colunas úteis."
)

print(
    "6. A categoria '#N/D' permanece como possível "
    "inconsistência de classificação e pode ser "
    "revisada futuramente."
)


# Observação sobre os agrupamentos.
print("\nOBSERVAÇÃO:")

print(
    "A base não possui uma coluna explícita "
    "de valor/preço. Portanto, os agrupamentos "
    "representam quantidade de registros, "
    "e não faturamento em R$."
)

# SPRINT 6 - VERSIONAMENTO

print("\n" + "=" * 75)
print("SPRINT 6 - VERSIONAMENTO")
print("=" * 75)

print("Arquivos previstos para o repositório GitHub:")

print("- Miniprojeto_Varejo.py")
print("- Varejo.csv")
print("- df_limpo.csv")
print("- README.md")
print("- README_Helen_Ribeiro_QA_VDBI_2026_1_4.md")

print("\nAnálise concluída com sucesso!")