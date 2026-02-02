from services.db import supabase
from datetime import datetime

def inserir_salario(valor):
    mes_atual = datetime.now().strftime("%B").capitalize()
    return supabase.table("salarios").insert({
        "valor_salario": valor,
        "mes_referencia": mes_atual
    }).execute()

def buscar_salario_atual():
    resposta = supabase.table("salarios") \
        .select("valor_salario") \
        .order("data_definicao", desc=True) \
        .limit(1) \
        .execute()

    if resposta.data:
        return float(resposta.data[0]["valor_salario"])
    return 0.0
