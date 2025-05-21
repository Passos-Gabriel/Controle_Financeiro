import controllers.gasto_controller as gasto
novo_gasto = {
    "valor": 150.75,
    "descricao": "Compra de livro",
    "categoria": "Estudo",
    "data": "2025-05-20"
}


print("Inserção:", gasto.adicionar_gasto(novo_gasto["valor"],novo_gasto["descricao"],novo_gasto["categoria"]))