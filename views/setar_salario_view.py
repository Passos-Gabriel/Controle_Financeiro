from tkinter import ttk
import tkinter as tk
import controllers.salario_controller as salario_controller
import views.incluir_gastos_view as pop_up

class SetarSalarioView:
    def __init__(self, root, voltar_callback):
        self.root = root
        self.voltar_callback = voltar_callback

        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(fill="both", expand=True)

        ttk.Button(self.frame, text="⬅ Home", command=self.voltar_callback).pack(anchor="w")

        ttk.Label(
            self.frame,
            text="Definir Salário Líquido",
            font=("Arial", 16, "bold")
        ).pack(pady=(10, 20))

        ttk.Label(self.frame, text="Salário líquido (R$):").pack(anchor="w")
        self.entry_salario = ttk.Entry(self.frame)
        self.entry_salario.pack(fill="x", pady=(0, 20))

        ttk.Button(
            self.frame,
            text="Salvar Salário",
            command=self.salvar
        ).pack()

    def salvar(self):
        try:
            valor = float(self.entry_salario.get())
        except ValueError:
            pop_up.exibir_popup("Erro", "Digite um valor válido.", tipo="erro")
            return

        salario_controller.salvar_salario(valor)
        pop_up.exibir_popup("Sucesso", "Salário salvo com sucesso!", tipo="sucesso")
        self.voltar_callback()
