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


