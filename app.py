# =====================================================
# Archivo: app.py
# Proyecto: Legalis
# Descripción: Punto de entrada de la aplicación Flask.
# =====================================================

# Importa la clase Flask para crear la aplicación web y la función render_template para cargar y renderizar plantillas HTML con Jinja2.
# Permite inicializar la app y mostrar vistas HTML dinámicas dentro de las rutas del proyecto.
from flask import Flask, render_template # type: ignore

# Crea la instancia principal de la aplicación Flask, usando el nombre del módulo para ubicar recursos y plantillas correctamente.
# Inicializa el servidor web y configura el contexto de la aplicación para manejar rutas, vistas y archivos estáticos.
app = Flask(__name__)

# =====================================================
# RUTA: INICIO - INDEX
# =====================================================

# Define la ruta principal del sitio ("/") y la asocia a una función que atenderá las solicitudes HTTP de inicio.
# Indica que cuando un usuario accede a la URL raíz del proyecto, Flask ejecuta la función decorada para generar la respuesta correspondiente.
@app.route('/')

# Define la función controladora que gestiona la vista de inicio cuando se accede a la ruta principal del sitio.
# Actúa como controlador: recibe la petición del usuario desde la ruta / y retorna la respuesta que se mostrará en el navegador.
def inicio():

    """Ruta principal del sistema Legalis.
        Procesa y renderiza la plantilla index.html mediante Jinja2.
        Actúa como página de inicio (home) del sitio web Legalis y es la primera vista del usuario."""

    # Renderiza la plantilla index.html y la envía como respuesta al navegador para mostrar la página de inicio del sitio.
    # Carga el archivo HTML desde la carpeta templates, procesa sus bloques dinámicos con Jinja2 y devuelve la vista al cliente.
    return render_template('index.html')

# Verifica si el archivo se está ejecutando directamente (no importado como módulo) para iniciar la aplicación.
# Garantiza que el servidor Flask se ejecute únicamente cuando este archivo sea el programa principal, evitando que se inicie automáticamente si es importado desde otro módulo.

# =====================================================
# RUTA: PREGUNTAS FRECUENTES
# =====================================================

# Elemento: Decorador de ruta de Flask (@app.route).
# Comentario Técnico: Registra un punto de acceso (endpoint) en la aplicación para la URL específica '/preguntas'.
# Función Técnica: Mapea la dirección que el usuario escribe en su navegador hacia una función lógica en el backend.
# DICCIONARIO: Decorador de Ruta | Es el "GPS" del servidor | La ruta debe coincidir exactamente con el atributo 'href' de tus enlaces en el HTML.
@app.route('/preguntas')

# Elemento: Definición de función de Python (View Function).
# Comentario Técnico: Declara el bloque de código encargado de procesar la solicitud cuando se accede a la ruta definida.
# Función Técnica: Actúa como el controlador que orquestará la respuesta que se le entregará al cliente.
# DICCIONARIO: Función de Vista | Es el motor lógico de la página | Se recomienda que el nombre de la función sea igual al nombre de la ruta para mayor claridad.
def preguntas():

    # Elemento: Sentencia de retorno con función de renderizado de plantillas.
    # Comentario Técnico: Invoca el motor Jinja2 para procesar y enviar el archivo HTML 'preguntas.html' al navegador.
    # Función Técnica: Conecta la lógica del servidor con la interfaz visual (frontend) para mostrar la página final al usuario.
    # DICCIONARIO: Renderizador | Transforma código estático en páginas dinámicas | El archivo mencionado DEBE existir dentro de la carpeta 'templates' del proyecto.
    return render_template('preguntas.html')

# =====================================================
# RUTA: QUIENES SOMOS (IDENTIDAD INSTITUCIONAL)
# =====================================================

# Elemento: Decorador de ruta en Flask.
# Comentario Técnico: Asocia la URL "/nosotros" con la función que se define inmediatamente después.
# Función Técnica: Permite que cuando un usuario escriba /nosotros en el navegador, el servidor ejecute una función específica.
# DICCIONARIO: @app.route | Decorador que registra una dirección web (URL) en la aplicación Flask | Siempre se coloca encima de la función que atenderá esa ruta.
@app.route('/nosotros')

# Elemento: Definición de función en Python.
# Comentario Técnico: Declara la función llamada "nosotros" que será ejecutada cuando el usuario visite la ruta asociada.
# Función Técnica: Contiene laa lógica que generará la respuesta del servidor para la página "Nosotros".
# DICCIONARIO: Función | Bloque de código reutilizable que se ejecuta cuando es llamado | En Flask representa una vista (view function).
def nosotros() :

    # Elemento: Función render_template de Flask.
    # Comentario Técnico: Carga el archivo "nosotros.html" desde la carpeta templates y lo envía al naveegador del usuario.
    # Función Técnica: Genera la página web que verá el visitante al entrar a la sección Nosotros.
    # DICCIONARIO: render_template | Función de Flask que convierte un archivo HTML en respuesta web | Permite mostrar páginas dinámicas.
    return render_template('nosotros.html')

# Elemento: Condicional de ejecución principal (Boilerplate).
# Comentario Técnico: Evalúa la variable especial '__name__' para determinar si el script se está ejecutando como el programa principal o si está siendo importado como un módulo.
# Función Técnica: Actúa como el interruptor de seguridad que autoriza el encendido del servidor Flask.
# DICCIONARIO: Punto de Entrada | Protege el código de ejecuciones accidentales en otros archivos | Es una convención obligatoria para scripts profesionales en Python.
if __name__ == '__main__':

    # Elemento: Método de ejecución de la instancia de la aplicación Flask.
    # Comentario Técnico: Inicia el servidor web de desarrollo local en la dirección predeterminada (usualmente localhost:5000) con el modo de depuración activo.
    # Función Técnica: Pone al sistema en estado de "escucha" para recibir peticiones y reinicia el servidor automáticamente cada vez que guardas un cambio.
    # DICCIONARIO: Arrancador de Aplicación | Permite probar la web en tiempo real y ver errores detallados en el navegador | El modo 'debug=True' debe ser desactivado estrictamente antes de desplegar la web a un servidor de producción.
    app.run(debug=True)