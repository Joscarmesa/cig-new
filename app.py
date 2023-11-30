from flask import Flask, render_template # importar librerias

app = Flask(__name__) #creando la instancia de la aplicacion

#definiendo ruta de inicio
@app.route('/')
def index():
    return render_template('index.html')

#iniciando aplicacion
if __name__ == '__main__': 
    app.run (debug=True)