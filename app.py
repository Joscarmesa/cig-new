from flask import Flask
from routes import register_routes
from flask_sitemap import Sitemap
import os
import logging
from flask_wtf import CSRFProtect
from flask_mail import Mail
from flask_talisman import Talisman
from flask_wtf.csrf import generate_csrf
from werkzeug.middleware.proxy_fix import ProxyFix
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configuración de seguridad con Talisman
# Forzar HTTPS solo en producción
force_https = os.getenv("FLASK_ENV") == "production"  # Desactiva HTTPS forzado en desarrollo
Talisman(app, content_security_policy=None, force_https=force_https)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.secret_key = os.getenv('SECRET_KEY', os.urandom(24).hex())

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[logging.StreamHandler()]
)

# Inicializa CSRFProtect
csrf = CSRFProtect()
csrf.init_app(app)

# Inyecta el token CSRF en las plantillas
@app.context_processor
def inject_csrf_token():
    return dict(csrf_token=generate_csrf())

# Inicialización de Firestore
from firestore_config import get_firestore_client
try:
    db = get_firestore_client()
    logging.info("Firestore inicializado correctamente.")
except Exception as e:
    logging.error(f"Error al inicializar Firestore: {e}")
    raise

# Inicialización de Flask-Sitemap
ext = Sitemap(app)

# Configuración para proxy inverso
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)

# Registra rutas
register_routes(app, mail=Mail(app), db=db)

# Manejadores de errores
@app.errorhandler(404)
def not_found_error(error):
    return "Página no encontrada", 404

@app.errorhandler(500)
def internal_error(error):
    return "Error interno del servidor", 500

if __name__ == '__main__':
    # Detectar el puerto y configurar debug según el entorno
    port = int(os.getenv("PORT", 8080))
    debug_mode = os.getenv("FLASK_ENV") == "development"
    logging.info(f"Servidor iniciado en el puerto {port} (debug={debug_mode}).")
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
