import os
import traceback

from services import evolution_api

def main():
    evo_client = evolution_api.EvolutionApi()

    try:
        sale = {'id': 1, 'valor': 1000}
        print(sale.id)
    except Exception as error:
        # enviar mensagem de erro para o WhatsApp
        message = f'Falha ao processar a venda: {error}\n\n{traceback.format_exc()}'
        evo_client.send_message(
            number=os.getenv('EVO_PHONE_LOGGER'),
            text=message
            )

if __name__ == '__main__':
    main()