import pandas as pd

pd.set_option('display.max_rows', 30)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


#Importando dados
df = pd.read_csv('07-11-2021.csv',low_memory=False)  # ,error_bad_lines=False, low_memory=False, verificar colunas uteis
print(df.head(5))
print("\n")

print("Eliminando coluna gerada devido aos indices do csv...")
df = df.drop('Unnamed: 0', axis=1)

print("Eliminando linhas duplicados e NaN...\n")
#df.duplicated().value_counts()
df = df.drop_duplicates()
df = df.dropna()

print(df.head(10))
print(df.info())

print(df.describe())

#Devido ao merge csv's temos cabeçalhos como linhas
# Obtendo os nomes dos índices para os quais a coluna DATAHORA tem o valor DATAHORA
indexNames = df[df['DATAHORA'] == 'DATAHORA'].index

# Excluindo os índices dessas linha do dataFrame
df = df.drop(indexNames)
print(df.head(10))


#Ajustando os tipos das nossas variáveis

colunas_string = ['ORDEM']
colunas_flutuantes = ['LATITUDE','LONGITUDE','VELOCIDADE']

def muda_tipo(DataFrame, colunas, tipo):
    for coluna in colunas:
        DataFrame[coluna] = DataFrame[coluna].astype(tipo)


muda_tipo(df, colunas_flutuantes, 'float')
muda_tipo(df, colunas_string, 'string')

print("\n")
print(df.info())
print("\n")
print(df.head(10))


#df.to_csv('07-11-2021_tratado_teste.csv')



