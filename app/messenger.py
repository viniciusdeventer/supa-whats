import requests
from app.config import ZAPI_INSTANCE, ZAPI_TOKEN

def enviar_mensagem(nome, telefone):
    mensagem = f"Olá {nome}, tudo bem com você?"
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}/send-text"

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print(f"Mensagem enviada para {nome}")
    else:
        print(f"Erro ao enviar para {nome}: {response.text}")
