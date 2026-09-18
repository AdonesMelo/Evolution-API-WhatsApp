import requests
import os
from dotenv import load_dotenv

load_dotenv()


BASE_URL = os.getenv('EVO_BASE_URL') # url do Evolution
INSTANCE_NAME = os.getenv('EVO_INSTANCE_NAME') # nome da instância do Evolution
EVOLUTION_AUTHENTICATION_API_KEY = os.getenv('AUTHENTICATION_API_KEY') # autenticação do Evolution

headers = {
    'apikey': EVOLUTION_AUTHENTICATION_API_KEY,
    'Content-Type': 'application/json'
}
payload = {
    'number': os.getenv('EVO_PHONE_LOGGER'), # número do WhatsApp
    'text': 'Olá, deu certo!',
    'delay': 10000, # simular "digitando"
}
response = requests.post(
    url=f'{BASE_URL}/message/sendText/{INSTANCE_NAME}',
    json=payload,
    headers=headers,
)
print(response.json())
