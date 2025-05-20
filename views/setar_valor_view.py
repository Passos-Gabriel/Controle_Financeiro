from tkinter import ttk

class SetarValorView:
    def __init__(self, root, voltar_callback):
        self.root = root
        self.voltar_callback = voltar_callback

        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(fill="both", expand=True)

        self.btn_voltar = ttk.Button(self.frame, text="⬅ Home", command=self.voltar_callback)
        self.btn_voltar.pack(anchor="w")

        # Título da tela
        titulo = ttk.Label(self.frame, text="Inserir Valor", font=("Arial", 16, "bold"))
        titulo.pack(pady=(10, 20))

        # Label teste
        self.label = ttk.Entry(root, font=('calibre',10,'normal'))
        self.label.pack(pady=50)