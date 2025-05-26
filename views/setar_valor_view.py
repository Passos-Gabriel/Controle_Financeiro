from tkinter import ttk, Toplevel
import tkinter as tk
import controllers.limites_controller as limites_controller

class SetarValorView:
    def __init__(self, root, voltar_callback):
        self.root = root
        self.voltar_callback = voltar_callback

        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(fill="both", expand=True)

        self.btn_voltar = ttk.Button(self.frame, text="⬅ Home", command=self.voltar_callback)
        self.btn_voltar.pack(anchor="w")

        titulo = ttk.Label(self.frame, text="Inserir Valor Limite de Gastos", font=("Arial", 16, "bold"))
        titulo.pack(pady=(10, 20))

        lbl_valor = ttk.Label(self.frame, text="Valor limite:")
        lbl_valor.pack(pady=(0, 5))

        self.entry_valor = ttk.Entry(self.frame, font=('Arial', 12))
        self.entry_valor.pack(pady=(0, 20))

        valor_atual = limites_controller.buscar_valor_limite_atual()
        if valor_atual is not None:
            self.entry_valor.insert(0, str(valor_atual))

        btn_salvar = ttk.Button(self.frame, text="Salvar", command=self.salvar_valor)
        btn_salvar.pack()

    def salvar_valor(self):
        try:
            valor = float(self.entry_valor.get())
        except ValueError:
            self.mostrar_pop_up("Erro", "Digite um número válido.", erro=True)
            return

        if not valor:
            self.mostrar_pop_up("Erro", "O campo 'Valor limite' é obrigatório.", erro=True)
            return

        resultado = limites_controller.adicionar_limite(valor)

        if bool(resultado):
            self.mostrar_pop_up("Sucesso", f"Novo limite definido: R$ {valor:.2f}")
        else:
            self.mostrar_pop_up("Erro", "Erro ao salvar o valor limite.", erro=True)

    def mostrar_pop_up(self, titulo, mensagem, erro=False):
        popup = Toplevel(self.root)
        popup.title(titulo)
        popup.transient(self.root)
        popup.grab_set()
        popup.resizable(False, False)

        # Define tamanho fixo do popup
        largura = 300
        altura = 150

        # Obtém as dimensões da janela principal
        root_x = self.root.winfo_rootx()
        root_y = self.root.winfo_rooty()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()

        # Aguarda a janela principal atualizar (garante medidas corretas)
        self.root.update_idletasks()

        # Calcula coordenadas para centralizar
        x = root_x + (root_width // 2) - (largura // 2)
        y = root_y + (root_height // 2) - (altura // 2)

        popup.geometry(f"{largura}x{altura}+{x}+{y}")

        # Conteúdo do popup
        frame = ttk.Frame(popup, padding=20)
        frame.pack(expand=True, fill="both")

        estilo = ("Arial", 12, "bold" if not erro else "normal")
        cor = "red" if erro else "green"

        lbl_titulo = ttk.Label(frame, text=titulo, font=("Arial", 14, "bold"), foreground=cor)
        lbl_titulo.pack(pady=(0, 10))

        lbl_msg = ttk.Label(frame, text=mensagem, font=estilo, wraplength=260, justify="center")
        lbl_msg.pack(pady=(0, 10))

        btn_ok = ttk.Button(frame, text="OK", command=popup.destroy)
        btn_ok.pack(pady=(5, 0))
