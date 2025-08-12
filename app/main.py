from app.supabase_client import get_usuarios
from app.messenger import enviar_mensagem

def main():
    usuarios = get_usuarios()
    for usuario in usuarios:
        nome = usuario["nome"]
        telefone = usuario["telefone"]
        if nome and telefone:
            enviar_mensagem(nome, telefone)

if __name__ == "__main__":
    main()
