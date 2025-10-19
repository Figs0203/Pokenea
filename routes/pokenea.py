# routes/pokenea.py

import random
import socket
from flask import Blueprint, render_template, jsonify, redirect, url_for, abort
from models.pokeneas import POKENEAS

# Creamos un Blueprint para organizar nuestras rutas de manera modular.
pokenea_blueprint = Blueprint('pokenea', __name__)

def get_container_id():
    """
    Obtiene el hostname del contenedor, que Docker suele asignar como ID.
    """
    return socket.gethostname()

@pokenea_blueprint.route('/')
def index():
    """
    Ruta raíz que redirige a un Pokenea aleatorio de la lista.
    """
    if POKENEAS:
        pokenea_aleatorio = random.choice(POKENEAS)
        return redirect(url_for('pokenea.mostrar_pokenea_por_id', pokenea_id=pokenea_aleatorio['id']))
    else:
        abort(404) # No hay Pokeneas que mostrar

@pokenea_blueprint.route('/pokenea/<int:pokenea_id>', methods=['GET'])
def mostrar_pokenea_por_id(pokenea_id):
    """
    Muestra un Pokenea específico basado en su ID.
    """
    # Buscar el pokenea por ID. `next` es más eficiente que un bucle for.
    pokenea_actual = next((p for p in POKENEAS if p['id'] == pokenea_id), None)

    if pokenea_actual is None:
        abort(404) # Pokenea no encontrado

    container_id = get_container_id()
    total_pokeneas = len(POKENEAS)
    
    # Pasamos los datos a la plantilla HTML para que los renderice.
    return render_template('pokenea.html', pokenea=pokenea_actual, container_id=container_id, total_pokeneas=total_pokeneas)

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
