import pandas as pd


reviews = pd.read_csv("books_of_the_decade.csv", index_col=0)


df = reviews.copy()

#print(reviews.set_index("Book Name")) "set index es usado para tomar la columba y ponera como de index o "titulo"
#mejores_Calificados = reviews.info() .info sirve para mostrar la informaion o tipo de dato en forma tabla
#reviews.astype({"Rating": "float"})
print("Valores únicos en Rating antes de la conversión:", df["Number of Votes"].unique())
#print(reviews.info())    .info() se utiliza para saber los datos, el tipo de dato y los datos nulos
df.loc[df["Rating"]== "really liked it\n4.00", "Rating"] = 4 #Encontramos el valor deseado y despues le cambiamos el valor 
df.loc[df["Rating"]== "it was amazing\n5.00", "Rating"] = 5
df.loc[df["Rating"]== "liked it\n3.00", "Rating"] = 3
#df["Rating"] = df["Rating"].astype(float) #Cambiamos el tipo de dato de la columna 'Rating'
df["Rating"] = pd.to_numeric(df["Rating"], errors='coerce') #coerence convierte los valores en NAN
df["Number of Votes"] = df["Number of Votes"].str.replace(",", "") #Sostutuye comas por espacios
df["Number of Votes"] = pd.to_numeric(df["Number of Votes"], errors='coerce')
#print(df[df["Number of Votes"].str.contains("rating")])  Esto lo hice para saber los que tenian la palabra "rating" dentro y saber cuantas personas los habian calificado

df.dropna(inplace=True)
print("Valores NaN en Rating después de la conversión:", df["Number of Votes"].isna().sum()) #verifica los valores NAN despues de haberlos
mejores_Calificados = df.loc[df.Rating >= 4.5]   #Obtenemos valores superiores a 4.5

#print(df[df.isna().any(axis=1)])   #Se usa para saber si es NA 

sorted_by_Votes = df.sort_values(by="Number of Votes", ascending=False)#Ordenar valores dentro de una columna "false" desendente, true asendente
print(f'Los Libros mas leidos del 2020 son: \n{sorted_by_Votes}')

sorted_by_Score = df.sort_values(by="Score", ascending=False)
print(f'Los datos ordenados por numero de Score quedan de la siguiente manera: \n{sorted_by_Score}')

sorted_by_Rating = df.sort_values(by="Rating", ascending=False)
print(sorted_by_Rating)
#print(df["Number of Votes"].sum())