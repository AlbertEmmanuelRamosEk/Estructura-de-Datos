import customtkinter as ctk
import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import os
import io

class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()
        self.crear_grafo()

    def crear_grafo(self):
        self.grafo.add_weighted_edges_from([
            ("Jalisco", "Nayarit", 120),
            ("Jalisco", "Zacatecas", 280),
            ("Nayarit", "Sinaloa", 220),
            ("Zacatecas", "Durango", 190),
            ("Durango", "Sinaloa", 210),
            ("Durango", "Chihuahua", 250),
            ("Chihuahua", "Coahuila", 320),
            ("Zacatecas", "Coahuila", 400),
            ("Jalisco", "Durango", 300)
        ])

    def vertices(self):
        return list(self.grafo.nodes)

    def numVertices(self):
        return self.grafo.number_of_nodes()

    def numAristas(self):
        return self.grafo.number_of_edges()

    def recorrido_sin_repetir(self):
        recorrido = list(nx.dfs_preorder_nodes(self.grafo, source="Jalisco"))
        costo = sum(
            self.grafo[recorrido[i]][recorrido[i+1]]["weight"]
            for i in range(len(recorrido)-1)
        )
        return recorrido, costo

    def recorrido_con_repetir(self):
        recorrido = ["Jalisco", "Nayarit", "Sinaloa", "Durango", "Zacatecas", "Jalisco", "Coahuila"]
        costo = sum(
            self.grafo[recorrido[i]][recorrido[i+1]]["weight"]
            for i in range(len(recorrido)-1)
        )
        return recorrido, costo


class InterfazGrafo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Mapa de Estados - Grafo en Python")
        self.geometry("1100x700")
        self.grafo = Grafo()
        self.crear_interfaz()

    def crear_interfaz(self):
        frame_izq = ctk.CTkFrame(self, width=250, corner_radius=15)
        frame_izq.pack(side="left", fill="y", padx=10, pady=10)

        titulo = ctk.CTkLabel(frame_izq, text="Opciones del Grafo", font=("Arial", 18, "bold"))
        titulo.pack(pady=10)

        ctk.CTkButton(frame_izq, text="Mostrar Grafo con Mapa", command=self.mostrar_grafo_con_mapa).pack(pady=10)
        ctk.CTkButton(frame_izq, text="Recorrido sin repetir", command=self.mostrar_recorrido_sin_repetir).pack(pady=10)
        ctk.CTkButton(frame_izq, text="Recorrido con repetir", command=self.mostrar_recorrido_con_repetir).pack(pady=10)

        self.label_info = ctk.CTkLabel(frame_izq, text="", font=("Arial", 14))
        self.label_info.pack(pady=20)

        self.frame_der = ctk.CTkFrame(self, corner_radius=15)
        self.frame_der.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    def mostrar_grafo_con_mapa(self):
        for widget in self.frame_der.winfo_children():
            widget.destroy()

        ruta_imagen = os.path.join(os.path.dirname(__file__), "mapa_mexico.webp")
        if not os.path.exists(ruta_imagen):
            self.label_info.configure(text="❌ No se encontró 'mapa_mexico.webp' en la carpeta del programa.")
            return

        # Cargar mapa base
        mapa = Image.open(ruta_imagen)
        ancho, alto = mapa.size
        fig, ax = plt.subplots(figsize=(8, 6))

        # Mostrar mapa como fondo
        ax.imshow(mapa, extent=[-117, -86, 14, 33])  # Coordenadas aproximadas de México

        # Posiciones geográficas aproximadas (coordenadas para ubicar estados)
        pos_geo = {
            "Jalisco": (-103, 20.5),
            "Nayarit": (-104.8, 21.8),
            "Sinaloa": (-107.5, 25),
            "Durango": (-105.5, 24),
            "Zacatecas": (-102.5, 22.7),
            "Chihuahua": (-106, 28),
            "Coahuila": (-102, 27.5)
        }

        nx.draw(
            self.grafo.grafo,
            pos=pos_geo,
            with_labels=True,
            node_color="skyblue",
            node_size=1800,
            font_size=10,
            font_weight="bold",
            ax=ax,
            width=2
        )

        labels = nx.get_edge_attributes(self.grafo.grafo, 'weight')
        nx.draw_networkx_edge_labels(self.grafo.grafo, pos_geo, edge_labels=labels, font_size=9, ax=ax)

        ax.axis("off")

        buffer = io.BytesIO()
        plt.savefig(buffer, format="png", bbox_inches="tight", dpi=100)
        buffer.seek(0)
        plt.close(fig)

        imagen_grafo = Image.open(buffer)
        imagen_tk = ImageTk.PhotoImage(imagen_grafo)
        label_grafo = ctk.CTkLabel(self.frame_der, image=imagen_tk, text="")
        label_grafo.image = imagen_tk
        label_grafo.pack(expand=True)

        self.label_info.configure(text="✅ Grafo mostrado sobre el mapa real de México.")

    def mostrar_recorrido_sin_repetir(self):
        recorrido, costo = self.grafo.recorrido_sin_repetir()
        self.label_info.configure(
            text=f"Recorrido sin repetir:\n{' → '.join(recorrido)}\nCosto total: {costo}"
        )

    def mostrar_recorrido_con_repetir(self):
        recorrido, costo = self.grafo.recorrido_con_repetir()
        self.label_info.configure(
            text=f"Recorrido con repetir:\n{' → '.join(recorrido)}\nCosto total: {costo}"
        )


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = InterfazGrafo()
    app.mainloop()
