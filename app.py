from flask import Flask
from routes import register_routes
import os

app = Flask(__name__)

# Registra las rutas desde el archivo routes.py
register_routes(app)

if __name__ == '__main__':
    # Detecta el puerto del entorno (importante para Google Cloud Run)
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)