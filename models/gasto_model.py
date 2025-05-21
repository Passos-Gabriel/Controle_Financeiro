from services.db import supabase
from datetime import datetime


def listar_gastos():
    response = supabase.table("gastos").select("*").execute()
    return response.data

def inserir_gasto(valor, descricao, categoria):
    mes_atual = datetime.now().strftime("%B").capitalize()  # Exemplo: "Maio"
    return supabase.table("gastos").insert({
        "valor": valor,
        "descricao": descricao,
        "categoria": categoria,
        "mes_referencia": mes_atual  # <- garante que está enviando o mês
    }).execute()

def deletar_gasto(gasto_id):
    response = supabase.table("gastos").delete().eq("id", gasto_id).execute()
    return response.data

# Outros métodos que precisar, tipo atualizar, buscar por id, etc.
