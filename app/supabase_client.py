from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_usuarios():
    response = supabase.table("usuarios").select("nome, telefone").execute()
    return response.data
