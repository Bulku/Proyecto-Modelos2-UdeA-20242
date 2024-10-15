# Usar una imagen base de Python
FROM python:3.9-slim

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir numpy pandas scikit-learn loguru

# Crear el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copiar los scripts al directorio de trabajo
COPY train.py predict.py ./