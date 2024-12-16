from flask import Flask
from routes import register_routes
from flask_sitemap import Sitemap
import os

# Importando firestore_config.py para newsletter
from firestore_config import get_firestore_client

# Inicialización de Flask-Sitemap
ext = Sitemap()

# Importando flask mail y variables de entorno
from flask_mail import Mail
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Cargado desde .env
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Cargado desde .env
app.secret_key = os.getenv('SECRET_KEY')  # Cargado desde .env

# Inicializa Flask-Mail
mail = Mail(app)

# Inicialización del cliente de Firestore
db = get_firestore_client()

# Registra las rutas desde el archivo routes.py
register_routes(app, mail, db)  # Pasamos `mail` y `db` para usarlos en las rutas

if __name__ == '__main__':
    # Detecta el puerto del entorno (importante para Google Cloud Run)
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
