import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
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
        self.root.title("Calculadora Financeira")
        self.centralizar_janela()
        self.root.resizable(False, False)

        self.style = ttk.Style("darkly")  # dark theme moderno
        self.mostrar_tela_principal()

    def mostrar_tela_principal(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Frame centralizado
        frame = ttk.Frame(self.root, padding=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        mes_atual = datetime.now().strftime("%B").capitalize()
        saldo = limites_controller.obter_saldo_atual()
        cor_saldo = "#7CFC00" if saldo >= 0 else "#FF4500"

        self.saldo_label = ttk.Label(
            self.root,
            text=f"Saldo Atual ({mes_atual}): R$ {saldo:.2f}",
            anchor="e",
            font=("Arial", 10, "bold"),
            foreground=cor_saldo
        )
        self.saldo_label.place(relx=1.0, x=-10, y=10, anchor="ne")

        titulo = ttk.Label(frame, text="Menu Principal", font=("Arial", 16, "bold"))
        titulo.pack(pady=(0, 30))

        self.btn_incluir = ttk.Button(frame, text="Incluir Gastos do Mês Atual", width=30, bootstyle="info-outline", command=self.abrir_incluir_gastos_view)
        self.btn_incluir.pack(pady=10)

        self.btn_relatorio = ttk.Button(frame, text="Ver Relatório de Gastos", width=30, bootstyle="info-outline", command=self.abrir_relatorio_gastos_view)
        self.btn_relatorio.pack(pady=10)

        self.btn_limite = ttk.Button(frame, text="Inserir Limite para Gasto", width=30, bootstyle="info-outline", command=self.abrir_setar_valor_view)
        self.btn_limite.pack(pady=10)

        # Rodapé
        rodape = ttk.Label(
            self.root,
            text="Created by Gabriel Passos\nEmail: bielpassos@hotmail.com",
            font=("Arial", 9),
            justify="center"
        )
        rodape.place(relx=0.5, rely=1.0, anchor="s", y=-10)  # y=-10 para dar um respiro do fim da janela

    def abrir_incluir_gastos_view(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        IncluirGastosView(self.root, self.mostrar_tela_principal)

    def abrir_relatorio_gastos_view(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        RelatorioGastosView(self.root, self.mostrar_tela_principal)

    def abrir_setar_valor_view(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        SetarValorView(self.root, self.mostrar_tela_principal)

    def centralizar_janela(self, largura=750, altura=600):
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")
