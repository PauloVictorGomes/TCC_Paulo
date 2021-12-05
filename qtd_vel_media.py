import pandas as pd


pd.set_option('display.max_rows', 30)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


#Importando dados
df1 = pd.read_csv('01-11-2021_tratado.csv')  # ,error_bad_lines=False, low_memory=False, verificar colunas uteis
df2 = pd.read_csv('02-11-2021_tratado.csv')
df3 = pd.read_csv('03-11-2021_tratado.csv')
df4 = pd.read_csv('04-11-2021_tratado.csv')
df5 = pd.read_csv('05-11-2021_tratado.csv')
df6 = pd.read_csv('06-11-2021_tratado.csv')
df7 = pd.read_csv('07-11-2021_tratado.csv')

#print(df.head(5))
print("\n")

#print(df['LINHA'].unique().count)
print('\nDados sobre a Ônibus referente a cada dia:\n')

df1_qtd_bus = df1['ORDEM']
df1_qtd_bus = df1['ORDEM']
df2_qtd_bus = df2['ORDEM']
df3_qtd_bus = df3['ORDEM']
df4_qtd_bus = df4['ORDEM']
df5_qtd_bus = df5['ORDEM']
df6_qtd_bus = df6['ORDEM']
df7_qtd_bus = df7['ORDEM']


print(f"Quantidade de onibus no dia 01/11: {df1_qtd_bus.nunique()}")
print(f"Quantidade de onibus no dia 02/11: {df2_qtd_bus.nunique()}")
print(f"Quantidade de onibus no dia 03/11: {df3_qtd_bus.nunique()}")
print(f"Quantidade de onibus no dia 04/11: {df4_qtd_bus.nunique()}")
print(f"Quantidade de onibus no dia 05/11: {df5_qtd_bus.nunique()}")
print(f"Quantidade de onibus no dia 06/11: {df6_qtd_bus.nunique()}")
print(f"Quantidade de onibus no dia 07/11: {df7_qtd_bus.nunique()}")

onibus_list = [df1_qtd_bus.nunique(), df2_qtd_bus.nunique(), df3_qtd_bus.nunique(), df4_qtd_bus.nunique(),
               df5_qtd_bus.nunique(), df6_qtd_bus.nunique(), df7_qtd_bus.nunique()]

print(onibus_list)

df_media_bus



#print(df1_qtd_bus)



