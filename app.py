from flask import Flask
from routes import register_routes

app = Flask(__name__)

# Registra las rutas desde el archivo routes.py
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)


# para implementacion en host

import os

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
