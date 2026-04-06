#======================================================
# Archivo app.py
# Proyecto: Legalis
# Descripción: Punto de entreda de la aplicación Flask.
#======================================================

# Importa la clase Flask para crear la aplicación web y la función render_template para cargar y renderizar plantillas HTML con Jinja2.
# Permite inicializar la app y mostrar vistas HTML dinámicas dentro de las rutaas del proyecto.
from flask import Flask, render_template # type: ignore

# Crea la instancia principal de la aplicación Flask, usando el nombre del módulo para ubicar recursos y plantillas correctamente.
# Inicializa el servidor web y configura el contexto de la aplicación para manejar rutas, vistas y archivos estáticos. 
app = Flask(__name__)

# Define la ruta principal del sitio ("/") y la asocia a una función que atenderá las solicitudes HTTP de inicio.
# Indica que cuando un usuario accede a la URL raíz del proyecto, Flask ejecuta la función decorada para generar la respuesta correspondiente.
@app.route('/')

# Define la función controladora que gestiona la vista de inicio cuando se accede a la ruta principal del sitio.
# Actúa como controlador: recibe la petición del usuario desde la ruta / y  retorna la respuesta que se mostrará en el navegador.
def inicio():

    """Ruta principal del sistema Legalis.
        Temporalmente renderiza la plantilla base para auditar
        menú y footer antes de ingresar la tienda."""
    
    # Renderiza la plantilla index.html y la envía como respuesta al navegador para mostrar la página de inicio del sitio.
    # Carga el archivo HTML desde la carpeta templates, procesa sus bloques dinámicos con Jinja2 y devuelve la vista al cliente.
    return render_template('index.html')

# Verifica si el archivo se está ejecutando directamente (no importado como módulo) para iniciar la aplicación.
# Garantiza que el servidor Flask se ejecute únicamente cuando este archivo sea el programa principal, evitando que se inicie automáticamente si es importdo desde otro módulo.
if __name__=='__main__':

# Inicia el servidor de desarrollo de Flask en modo depuración para mostrar errores detallados y recargar automáticamente los cambios.
# Ejecuta la aplicación web localmente, permitiendo detectar fallos en tiempo real y actualizar sin reiniciar manualmente el servidor.
    app.run(debug=True)