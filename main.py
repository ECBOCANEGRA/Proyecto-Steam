from fastapi import FastAPI
import uvicorn
import pandas as pd

app = FastAPI()

df_funcion1 = pd.read_parquet('df_funcion1.parquet', engine='fastparquet', index=False)
df_funcion2 = pd.read_parquet('df_funcion2.parquet', engine='fastparquet', index=False)


@app.get('/Playtime')
def PlayTimeGenre(genero : str ):
    df_funcion1['genres'] = df_funcion1['genres'].astype(str)
    datos = df_funcion1[df_funcion1['genres'].str.contains(genero, case=False)].head(1)
    return "Año de lanzamiento con mas horas jugadas para {} : {}".format(genero,datos.iloc[0,1])

@app.get('/UserGenre')
def UserForGenre(genero : str ):
    df_funcion2 = pd.read_parquet('df_funcion2.parquet', engine='fastparquet', index=False)
    df_funcion2['genres'] = df_funcion2['genres'].astype(str)
    datos = df_funcion2[df_funcion2['genres'].str.contains(genero, case=False)].head(1)
    return "Usuario con más horas jugadas para {} : {}, Horas jugadas : {}".format(genero,datos.iloc[0,2],datos.iloc[0,3])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


