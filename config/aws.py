# config/aws.py

import os
from dotenv import load_dotenv

def load_aws_config():
    """
    Carga las variables de entorno desde un archivo .env.
    Esto es ideal para el desarrollo local. En producción (Docker/AWS),
    las variables se inyectarán directamente en el entorno.
    """
    load_dotenv()

def get_s3_credentials():
    """
    Obtiene las credenciales de AWS y la configuración del bucket desde el entorno.
    """
    credentials = {
        "aws_access_key_id": os.getenv('AWS_ACCESS_KEY_ID'),
        "aws_secret_access_key": os.getenv('AWS_SECRET_ACCESS_KEY'),
        "s3_bucket_name": os.getenv('S3_BUCKET'),
        "aws_region": os.getenv('AWS_REGION', 'us-east-1') # Región por defecto si no se especifica
    }
    
    if not all(credentials.values()):
        print("Advertencia: Faltan una o más variables de entorno de AWS (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET).")
    
    return credentials

# Cargar la configuración al importar el módulo
load_aws_config()
