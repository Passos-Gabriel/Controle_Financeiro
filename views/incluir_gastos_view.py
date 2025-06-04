from tkinter import ttk
import tkinter as tk
import controllers.gasto_controller as gasto
from datetime import datetime

mes_atual = datetime.now().strftime("%B").capitalize()

class IncluirGastosView:
    def __init__(self, root, voltar_callback):
        self.root = root
        self.voltar_callback = voltar_callback
        self.gasto_em_edicao_id = None  # Controla se está editando

        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(fill="both", expand=True)

        # Botão voltar
        self.btn_voltar = ttk.Button(self.frame, text="⬅ Home", command=self.voltar_callback)
        self.btn_voltar.pack(anchor="w")

        # Título
        titulo = ttk.Label(self.frame, text="Adicionar Registro", font=("Arial", 16, "bold"))
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
        self.btn_salvar = ttk.Button(self.frame, text="Salvar Registro", command=self.salvar_gasto)
        self.btn_salvar.pack()

        self.btn_cancelar_edicao = ttk.Button(self.frame, text="Cancelar Edição", command=self.cancelar_edicao)
        self.btn_cancelar_edicao.pack(pady=(5, 10))
        self.btn_cancelar_edicao.pack_forget()  # esconde inicialmente

        btn_apagar = ttk.Button(self.frame, text="🗑 Apagar Registro Selecionado", command=self.apagar_gasto)
        btn_apagar.pack(pady=(5, 10))

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
        # Frame inferior com botão de cancelar e total
        rodape_frame = ttk.Frame(self.frame)
        rodape_frame.pack(fill="x", pady=(10, 0))

        self.btn_cancelar_edicao = ttk.Button(rodape_frame, text="Cancelar Edição", command=self.cancelar_edicao)
        self.btn_cancelar_edicao.pack(side="left")
        self.btn_cancelar_edicao.pack_forget()  # escondido por padrão

        self.label_total = ttk.Label(rodape_frame, text=f"Total dos Gastos de {mes_atual}: R$ 0.00", font=("Arial", 12, "bold"))
        self.label_total.pack(side="right")

        # Preenche a tabela com dados do mês atual
        self.carregar_gastos_mes()
        self.tabela.bind("<Double-1>", self.preencher_campos_para_edicao)

    def preencher_campos_para_edicao(self, event):
        item_selecionado = self.tabela.selection()
        if not item_selecionado:
            return

        gasto_id = item_selecionado[0]
        valores = self.tabela.item(gasto_id, "values")

        data, descricao, categoria, valor = valores
        self.entry_valor.delete(0, tk.END)
        self.entry_valor.insert(0, valor)
        self.entry_descricao.delete(0, tk.END)
        self.entry_descricao.insert(0, descricao)
        self.valor_proposito.set(categoria)

        self.gasto_em_edicao_id = gasto_id

        self.btn_salvar.config(text="Salvar Edição")
        self.btn_cancelar_edicao.pack()

    def cancelar_edicao(self):
        self.entry_valor.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.valor_proposito.set("Selecione...")
        self.gasto_em_edicao_id = None
        self.btn_salvar.config(text="Salvar Registro")
        self.btn_cancelar_edicao.pack_forget()


    def carregar_gastos_mes(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        mes_atual = datetime.now().strftime("%B").capitalize()
        gastos = gasto.buscar_gastos_por_mes(mes_atual)

        total = 0.0
        for g in gastos:
            data = g.get("data", "")[:10]
            self.tabela.insert(
                "", "end", iid=g["id"],  # <- usa o ID como identificador único
                values=(data, g["descricao"], g["categoria"], f"{g['valor']:.2f}")
            )
            total += float(g["valor"])


        self.label_total.config(text=f"Total dos Gastos de {mes_atual}: R$ {total:.2f}")

    def salvar_gasto(self):
        descricao = self.entry_descricao.get().strip()
        categoria = self.valor_proposito.get().strip()

        try:
            valor = float(self.entry_valor.get())
        except ValueError:
            exibir_popup("Erro", "O campo 'Valor Gasto' deve ser um número válido.", tipo="erro")
            return

        if not valor or not descricao or categoria == "Selecione..." or not categoria:
            exibir_popup("Erro", "Todos os campos são obrigatórios.", tipo="erro")
            return

        if self.gasto_em_edicao_id:
            resultado = gasto.atualizar_gasto(self.gasto_em_edicao_id, valor, descricao, categoria)
            if resultado.data:
                exibir_popup("Sucesso", "Gasto atualizado com sucesso!", tipo="sucesso")
            else:
                exibir_popup("Erro", "Falha ao atualizar o gasto.", tipo="erro")
            self.gasto_em_edicao_id = None
        else:
            resultado = gasto.adicionar_gasto(valor, descricao, categoria)
            if resultado.data:
                exibir_popup("Sucesso", "Gasto salvo com sucesso!", tipo="sucesso")
            else:
                exibir_popup("Erro", "Falha ao salvar o gasto.", tipo="erro")

        # Limpar campos e recarregar tabela
        self.entry_valor.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.valor_proposito.set("Selecione...")

        self.entry_valor.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.valor_proposito.set("Selecione...")
        self.carregar_gastos_mes()

        self.btn_salvar.config(text="Salvar Registro")
        self.btn_cancelar_edicao.pack_forget()
        self.carregar_gastos_mes()

    def apagar_gasto(self):
        item_selecionado = self.tabela.selection()
        if not item_selecionado:
            exibir_popup("Atenção", "Selecione um gasto para apagar.", tipo="info")
            return

        gasto_id = item_selecionado[0]  # o ID está como iid
        confirmacao = tk.messagebox.askyesno("Confirmar", "Tem certeza que deseja apagar este gasto?")

        if confirmacao:
            resultado = gasto.deletar_gasto(gasto_id)
            if resultado:
                exibir_popup("Sucesso", "Gasto apagado com sucesso!", tipo="sucesso")
                self.carregar_gastos_mes()
            else:
                exibir_popup("Erro", "Falha ao apagar o gasto.", tipo="erro")


# Função auxiliar para mostrar pop-ups personalizados
def exibir_popup(titulo, mensagem, tipo="info"):
    popup = tk.Toplevel()
    popup.title(titulo)
    popup.geometry("300x150")
    popup.resizable(False, False)
    popup.configure(bg="#f0f0f0")

    # Centraliza o popup
    popup.update_idletasks()
    x = (popup.winfo_screenwidth() // 2) - (300 // 2)
    y = (popup.winfo_screenheight() // 2) - (150 // 2)
    popup.geometry(f"+{x}+{y}")

    # Frame principal
    frame = ttk.Frame(popup, padding=20)
    frame.pack(expand=True, fill="both")

    # Ícone
    icone = {
        "info": "ℹ️",
        "erro": "❌",
        "sucesso": "✅"
    }.get(tipo, "ℹ️")

    lbl_titulo = ttk.Label(frame, text=f"{icone} {titulo}", font=("Arial", 12, "bold"))
    lbl_titulo.pack(pady=(0, 10))

    lbl_msg = ttk.Label(frame, text=mensagem, wraplength=260)
    lbl_msg.pack(pady=(0, 20))

    btn_ok = ttk.Button(frame, text="OK", command=popup.destroy)
    btn_ok.pack()

    popup.transient()
    popup.grab_set()
    popup.wait_window()
