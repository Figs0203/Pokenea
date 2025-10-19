# routes/pokenea.py

import random
import socket
from flask import Blueprint, render_template, jsonify
from models.pokeneas import POKENEAS

# Creamos un Blueprint para organizar nuestras rutas de manera modular.
pokenea_blueprint = Blueprint('pokenea', __name__)

def get_container_id():
    """
    Obtiene el hostname del contenedor, que Docker suele asignar como ID.
    """
    return socket.gethostname()

@pokenea_blueprint.route('/', methods=['GET'])
def mostrar_pokenea_aleatorio():
    """
    Ruta principal que muestra la imagen y la frase de un Pokenea aleatorio.
    También muestra el ID del contenedor que atiende la solicitud.
    """
    pokenea_aleatorio = random.choice(POKENEAS)
    container_id = get_container_id()
    
    # Pasamos los datos a la plantilla HTML para que los renderice.
    return render_template('pokenea.html', pokenea=pokenea_aleatorio, container_id=container_id)

@pokenea_blueprint.route('/api/pokenea', methods=['GET'])
def obtener_pokenea_json():
    """
    Ruta de API que devuelve los datos de un Pokenea aleatorio en formato JSON.
    Incluye el ID del contenedor.
    """
    pokenea_aleatorio = random.choice(POKENEAS)
    container_id = get_container_id()
    
    # Creamos el diccionario de respuesta con los campos solicitados.
    response_data = {
        "id": pokenea_aleatorio["id"],
        "nombre": pokenea_aleatorio["nombre"],
        "altura": pokenea_aleatorio["altura"],
        "habilidad": pokenea_aleatorio["habilidad"],
        "container_id": container_id
    }
    
    return jsonify(response_data)
