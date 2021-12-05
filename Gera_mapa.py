import pandas as pd
import folium
pd.set_option('display.max_rows', 30)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


df = pd.read_csv('01-11-2021_tratado.csv')  # ,error_bad_lines=False, low_memory=False, verificar colunas uteis
print(df.head(5))
print("\n")

index = df.index
number_of_rows = len(index)
print(number_of_rows)

#input("teste")

# Getting data for 1 June 2017
print("-- Dados do dia x de x de 2021 --")
df = df[df['DATAHORA'].str.split(' ').apply(lambda x:x[0] == '11-01-2021')]
print(df.shape)
print(df)
print("\n")


print("-- Atribuindo somente os dados relevantes --")
df=df[['DATAHORA','LINHA','LATITUDE','LONGITUDE']]
print(df.head())
print("\n")

print("-- True: linhas duplicadas --")
print(df.duplicated().value_counts())
print("\n")

print("-- Apagando linhs duplicadas --")
df=df.drop_duplicates()
print("\n")

print("-- Verificando valor nulo --")
print(df.isnull().sum())
print("\n")



print("-- Convertendo coluna para DATETIME  --")
df['DATAHORA']=pd.to_datetime((df['DATAHORA']))
df['DATAHORA']=pd.to_datetime(df['DATAHORA'],format='%Y-%m-%d %H:%M:%S')
print("\n")
print(df.info())
print(df.head())
print("\n")


## Creating hour column
df['HORA']=df['DATAHORA'].apply(lambda x: x.hour)
print(df.head())
print("\n")

# Encontrar o último tempo registrado para cada ônibus em uma hora
df2=pd.DataFrame(df.groupby(['HORA','LINHA'])['DATAHORA'].max())
df2.reset_index(inplace=True)
print(df2.head())
print("\n")

# Encontrar a localização dos ônibus, unindo DF's
df3=pd.merge(df2,df,left_on=['HORA','LINHA','DATAHORA'],right_on=['HORA','LINHA','DATAHORA'])
print(df3)
#input("teste")
#converter a posição dos ônibus
lat_long_list = []
for i in range(0,24):
    temp=[]
    for index, instance in df3[df3['HORA'] == i].iterrows():
        temp.append([instance['LATITUDE'],instance['LONGITUDE']])
    lat_long_list.append(temp)


#Visualizando o tráfego do barramento por meio do plug-in HeatMapWithTime

from folium.plugins import HeatMapWithTime

fig7=folium.Figure(width=850,height=550)

m7=folium.Map(location=[-22.9035, -43.2096],tiles='cartodbpositron',zoom_start=10)
fig7.add_child(m7)


HeatMapWithTime(lat_long_list,radius=6,auto_play=True,position='bottomright').add_to(m7)


m7.save('01-11-2021.html')

print(lat_long_list)

