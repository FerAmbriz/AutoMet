import pandas as pd
import sys

Output=sys.argv[1]

print ('#----------------Construct Autoncoprint-------------------#')
merge_filtrado = pd.read_csv(Output+'/FiltradoMergue.csv')

merge_filtrado=merge_filtrado.drop(['Chr', 'End',  'Cyt_Met', 'Cyt_NoMet'], axis=1)

df=merge_filtrado.pivot(index=['Start','Gen'], columns='Sample')

# Eliminar el multindice de las columnas
df = df.droplevel(level=0, axis=1)

df.to_csv(Output+'/Autoncoprint.csv')

#Remplazar los valores numericos por 0
df = df.fillna(0)


df.to_csv(Output+'/AutoncoprintRellenado.csv')


print ('''

Output: 
	Output/Autoncoprint.csv
	Output/AutoncoprintRellenado.csv

''')

print ('#----------------- Done Autoncoprint--------------------#')

#-----------------------------------------------------------------------

print('')
print('#------------Init Construct Autoncoprint Promedio -----------#')

# Eliminar el multindice
df = df.droplevel(level=0)
# Eliminar los indices
df_reset=df.reset_index()

# Determinar los genes a graficar
gen = pd.DataFrame(df_reset['Gen'].value_counts())
gen = gen.index

# Construcción de un df con las columnas anteriores
df_bd = pd.DataFrame(columns = df.columns)
for i in range(len(gen)):
	# Filtrar el df por gen
	df_reset_i = df_reset[df_reset['Gen'] == gen[i] ]
	# Calcular la media por paciente de cada gen
	x= df_reset_i.mean()
	list = x.tolist()
	# Agregar fila por fila correspondiente a cada gen de todas las muestras
	df_bd.loc[i]=list

# Insertat la columna de genes
df_bd.insert(0, 'Gen', gen)

df_bd.to_csv(Output+'/AutoncoprintPromedio.csv')

print ('')
print('Output: AutoncoprintPromedio.csv')
print('')

print('#----------------Done--------------------#')
