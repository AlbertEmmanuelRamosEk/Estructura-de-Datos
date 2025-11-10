import customtkinter as ctk
import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import os
import io

class GrafoInteractivo:
    def __init__(self):
        self.grafo = nx.Graph()
        self.posiciones = {}
        self.estado_actual = None

    def agregar_nodo(self, nombre, x, y):
        self.grafo.add_node(nombre)
        self.posiciones[nombre] = (x, y)

    def agregar_arista(self, origen, destino, peso):
        self.grafo.add_edge(origen, destino, weight=peso)

    def recorrido_sin_repetir(self):
        if not self.grafo:
            return [], 0
        recorrido = list(nx.dfs_preorder_nodes(self.grafo, source=list(self.grafo.nodes)[0]))
        costo = sum(
            self.grafo[recorrido[i]][recorrido[i + 1]]["weight"]
            for i in range(len(recorrido) - 1)
        )
        return recorrido, costo

    def recorrido_con_repetir(self):
        if not self.grafo:
            return [], 0
        nodos = list(self.grafo.nodes)
        if len(nodos) < 2:
            return [], 0
        recorrido = nodos + [nodos[0]]
        costo = sum(
            self.grafo[recorrido[i]][recorrido[i + 1]]["weight"]
            for i in range(len(recorrido) - 1)
        )
        return recorrido, costo


class InterfazGrafo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Grafo Interactivo - Mapa de México")
        self.geometry("1100x700")
        self.grafo = GrafoInteractivo()
        self.imagen_tk = None
        self.canvas = None
        self.mapa = None
        self.crear_interfaz()

    def crear_interfaz(self):
        frame_izq = ctk.CTkFrame(self, width=250, corner_radius=15)
        frame_izq.pack(side="left", fill="y", padx=10, pady=10)

        titulo = ctk.CTkLabel(frame_izq, text="Opciones del Grafo", font=("Arial", 18, "bold"))
        titulo.pack(pady=10)

        ctk.CTkButton(frame_izq, text="Cargar Mapa", command=self.cargar_mapa).pack(pady=10)
        ctk.CTkButton(frame_izq, text="Mostrar Grafo", command=self.mostrar_grafo).pack(pady=10)
        ctk.CTkButton(frame_izq, text="Recorrido sin repetir", command=self.recorrido_sin_repetir).pack(pady=10)
        ctk.CTkButton(frame_izq, text="Recorrido con repetir", command=self.recorrido_con_repetir).pack(pady=10)

        self.label_info = ctk.CTkLabel(frame_izq, text="", font=("Arial", 14), wraplength=200)
        self.label_info.pack(pady=20)

        self.frame_der = ctk.CTkFrame(self, corner_radius=15)
        self.frame_der.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    def cargar_mapa(self):
        for widget in self.frame_der.winfo_children():
            widget.destroy()

        ruta_imagen = os.path.join(os.path.dirname(__file__), "mapa_mexico.webp")
        if not os.path.exists(ruta_imagen):
            self.label_info.configure(text="❌ No se encontró 'mapa_mexico.webp' en la carpeta del programa.")
            return

        self.mapa = Image.open(ruta_imagen).resize((800, 600))
        self.imagen_tk = ImageTk.PhotoImage(self.mapa)

        self.canvas = ctk.CTkCanvas(self.frame_der, width=800, height=600, bg="white", highlightthickness=0)
        self.canvas.pack(expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagen_tk)

        self.canvas.bind("<Button-1>", self.colocar_nodo)
        self.label_info.configure(text="🖱️ Haz clic en el mapa para colocar los nodos (estados).")

    def colocar_nodo(self, event):
        nombre = f"Estado_{len(self.grafo.grafo.nodes) + 1}"
        x, y = event.x, event.y
        self.grafo.agregar_nodo(nombre, x, y)
        self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="skyblue")
        self.canvas.create_text(x, y - 15, text=nombre, fill="black", font=("Arial", 10, "bold"))
        self.label_info.configure(text=f"Nodo agregado: {nombre} en ({x}, {y})")

        if len(self.grafo.grafo.nodes) > 1:
            anterior = list(self.grafo.grafo.nodes)[-2]
            peso = ctk.CTkInputDialog(text=f"Ingresa el costo entre {anterior} y {nombre}:", title="Costo del traslado").get_input()
            try:
                peso = int(peso)
                self.grafo.agregar_arista(anterior, nombre, peso)
                self.canvas.create_line(
                    self.grafo.posiciones[anterior][0],
                    self.grafo.posiciones[anterior][1],
                    x,
                    y,
                    fill="black",
                    width=2
                )
            except:
                self.label_info.configure(text="⚠️ Costo inválido. No se agregó la arista.")

    def mostrar_grafo(self):
        if not self.grafo.grafo:
            self.label_info.configure(text="⚠️ No hay nodos en el grafo.")
            return

        plt.figure(figsize=(8, 6))
        nx.draw(
            self.grafo.grafo,
            pos=self.grafo.posiciones,
            with_labels=True,
            node_color="skyblue",
            node_size=1500,
            font_size=10,
            font_weight="bold"
        )
        labels = nx.get_edge_attributes(self.grafo.grafo, "weight")
        nx.draw_networkx_edge_labels(self.grafo.grafo, self.grafo.posiciones, edge_labels=labels)
        plt.show()

    def recorrido_sin_repetir(self):
        recorrido, costo = self.grafo.recorrido_sin_repetir()
        if not recorrido:
            self.label_info.configure(text="⚠️ El grafo está vacío.")
            return
        self.label_info.configure(text=f"Recorrido sin repetir:\n{' → '.join(recorrido)}\nCosto total: {costo}")

    def recorrido_con_repetir(self):
        recorrido, costo = self.grafo.recorrido_con_repetir()
        if not recorrido:
            self.label_info.configure(text="⚠️ El grafo está vacío.")
            return
        self.label_info.configure(text=f"Recorrido con repetir:\n{' → '.join(recorrido)}\nCosto total: {costo}")


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = InterfazGrafo()
    app.mainloop()
