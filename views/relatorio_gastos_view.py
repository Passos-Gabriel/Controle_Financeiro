from tkinter import ttk

class RelatorioGastosView:
    def __init__(self, root, voltar_callback):
        self.root = root
        self.voltar_callback = voltar_callback

        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(fill="both", expand=True)

        self.btn_voltar = ttk.Button(self.frame, text="⬅ Home", command=self.voltar_callback)
        self.btn_voltar.pack(anchor="w")

        # Título da tela
        titulo = ttk.Label(self.frame, text="Ver Relatório de Gastos", font=("Arial", 16, "bold"))
        titulo.pack(pady=(10, 20))

        # Label teste
        self.label = ttk.Label(self.frame, text="TESTE 2", font=("Arial", 18))
        self.label.pack(pady=50)
