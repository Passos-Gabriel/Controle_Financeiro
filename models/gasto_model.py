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

def buscar_por_mes(mes):
    resposta = supabase.table("gastos").select("*").eq("mes_referencia", mes).order("id", desc=True).execute()
    return resposta.data if resposta.data else []

# Outros métodos que precisar, tipo atualizar, buscar por id, etc.
def atualizar_gasto(gasto_id, valor, descricao, categoria):
    mes_atual = datetime.now().strftime("%B").capitalize()
    return supabase.table("gastos").update({
        "valor": valor,
        "descricao": descricao,
        "categoria": categoria,
        "mes_referencia": mes_atual
    }).eq("id", gasto_id).execute()