import os
from google.cloud import secretmanager
from google.oauth2.service_account import Credentials
from google.cloud import firestore

def get_firestore_credentials_from_secret():
    """
    Recupera las credenciales JSON de Firestore desde Google Cloud Secret Manager.
    """
    # Project ID y nombre del secreto
    project_id = "speedy-aurora-439004-d2"  # Reemplazado con tu Project ID
    secret_name = f"projects/{project_id}/secrets/FIRESTORE_CREDENTIALS/versions/latest"

    try:
        # Cliente de Secret Manager
        client = secretmanager.SecretManagerServiceClient()
        
        # Acceder al secreto
        response = client.access_secret_version(name=secret_name)
        credentials_json = response.payload.data.decode('UTF-8')
        return credentials_json
    except Exception as e:
        raise RuntimeError(f"Error al acceder al secreto en Secret Manager: {e}")

def get_firestore_client():
    """
    Inicializa y devuelve el cliente de Firestore usando las credenciales desde Secret Manager.
    """
    # Obtener credenciales desde Secret Manager
    credentials_json = get_firestore_credentials_from_secret()

    try:
        # Convertir JSON a credenciales y crear el cliente de Firestore
        firestore_credentials = Credentials.from_service_account_info(eval(credentials_json))
        return firestore.Client(credentials=firestore_credentials)
    except Exception as e:
        raise RuntimeError(f"Error al inicializar Firestore: {e}")

# Prueba de conexión
if __name__ == "__main__":
    try:
        db = get_firestore_client()
        print("Firestore inicializado correctamente.")
    except Exception as e:
        print(f"Error al inicializar Firestore: {e}")
