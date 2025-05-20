from tkinter import ttk
import tkinter

class IncluirGastosView:
    def __init__(self, root, voltar_callback):
        self.root = root
        self.voltar_callback = voltar_callback

        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(fill="both", expand=True)

        self.btn_voltar = ttk.Button(self.frame, text="⬅ Home", command=self.voltar_callback)
        self.btn_voltar.pack(anchor="w")

        self.label = ttk.Label(self.frame, text="Valor Gasto", font=("Arial", 18))
        self.label.pack(pady=2)

        self.label = ttk.Entry(root, font=('calibre',10,'normal'))
        self.label.pack(pady=2)

        self.label = ttk.Label(self.frame, text="Descrição", font=("Arial", 18))
        self.label.pack(pady=2)

        self.label = ttk.Entry(root, font=('calibre',10,'normal'))
        self.label.pack(pady=2)

        options_list = ["Lazer", "Estudo", "Despesas Fixas", "Outros"]
        value_inside = tkinter.StringVar(root)
        value_inside.set("Selecione qual o Propósito do gasto")

        self.label = ttk.OptionMenu(root,value_inside,*options_list)
        self.label.pack(pady=2)
        
