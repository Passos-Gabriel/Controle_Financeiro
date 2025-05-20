import tkinter as tk
from views.app_view import AppView

if __name__ == "__main__":
    root = tk.Tk()
    app = AppView(root)
    root.mainloop()
