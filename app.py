from flask import Flask
from routes import register_routes
from flask_sitemap import Sitemap
import os

# Inicialización de Flask-Sitemap
ext = Sitemap()

# Importando flask mail y variables de entorno
from flask_mail import Mail
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

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

# Registra las rutas desde el archivo routes.py
register_routes(app, mail)  # Pasamos `mail` para usarlo en las rutas

if __name__ == '__main__':
    # Detecta el puerto del entorno (importante para Google Cloud Run)
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
