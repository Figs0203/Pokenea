# app.py

from flask import Flask
from routes.pokenea import pokenea_blueprint
from config.aws import load_aws_config

# Cargar configuración de AWS al inicio (opcional, pero buena práctica)
load_aws_config()

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Registrar el blueprint que contiene las rutas de los Pokeneas
app.register_blueprint(pokenea_blueprint)

if __name__ == '__main__':
    # El host '0.0.0.0' es crucial para que la app sea accesible
    # desde fuera del contenedor Docker.
    app.run(host='0.0.0.0', port=5000, debug=True)
