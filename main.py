from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df_funcion1 = pd.read_parquet('df_funcion1.parquet', engine='fastparquet', index=False)
df_funcion2 = pd.read_parquet('df_funcion2.parquet', engine='fastparquet', index=False)
df_recomendacion_csv = pd.read_csv('df_recomendacion.csv')
jaccard_csv=pd.read_csv('df_jaccard.csv', index_col='title')




@app.get('/PlayTimeGenre/{genero}')
def PlayTimeGenre(genero : str ):
    df_funcion1['genres'] = df_funcion1['genres'].astype(str)
    datos = df_funcion1[df_funcion1['genres'].str.contains(genero, case=False)].head(1)
    return {"Año de lanzamiento con mas horas jugadas para {} : {}".format(genero,datos.iloc[0,1])}

@app.get('/UserForGenre/{genero}')
def UserForGenre(genero : str ):
    df_funcion2['genres'] = df_funcion2['genres'].astype(str)
    datos = df_funcion2[df_funcion2['genres'].str.contains(genero, case=False)].head(1)
    return {"Usuario con más horas jugadas para {} : {}, Horas jugadas : {}".format(genero,datos.iloc[0,2],datos.iloc[0,3])}

@app.get('/recomendacion_juego/{titulo}')
def recomendacion_juego(titulo : str) -> list:
    juego = df_recomendacion_csv[df_recomendacion_csv['title'].str.lower().str.contains(titulo, case=False)]
    juego = juego.iloc[0,0]
    recomendaciones=jaccard_csv[juego].sort_values(ascending=False)
    recomendaciones = list(recomendaciones.index[1:6].tolist())    
    return recomendaciones

  
    



