import models.gasto_model as gasto_model

def listar_gastos():
    return gasto_model.listar_gastos()

def adicionar_gasto(valor, descricao, categoria):
    # Pode colocar validações aqui se quiser
    if valor <= 0:
        raise ValueError("Valor precisa ser maior que zero")
    if not descricao or not categoria:
        raise ValueError("Descrição e categoria são obrigatórias")
    return gasto_model.inserir_gasto(valor, descricao, categoria)

def buscar_gastos_por_mes(mes):
    return gasto_model.buscar_por_mes(mes)