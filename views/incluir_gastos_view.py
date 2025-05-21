from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import controllers.gasto_controller as gasto
from datetime import datetime

mes_atual = datetime.now().strftime("%B").capitalize()

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

        # Label da tabela
        ttk.Label(self.frame, text="Gastos do mês atual:", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10, 5))

        # Frame para agrupar Treeview e Scrollbar
        tabela_frame = ttk.Frame(self.frame)
        tabela_frame.pack(fill="both", expand=True)

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(tabela_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        # Tabela (Treeview)
        self.tabela = ttk.Treeview(
            tabela_frame,
            columns=("data", "descricao", "categoria", "valor"),
            show="headings",
            height=6,
            yscrollcommand=scrollbar.set
        )

        # Configura Scrollbar
        scrollbar.config(command=self.tabela.yview)

        # Cabeçalhos
        self.tabela.heading("data", text="Data")
        self.tabela.heading("descricao", text="Descrição")
        self.tabela.heading("categoria", text="Categoria")
        self.tabela.heading("valor", text="Valor (R$)")

        # Largura das colunas
        self.tabela.column("data", width=90)
        self.tabela.column("descricao", width=150)
        self.tabela.column("categoria", width=100)
        self.tabela.column("valor", width=80)

        # Posiciona a tabela
        self.tabela.pack(side="left", fill="both", expand=True)
        self.label_total = ttk.Label(self.frame, text=f"Total dos Gastos de {mes_atual}: R$ 0.00", font=("Arial", 12, "bold"))
        self.label_total.pack(anchor="e", pady=(10, 0))

        # Preenche a tabela com dados do mês atual
        self.carregar_gastos_mes()

    def carregar_gastos_mes(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        mes_atual = datetime.now().strftime("%B").capitalize()
        gastos = gasto.buscar_gastos_por_mes(mes_atual)

        total = 0.0
        for g in gastos:
            data = g.get("data", "")[:10]  # Pegando só a data (AAAA-MM-DD)
            self.tabela.insert("", "end", values=(data, g["descricao"], g["categoria"], f"{g['valor']:.2f}"))
            total += float(g["valor"])

         # Atualiza a label total
        self.label_total.config(text=f"Total dos Gastos de {mes_atual}: R$ {total:.2f}")

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
            self.entry_valor.delete(0, tk.END)
            self.entry_descricao.delete(0, tk.END)
            self.valor_proposito.set("Selecione...")

            # Atualiza a tabela
            self.carregar_gastos_mes()
        else:
            messagebox.showerror("Erro", "Falha ao salvar o gasto.")

