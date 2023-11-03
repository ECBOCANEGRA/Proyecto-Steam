# Proyecto Individual

# MLOps
![](https://github.com/ECBOCANEGRA/Proyecto-Steam/blob/main/mlops.png)

# Contexto
Se planteó la necesidad de realizar el análisis y limpieza de datos de una base de datos de Steam, una plataforma multinacional de videojuegos. Así como crear un sistema de recomendaciones de videojuegos.

# Requerimientos 
Crear una api en Fastapi y deployarla en render para ser consumida

# Fujo de trabajo
![](https://github.com/ECBOCANEGRA/Proyecto-Steam/blob/main/DiagramaConceptualDelFlujoDeProcesos.png)

# Desarrollo del proyecto

Los principales archivos que se desarrollaron son:
* etl.ipynb
* EDA_final.ipynb
* funciones.ipynb
* recomendaciones.ipynb
* main.py

Las funciones que se crearon en la api son:
* def PlayTimeGenre( genero : str ): retorna año con mas horas jugadas para el género ingresado.

* def UserForGenre( genero : str ): retorna el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

Sistema de recomendación
* def recomendacion_juego( id de producto ): Ingresando el título del juego, recibimos una lista con 5 juegos recomendados similares al ingresado.


# Fuente de datos
[Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj): Carpeta con el archivo que requieren ser procesados, tengan en cuenta que hay datos que estan anidados (un diccionario o una lista como valores en la fila).

[Diccionario de datos](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit#gid=0): Diccionario con algunas descripciones de las columnas disponibles en el dataset.



