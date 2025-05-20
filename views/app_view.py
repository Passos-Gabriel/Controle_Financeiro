import tkinter as tk
from tkinter import ttk
from datetime import datetime
from views.incluir_gastos_view import IncluirGastosView
from views.relatorio_gastos_view import RelatorioGastosView
from views.setar_valor_view import SetarValorView
import locale

try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except:
    pass

class AppView:
    def __init__(self, root):
        self.root = root
        root.title("Calculadora Financeira")
        root.geometry("400x300")
        root.resizable(False, False)

        self.mostrar_tela_principal()

    def mostrar_tela_principal(self):
        # Limpa a tela antes de desenhar
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill="both", expand=True)

        mes_atual = datetime.now().strftime("%B").capitalize()

        self.saldo_label = ttk.Label(self.root, text=f"Saldo Atual ({mes_atual}): R$ 00,00", anchor="e", font=("Arial", 10, "bold"))
        self.saldo_label.place(relx=1.0, x=-10, y=10, anchor="ne")

        titulo = ttk.Label(frame, text="Menu Principal", font=("Arial", 16, "bold"))
        titulo.pack(pady=(50, 30))

        self.btn_incluir = ttk.Button(frame, text="Incluir Gastos do Mês Atual", width=30, command=self.abrir_incluir_gastos_view)
        self.btn_incluir.pack(pady=10)

        self.btn_relatorio = ttk.Button(frame, text="Ver Relatório de Gastos", width=30, command=self.abrir_relatorio_gastos_view)
        self.btn_relatorio.pack(pady=10)

        self.btn_relatorio = ttk.Button(frame, text="Inserir Limite para Gasto", width=30, command=self.abrir_setar_valor_view)
        self.btn_relatorio.pack(pady=10)

    def abrir_incluir_gastos_view(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Agora sim: passando a função correta que volta para o menu
        IncluirGastosView(self.root, self.mostrar_tela_principal)

    def abrir_relatorio_gastos_view(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        RelatorioGastosView(self.root, self.mostrar_tela_principal)

    def abrir_setar_valor_view(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        SetarValorView(self.root, self.mostrar_tela_principal)
