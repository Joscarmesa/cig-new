# Utiliza una imagen base oficial de Python (puedes cambiar la versión si es necesario)
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia todos los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias listadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la aplicación estará escuchando (8080 suele ser el estándar para Google Cloud Run)
EXPOSE 8080

# Comando para ejecutar la aplicación usando Gunicorn, una opción robusta para servidores web
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
