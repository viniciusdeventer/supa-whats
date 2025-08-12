import requests
from app.config import ZAPI_INSTANCE, ZAPI_TOKEN, CLIENT_TOKEN

def enviar_mensagem(nome, telefone):
    mensagem = f"Olá {nome}, tudo bem com você?"
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}/send-text"

    headers = {
        "Client-Token": CLIENT_TOKEN,
        "Content-Type": "application/json"
    }

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Mensagens enviadas com sucesso!")
    else:
        print(f"Erro ao enviar mensagem para {nome}: {response.text}")
