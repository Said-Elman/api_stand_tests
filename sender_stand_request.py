import configuration
import requests
import data

def post_new_user(user_body):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, # Concatenación de URL base y ruta.
                         json=user_body, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.








