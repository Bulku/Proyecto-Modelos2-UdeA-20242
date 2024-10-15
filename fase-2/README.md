En esta fase del proyecto se configura un contenedor de Docker con todas las librerías necesarias para correr el modelo.

El contenedor tiene dos scripts:

predict.py: que dado un conjunto de datos de entrada como un fichero csv, emita una predicción para cada dato de entrada, usando un modelo previamente almacenado en disco.

train.py: que dado un conjunto de entrenamiento (datos más etiquetas), entrene de nuevo el modelo y guarde una versión nueva del mismo.

## Construir la imagen en docker:
*Ejecutar el comando:*

docker build -t imagenlt .

# En Windows:
## Ejecutar train.py como volumen en docker:

docker run -v $PWD/resultados:/usr/src/app/resultados imagenlt python train.py --data_file /usr/src/app/resultados/train.csv --model_file /usr/src/app/resultados/modelo.pkl --overwrite_model

El contenedor está montando el volumen output en el directorio /usr/src/app/resultados, lo que asegura que cualquier archivo creado o modificado en esa ruta persista en tu sistema anfitrión.

## Ejecutar predict.py como volumen de docker:

docker run -v $PWD/resultados:/usr/src/app/resultados imagenlt python predict.py --input_file /usr/src/app/resultados/test.csv --model_file /usr/src/app/resultados/modelo.pkl --predictions_file /usr/src/app/resultados/ppredictions.csv

Cada vez que ejecutes los scripts train.py o predict.py, los resultados se almacenarán en ./resultados en tu sistema local.
