import pandas as pd

#Importando dados
df1 = pd.read_csv('01-11-2021_tratado.csv', index_col=0)

#df1['ORDEM'] = df1['ORDEM'].astype('str')

df_teste = df1.loc[df1['ORDEM']=='D86315']

#df_teste1 = df1.

#print(df1['ORDEM'])
print(df_teste.head())
#print(df_teste1.head())
