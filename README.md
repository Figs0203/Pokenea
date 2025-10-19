# Pokedex Pokenea

Proyecto de una Pokedex para "Pokeneas" (criaturas ficticias de Antioquia) desarrollado en Flask y diseñado para ser desplegado en un clúster de Docker Swarm en AWS.

## Arquitectura

El proyecto sigue una arquitectura modular para separar responsabilidades:
- `app.py`: Punto de entrada de la aplicación.
- `models/`: Contiene la definición de los datos (el arreglo de Pokeneas).
- `routes/`: Define los endpoints de la API y las rutas web.
- `config/`: Maneja la configuración, especialmente las credenciales de AWS.
- `templates/`: Contiene las plantillas HTML.
- `Dockerfile`: Define la imagen de contenedor para la aplicación.

## Requisitos

- Python 3.9+
- Docker
- Cuenta de AWS con credenciales de acceso (Access Key y Secret Key).
- Un bucket de S3 con acceso público.

## Configuración Inicial

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO_DE_GITHUB>
    cd pokedex-pokenea
    ```

2.  **Configurar variables de entorno:**
    Crea un archivo llamado `.env` en la raíz del proyecto y añade tus credenciales de AWS y el nombre de tu bucket.

    ```
    AWS_ACCESS_KEY_ID=TU_ACCESS_KEY
    AWS_SECRET_ACCESS_KEY=TU_SECRET_KEY
    S3_BUCKET=nombre-de-tu-bucket
    AWS_REGION=tu-region-aws # ej: us-east-1
    ```

3.  **Actualizar URL del Bucket:**
    Abre el archivo `models/pokeneas.py` y reemplaza el placeholder `<TU_BUCKET_URL_AQUI>` por la URL pública de tu bucket de S3.

4.  **Subir imágenes a S3:**
    Sube las imágenes de tus Pokeneas al bucket de S3 y asegúrate de que tengan acceso público.

## Ejecución

### Ejecución Local (para pruebas)

1.  **Crear entorno virtual e instalar dependencias:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

2.  **Ejecutar la aplicación:**
    ```bash
    python app.py
    ```
    La aplicación estará disponible en `http://127.0.0.1:5000`.

### Ejecución con Docker (Método para despliegue)

1.  **Construir la imagen de Docker:**
    ```bash
    docker build -t tu-usuario-dockerhub/pokedex-pokenea:latest .
    ```

2.  **Ejecutar el contenedor:**
    Pasa las variables de entorno al contenedor al ejecutarlo.
    ```bash
    docker run --rm -p 5000:5000 \
      --env-file ./.env \
      tu-usuario-dockerhub/pokedex-pokenea:latest
    ```
    *Nota: El comando `--env-file ./.env` carga todas las variables desde tu archivo `.env` local, lo cual es más seguro y práctico.*

## Endpoints

-   `GET /`: Muestra una página HTML con la imagen y frase de un Pokenea aleatorio, junto con el ID del contenedor.
-   `GET /api/pokenea`: Devuelve un JSON con los datos (`id`, `nombre`, `altura`, `habilidad`) de un Pokenea aleatorio, junto con el ID del contenedor.
