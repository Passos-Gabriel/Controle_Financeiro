import models.salario_model as salario_model
from datetime import datetime
from services.db import supabase
import controllers.salario_controller as salario
import controllers.gasto_controller as gasto

def salvar_salario(valor):
    if valor <= 0:
        raise ValueError("Salário deve ser maior que zero")
    return salario_model.inserir_salario(valor)

def obter_salario_atual():
    return salario_model.buscar_salario_atual()


def calcular_saldo_salario_mes():
    salario_atual = salario.obter_salario_atual()

    mes_atual = datetime.now().strftime("%B").capitalize()
    gastos = gasto.buscar_gastos_por_mes(mes_atual)

    total_gastos = sum(float(g["valor"]) for g in gastos)

    return round(salario_atual - total_gastos, 2)
