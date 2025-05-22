from tkinter import ttk
import tkinter as tk
from datetime import datetime
import controllers.gasto_controller as gasto_controller

class RelatorioGastosView:
    def __init__(self, root, voltar_callback):
        self.root = root
        self.voltar_callback = voltar_callback

        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(fill="both", expand=True)

        self.btn_voltar = ttk.Button(self.frame, text="⬅ Home", command=self.voltar_callback)
        self.btn_voltar.pack(anchor="w")

        titulo = ttk.Label(self.frame, text="Relatório de Gastos", font=("Arial", 16, "bold"))
        titulo.pack(pady=(10, 10))

        # Filtros
        filtros_frame = ttk.Frame(self.frame)
        filtros_frame.pack(fill="x", pady=(0, 10))

        # Filtro por mês
        ttk.Label(filtros_frame, text="Mês:").grid(row=0, column=0, padx=5)
        self.mes_var = tk.StringVar()
        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        mes_atual = datetime.now().strftime("%B").capitalize()
        self.mes_var.set(mes_atual)
        self.dropdown_mes = ttk.OptionMenu(filtros_frame, self.mes_var, mes_atual, *meses)
        self.dropdown_mes.grid(row=0, column=1)

        # Filtro por categoria
        ttk.Label(filtros_frame, text="Categoria:").grid(row=0, column=2, padx=5)
        self.categoria_var = tk.StringVar()
        categorias = ["Todas", "Lazer", "Estudo", "Despesas Fixas", "Outros"]
        self.categoria_var.set("Todas")
        self.dropdown_categoria = ttk.OptionMenu(filtros_frame, self.categoria_var, "Todas", *categorias)
        self.dropdown_categoria.grid(row=0, column=3)

        # Intervalo de datas
        ttk.Label(filtros_frame, text="De (AAAA-MM-DD):").grid(row=1, column=0, padx=5, pady=(10, 0))
        self.data_inicio_var = tk.StringVar()
        ttk.Entry(filtros_frame, textvariable=self.data_inicio_var).grid(row=1, column=1, pady=(10, 0))

        ttk.Label(filtros_frame, text="Até (AAAA-MM-DD):").grid(row=1, column=2, padx=5, pady=(10, 0))
        self.data_fim_var = tk.StringVar()
        ttk.Entry(filtros_frame, textvariable=self.data_fim_var).grid(row=1, column=3, pady=(10, 0))

        # Botão Filtrar
        btn_filtrar = ttk.Button(filtros_frame, text="Filtrar", command=self.filtrar_gastos)
        btn_filtrar.grid(row=1, column=4, padx=10, pady=(10, 0))

        # Tabela com scrollbar
        self.tabela_frame = ttk.Frame(self.frame)
        self.tabela_frame.pack(fill="both", expand=True)

        # Scrollbar vertical
        self.scrollbar = ttk.Scrollbar(self.tabela_frame, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        # Treeview
        self.tabela = ttk.Treeview(
            self.tabela_frame,
            columns=("descricao", "categoria", "valor", "data"),
            show="headings",
            yscrollcommand=self.scrollbar.set
        )
        self.tabela.pack(fill="both", expand=True)

        # Link scrollbar à Treeview
        self.scrollbar.config(command=self.tabela.yview)

        self.tabela.heading("descricao", text="Descrição")
        self.tabela.heading("categoria", text="Categoria")
        self.tabela.heading("valor", text="Valor (R$)")
        self.tabela.heading("data", text="Data")

        self.tabela.column("descricao", width=150)
        self.tabela.column("categoria", width=100)
        self.tabela.column("valor", width=80)
        self.tabela.column("data", width=100)

        # Total
        self.total_label = ttk.Label(self.frame, text="Total: R$ 0.00", font=("Arial", 12, "bold"))
        self.total_label.pack(anchor="e", pady=(10, 0))

        self.carregar_gastos(mes_atual, "Todas")

    def carregar_gastos(self, mes, categoria, data_inicio=None, data_fim=None):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        gastos = gasto_controller.buscar_gastos_por_mes(mes)

        total = 0.0
        for g in gastos:
            if categoria != "Todas" and g["categoria"] != categoria:
                continue

            data_gasto = g.get("data", "")[:10]
            if data_inicio and data_gasto < data_inicio:
                continue
            if data_fim and data_gasto > data_fim:
                continue

            self.tabela.insert("", "end", values=(
                g["descricao"],
                g["categoria"],
                f"{g['valor']:.2f}",
                data_gasto
            ))
            total += g["valor"]

        self.total_label.config(text=f"Total: R$ {total:.2f}")

    def filtrar_gastos(self):
        mes = self.mes_var.get()
        categoria = self.categoria_var.get()
        data_inicio = self.data_inicio_var.get().strip() or None
        data_fim = self.data_fim_var.get().strip() or None

        self.carregar_gastos(mes, categoria, data_inicio, data_fim)
