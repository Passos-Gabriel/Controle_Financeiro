from tkinter import ttk

class IncluirGastosView:
    def __init__(self, root, voltar_callback):
        self.root = root
        self.voltar_callback = voltar_callback

        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(fill="both", expand=True)

        self.btn_voltar = ttk.Button(self.frame, text="⬅ Home", command=self.voltar_callback)
        self.btn_voltar.pack(anchor="w")

        self.label = ttk.Label(self.frame, text="TESTE", font=("Arial", 18))
        self.label.pack(pady=50)
