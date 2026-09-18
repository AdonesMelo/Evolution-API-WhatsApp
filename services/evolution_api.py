import os
import requests
from dotenv import load_dotenv

load_dotenv()

class EvolutionApi:
    BASE_URL = os.getenv('EVO_BASE_URL')
    INSTANCE_NAME = os.getenv('EVO_INSTANCE_NAME')

    def __init__(self):
        self.__api_key = os.getenv('AUTHENTICATION_API_KEY')
        self.__headers = {
            'apikey': self.__api_key,
            'Content-Type': 'application/json'
        }

    def send_message(self, number, text):
        payload = {
            'number': number,
            'text': text,
            'delay': 10000, # simular "digitando"
        }

        response = requests.post(
            url=f'{self.BASE_URL}/message/sendText/{self.INSTANCE_NAME}',
            json=payload,
            headers=self.__headers,
        )

        return response.json()