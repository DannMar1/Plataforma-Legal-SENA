#======================================================
# Archivo app.py
# Proyecto: Legalis
# Descripción: Punto de entreda de la aplicación Flask.
#======================================================

from flask import Flask, render_template

# Inicialización de la aplicación
app = Flask(__name__)

@app.route('/') # Define una ruta web en Flask y la asocia a una función que atenderá las peticiones a esa URL.

def inicio():
    """Ruta principal del sistema Legalis.
    Temporalmente renderiza la plantilla base para auditar
    menú y footer antes de ingresar la tienda."""
    
    
    return render_template('base.html')

if __name__=='__main__':
# Arranque del servidor en modo desarrollo
    app.run(debug=True)