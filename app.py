from flask import Flask

app=Flask(__name__)
@app.route('/')
def inicio():
    return "Bienvenido a la Plataforma Legal de Tutelas - Servidor Operativo"

if __name__=='__main__':
    app.run(debug=True)