import tkinter as tk
from tkinter import ttk, messagebox

class Pila:
    def __init__(self):
        self.items = []
    def apilar(self, elemento):
        self.items.append(elemento)
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None
    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None
    def esta_vacia(self):
        return len(self.items) == 0
    def mostrar(self):
        return list(self.items)

class PilaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interfaz - Pila (Tkinter)")
        self.geometry("500x400")
        self.resizable(False, False)

        self.pila = Pila()
        self.create_widgets()
        self.update_gui()

    def create_widgets(self):
        frame_top = ttk.Frame(self, padding=12)
        frame_top.pack(fill=tk.X)

        ttk.Label(frame_top, text="Elemento:").pack(side=tk.LEFT)
        self.entry_elem = ttk.Entry(frame_top)
        self.entry_elem.pack(side=tk.LEFT, padx=6)

        btn_apilar = ttk.Button(frame_top, text="Apilar", command=self.on_apilar)
        btn_apilar.pack(side=tk.LEFT, padx=4)

        btn_desapilar = ttk.Button(frame_top, text="Desapilar", command=self.on_desapilar)
        btn_desapilar.pack(side=tk.LEFT, padx=4)

        btn_cima = ttk.Button(frame_top, text="Ver cima", command=self.on_cima)
        btn_cima.pack(side=tk.LEFT, padx=4)

        # Middle: stack visualization and controls
        frame_mid = ttk.Frame(self, padding=12)
        frame_mid.pack(fill=tk.BOTH, expand=True)

        lbl_stack = ttk.Label(frame_mid, text="Contenido de la pila (tope abajo):")
        lbl_stack.pack(anchor=tk.W)

        self.listbox = tk.Listbox(frame_mid, height=10, activestyle='none')
        self.listbox.pack(fill=tk.BOTH, expand=True, pady=6)

        # Bottom: log area
        frame_bot = ttk.Frame(self, padding=12)
        frame_bot.pack(fill=tk.X)

        ttk.Label(frame_bot, text="Registro:").pack(anchor=tk.W)
        self.txt_log = tk.Text(frame_bot, height=6, state=tk.DISABLED)
        self.txt_log.pack(fill=tk.X, pady=6)

        # Menu: limpiar y salir
        menubar = tk.Menu(self)
        appmenu = tk.Menu(menubar, tearoff=0)
        appmenu.add_command(label="Limpiar registro", command=self.limpiar_registro)
        appmenu.add_separator()
        appmenu.add_command(label="Salir", command=self.quit)
        menubar.add_cascade(label="App", menu=appmenu)
        self.config(menu=menubar)

    def on_apilar(self):
        elem = self.entry_elem.get().strip()
        if elem == "":
            messagebox.showwarning("Entrada vacía", "Ingresa un elemento para apilar.")
            return
        self.pila.apilar(elem)
        self.log(f"✓ Apilado: {elem}")
        self.entry_elem.delete(0, tk.END)
        self.update_gui()

    def on_desapilar(self):
        elem = self.pila.desapilar()
        if elem is None:
            self.log("La pila está vacía. No se puede desapilar.")
            messagebox.showinfo("Pila vacía", "La pila está vacía.")
        else:
            self.log(f"✗ Desapilado: {elem}")
        self.update_gui()

    def on_cima(self):
        elem = self.pila.cima()
        if elem is None:
            self.log("Cima: Pila vacía")
            messagebox.showinfo("Cima", "La pila está vacía.")
        else:
            self.log(f"Cima: {elem}")
            messagebox.showinfo("Cima", f"Elemento en cima: {elem}")

    def update_gui(self):
        # Actualiza la lista que muestra la pila
        self.listbox.delete(0, tk.END)
        items = self.pila.mostrar()
        # Queremos mostrar el tope en la parte inferior (como en el ejemplo original)
        # Si prefieres mostrar el tope arriba, invierte items
        for item in items:
            self.listbox.insert(tk.END, item)

    def log(self, mensaje):
        self.txt_log.config(state=tk.NORMAL)
        self.txt_log.insert(tk.END, mensaje + "\n")
        self.txt_log.see(tk.END)
        self.txt_log.config(state=tk.DISABLED)

    def limpiar_registro(self):
        self.txt_log.config(state=tk.NORMAL)
        self.txt_log.delete(1.0, tk.END)
        self.txt_log.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = PilaApp()
    app.mainloop()
