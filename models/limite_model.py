from services.db import supabase
from datetime import datetime

def listar_limite():
    response = supabase.table("limites").select("*").execute()
    return response.data

def inserir_limite(valor):
    mes_atual = datetime.now().strftime("%B").capitalize()  # Exemplo: "Maio"
    return supabase.table("limites").insert({
        "valor_limite": valor,
        "mes_referencia": mes_atual  # <- garante que está enviando o mês
    }).execute()

def deletar_limite(limite_id):
    response = supabase.table("limites").delete().eq("id", limite_id).execute()
    return response.data

def buscar_valor_mais_recente():
    resposta = supabase.table("limites") \
        .select("valor_limite") \
        .order("data_definicao", desc=True) \
        .limit(1) \
        .execute()
    
    if resposta.data and len(resposta.data) > 0:
        return resposta.data[0]["valor_limite"]
    return None

def calcular_saldo_atual():
    # 1. Busca o limite mais recente
    limite_resp = supabase.table("limites")\
        .select("*")\
        .order("data_definicao", desc=True)\
        .limit(1)\
        .execute()

    if not limite_resp.data:
        return 0.0  # Sem limite definido

    limite = float(limite_resp.data[0]["valor_limite"])

    # 2. Busca gastos do mês atual
    mes_atual = datetime.now().strftime("%B").capitalize()
    gastos_resp = supabase.table("gastos")\
        .select("valor")\
        .eq("mes_referencia", mes_atual)\
        .execute()

    total_gastos = sum(float(gasto["valor"]) for gasto in gastos_resp.data)

    # 3. Calcula saldo
    saldo_atual = limite - total_gastos
    return round(saldo_atual, 2)
# Outros métodos que precisar, tipo atualizar, buscar por id, etc.