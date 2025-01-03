from flask import Flask
from routes import register_routes
from flask_sitemap import Sitemap
import os
import logging

# Importar la configuración de Firestore
from firestore_config import get_firestore_client

# Inicialización de Flask-Sitemap
ext = Sitemap()

# Importando Flask-Mail y variables de entorno
from flask_mail import Mail
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar logging para producción
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Desde variables de entorno
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Desde variables de entorno
app.secret_key = os.getenv('SECRET_KEY')  # Cargado desde variables de entorno

# Verificación de configuración de Flask-Mail
if not app.config['MAIL_USERNAME'] or not app.config['MAIL_PASSWORD']:
    logging.error("Las credenciales de correo no están configuradas. Verifica tu archivo .env.")
    raise EnvironmentError("Faltan las variables de entorno MAIL_USERNAME y MAIL_PASSWORD.")

# Inicializa Flask-Mail
mail = Mail(app)

# Inicialización del cliente de Firestore
try:
    db = get_firestore_client()
    logging.info("Firestore inicializado correctamente.")
except Exception as e:
    logging.error(f"Error al inicializar Firestore: {e}")
    raise

# Registra las rutas desde el archivo routes.py
register_routes(app, mail, db)

if __name__ == '__main__':
    # Detecta el puerto del entorno (importante para Google Cloud Run)
    port = int(os.getenv("PORT", 8080))
    logging.info(f"Servidor iniciado en el puerto {port}.")
    app.run(host='0.0.0.0', port=port, debug=False)  # Asegúrate de que debug=False en producción
