import tkinter as tk
from tkinter import ttk
from datetime import datetime

from views.incluir_gastos_view import IncluirGastosView
from views.relatorio_gastos_view import RelatorioGastosView
from views.setar_valor_view import SetarValorView

from controllers import limites_controller

import locale

try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except:
    pass

class AppView:
    def __init__(self, root):
        self.root = root
        root.title("Calculadora Financeira")
        self.centralizar_janela()
        root.resizable(False, False)

        self.mostrar_tela_principal()

    def mostrar_tela_principal(self):
        # Limpa a tela antes de desenhar
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill="both", expand=True)

        mes_atual = datetime.now().strftime("%B").capitalize()

        saldo = limites_controller.obter_saldo_atual()
        cor_saldo = "green" if saldo >= 0 else "red"
        self.saldo_label = ttk.Label(self.root, text=f"Saldo Atual ({mes_atual}): R$ {saldo:.2f}", anchor="e", font=("Arial", 10, "bold"), foreground= cor_saldo)
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

    def centralizar_janela(self, largura=650, altura=550):
        # pega a largura e altura da tela
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        # calcula a posição x e y para centralizar
        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)

        self.root.geometry(f"{largura}x{altura}+{x}+{y}")