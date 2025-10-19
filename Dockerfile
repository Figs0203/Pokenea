# 1. Usar una imagen base oficial de Python ligera
FROM python:3.9-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de requerimientos e instalar dependencias
# Se copia primero para aprovechar el cache de Docker si no cambia
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el resto del código de la aplicación
COPY . .

# 5. Exponer el puerto en el que se ejecutará la aplicación Flask
EXPOSE 5000

# 6. Comando para ejecutar la aplicación cuando se inicie el contenedor
# Se usa gunicorn en producción, pero para este caso `python app.py` es suficiente.
CMD ["python", "app.py"]
