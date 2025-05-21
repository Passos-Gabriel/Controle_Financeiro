from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import controllers.gasto_controller as gasto

class IncluirGastosView:
    def __init__(self, root, voltar_callback):
        self.root = root
        self.voltar_callback = voltar_callback

        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(fill="both", expand=True)

        # Botão voltar
        self.btn_voltar = ttk.Button(self.frame, text="⬅ Home", command=self.voltar_callback)
        self.btn_voltar.pack(anchor="w")

        # Título
        titulo = ttk.Label(self.frame, text="Adicionar Gasto", font=("Arial", 16, "bold"))
        titulo.pack(pady=(10, 20))

        # Campo: Valor Gasto
        lbl_valor = ttk.Label(self.frame, text="Valor Gasto:")
        lbl_valor.pack(anchor="w")
        self.entry_valor = ttk.Entry(self.frame)
        self.entry_valor.pack(fill="x", pady=(0, 10))

        # Campo: Descrição
        lbl_descricao = ttk.Label(self.frame, text="Descrição:")
        lbl_descricao.pack(anchor="w")
        self.entry_descricao = ttk.Entry(self.frame)
        self.entry_descricao.pack(fill="x", pady=(0, 10))

        # Campo: Propósito
        lbl_proposito = ttk.Label(self.frame, text="Propósito:")
        lbl_proposito.pack(anchor="w")
        opcoes = ["Lazer", "Estudo", "Despesas Fixas", "Outros"]
        self.valor_proposito = tk.StringVar()
        self.valor_proposito.set("")  # vazio por padrão
        dropdown = ttk.OptionMenu(self.frame, self.valor_proposito, "Selecione...", *opcoes)
        dropdown.pack(fill="x", pady=(0, 20))

        # Botão de salvar
        btn_salvar = ttk.Button(self.frame, text="Salvar Gasto", command=self.salvar_gasto)
        btn_salvar.pack()

    def salvar_gasto(self):
        descricao = self.entry_descricao.get().strip()
        categoria = self.valor_proposito.get().strip()

        # Valida número
        try:
            valor = float(self.entry_valor.get())
        except ValueError:
            messagebox.showerror("Erro", "O campo 'Valor Gasto' deve ser um número válido.")
            return
        
        # Verifica campos obrigatórios
        if not valor or not descricao or categoria == "Selecione..." or not categoria:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return

        # Se tudo ok, prossegue
        resultado = gasto.adicionar_gasto(valor, descricao, categoria)


        if resultado.data:  # Se há dados, a inserção foi bem-sucedida
            messagebox.showinfo("Sucesso", "Gasto salvo com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao salvar o gasto.")

