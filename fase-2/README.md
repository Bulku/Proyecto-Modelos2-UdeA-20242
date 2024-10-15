En esta fase del proyecto es donde se configura el o los contenedores generados con Docker con todas las librerías necesarias para correr el modelo, de esta manera se busca asegurar que cualquier persona que siga estos pasos pueda generar y obtener las predicciones.

El contenedor tiene dos scripts:

predict.py: que dado un conjunto de datos de entrada como un fichero csv, emita una predicción para cada dato de entrada, usando un modelo previamente almacenado en disco.

train.py: que dado un conjunto de entrenamiento (datos más etiquetas), entrene de nuevo el modelo y guarde una versión nueva del mismo.

## Construir la imagen en docker:
*Ejecutar el comando:*

docker build -t imagenlt .
con este comando se construye dentro de docker el contenedor(containers) yo le sugiero el nombre "imagenlt" pero en realidad puedes poner el que gustes.
# En Windows:
## Ejecutar train.py como volumen en docker:

Con el fin de entrenar el modelo predictivo desde el docker se utilizan los siguientes comando los cuales estan recibiendo parametros para cumplir con las indicaciones de la segunda entrega, se ponen dos opciones debido a que no se si se ejecutan desde Linux o Windows.
este comando lo que hace es ejecutar el "train.py" para hacer el entrenamiento se crea el modelo que es un archivo .pkl.

para Linux docker run -v ${PWD}/resultados:/usr/src/app/resultados imagenlt python train.py --data_file /usr/src/app/resultados/train.csv --model_file /usr/src/app/resultados/modelo.pkl --overwrite_model

Para Windows docker run -v %CD%/resultados:/usr/src/app/resultados imagenlt python train.py --data_file /usr/src/app/resultados/train.csv --model_file /usr/src/app/resultados/modelo.pkl --overwrite_model

El contenedor está montando el volumen de salida se encuentra en el directorio /usr/src/app/resultados, lo que asegura que cualquier archivo creado o modificado en esa ruta persista en tu sistema, para que tenga la posibilidad de visualizar los cambios.

## Ejecutar predict.py como volumen de docker:

Este comando se usa para ejecutar el modelo predictivo con el anterior entrenamiento, y crea un archivo .csv el cual usted escoje el nombre que quiera para visualizarlos.

Para windows docker run -v %CD%/resultados:/usr/src/app/resultados imagenlt python predict.py --input_file /usr/src/app/resultados/test.csv --model_file /usr/src/app/resultados/modelo.pkl --predictions_file /usr/src/app/resultados/prediccioneslt.csv

Para Linux docker run -v ${PWD}/resultados:/usr/src/app/resultados imagenlt python predict.py --input_file /usr/src/app/resultados/test.csv --model_file /usr/src/app/resultados/modelo.pkl --predictions_file /usr/src/app/resultados/prediccioneslt.csv

Cada vez que ejecutes los scripts train.py o predict.py, los resultados se almacenarán en ./resultados en tu sistema local.
