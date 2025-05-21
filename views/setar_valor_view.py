from tkinter import ttk, messagebox
import controllers.limites_controller as limites_controller  # Assumindo que vamos criar isso

class SetarValorView:
    def __init__(self, root, voltar_callback):
        self.root = root
        self.voltar_callback = voltar_callback

        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(fill="both", expand=True)

        # Botão voltar
        self.btn_voltar = ttk.Button(self.frame, text="⬅ Home", command=self.voltar_callback)
        self.btn_voltar.pack(anchor="w")

        # Título
        titulo = ttk.Label(self.frame, text="Inserir Valor Limite de Gastos", font=("Arial", 16, "bold"))
        titulo.pack(pady=(10, 20))

        # Campo de entrada do valor
        lbl_valor = ttk.Label(self.frame, text="Valor limite:")
        lbl_valor.pack(pady=(0, 5))

        self.entry_valor = ttk.Entry(self.frame, font=('Arial', 12))
        self.entry_valor.pack(pady=(0, 20))
        valor_atual = limites_controller.buscar_valor_limite_atual()
        if valor_atual is not None:
            self.entry_valor.insert(0, str(valor_atual))

        # Botão de salvar
        btn_salvar = ttk.Button(self.frame, text="Salvar", command=self.salvar_valor)
        btn_salvar.pack()

    def salvar_valor(self):

        try:
            valor = float( self.entry_valor.get())
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido.")
            return

        # Validação
        if not valor:
            messagebox.showerror("Erro", "O campo 'Valor limite' é obrigatório.")
            return

        # Chama o controller para salvar no Supabase
        resultado = limites_controller.adicionar_limite(valor)

        if bool(resultado):
            messagebox.showinfo("Sucesso", "Valor limite salvo com sucesso!")
        else:
            messagebox.showerror("Erro", "Erro ao salvar o valor limite.")
