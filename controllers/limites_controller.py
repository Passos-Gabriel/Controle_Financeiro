import models.limite_model as limite_model

def listar_limites():
    return limite_model.listar_limite()

def adicionar_limite(valor):
    # Pode colocar validações aqui se quiser
    if valor <= 0:
        raise ValueError("Valor precisa ser maior que zero")

    return limite_model.inserir_limite(valor)

def buscar_valor_limite_atual():
    return limite_model.buscar_valor_mais_recente()

def obter_saldo_atual():
    return limite_model.calcular_saldo_atual()