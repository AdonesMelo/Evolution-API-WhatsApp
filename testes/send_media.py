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
    'mediatype': 'image',
    'mimetype': 'image/jpeg',
    'caption': 'Python',
    'media': 'https://images.icon-icons.com/2699/PNG/512/python_logo_icon_168886.png',
    'fileName': 'python.jpeg',
    # 'delay': 10000, # simular "digitando"
}

response = requests.post(
    url=f'{BASE_URL}/message/sendMedia/{INSTANCE_NAME}',
    json=payload,
    headers=headers,
)

print(response.json())
