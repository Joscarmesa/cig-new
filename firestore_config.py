import os
import json
from google.oauth2.service_account import Credentials
from google.cloud import firestore

def get_firestore_client():
    # Obtén las credenciales desde la variable de entorno
    credentials = os.getenv('FIRESTORE_CREDENTIALS')
    if not credentials:
        raise EnvironmentError("La variable FIRESTORE_CREDENTIALS no está configurada.")

    # Convierte las credenciales de JSON string a un diccionario
    credentials_dict = json.loads(credentials)

    # Usa las credenciales para inicializar Firestore
    firestore_credentials = Credentials.from_service_account_info(credentials_dict)
    return firestore.Client(credentials=firestore_credentials)



