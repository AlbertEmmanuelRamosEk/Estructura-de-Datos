import customtkinter as ctk
from tkinter import messagebox, simpledialog
import math
from collections import deque

# --- NODO ---
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


# --- ÁRBOL BINARIO DE BÚSQUEDA ---
class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def esVacio(self):
        return self.raiz is None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar(nodo.der, valor)
        else:
            messagebox.showinfo("Duplicado", f"El valor {valor} ya existe en el árbol.")

    def buscar(self, nodo, valor):
        if nodo is None:
            return None
        if valor == nodo.valor:
            return nodo
        elif valor < nodo.valor:
            return self.buscar(nodo.izq, valor)
        else:
            return self.buscar(nodo.der, valor)

    # --- RECORRIDOS ---
    def preOrden(self, nodo, recorrido):
        if nodo:
            recorrido.append(nodo.valor)
            self.preOrden(nodo.izq, recorrido)
            self.preOrden(nodo.der, recorrido)

    def inOrden(self, nodo, recorrido):
        if nodo:
            self.inOrden(nodo.izq, recorrido)
            recorrido.append(nodo.valor)
            self.inOrden(nodo.der, recorrido)

    def postOrden(self, nodo, recorrido):
        if nodo:
            self.postOrden(nodo.izq, recorrido)
            self.postOrden(nodo.der, recorrido)
            recorrido.append(nodo.valor)

    # --- ELIMINAR POR PREDECESOR ---
    def eliminar_predecesor(self, valor):
        self.raiz = self._eliminar_predecesor(self.raiz, valor)

    def _eliminar_predecesor(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izq = self._eliminar_predecesor(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eliminar_predecesor(nodo.der, valor)
        else:
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            predecesor = self._maximo(nodo.izq)
            nodo.valor = predecesor.valor
            nodo.izq = self._eliminar_predecesor(nodo.izq, predecesor.valor)
        return nodo

    # --- ELIMINAR POR SUCESOR ---
    def eliminar_sucesor(self, valor):
        self.raiz = self._eliminar_sucesor(self.raiz, valor)

    def _eliminar_sucesor(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izq = self._eliminar_sucesor(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eliminar_sucesor(nodo.der, valor)
        else:
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            sucesor = self._minimo(nodo.der)
            nodo.valor = sucesor.valor
            nodo.der = self._eliminar_sucesor(nodo.der, sucesor.valor)
        return nodo

    def _minimo(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    def _maximo(self, nodo):
        while nodo.der:
            nodo = nodo.der
        return nodo

    # --- RECORRIDO POR NIVELES ---
    def recorrido_niveles(self):
        if self.raiz is None:
            return []
        q = deque([self.raiz])
        niveles = []
        while q:
            actual = q.popleft()
            niveles.append(actual.valor)
            if actual.izq:
                q.append(actual.izq)
            if actual.der:
                q.append(actual.der)
        return niveles

    # --- ALTURA ---
    def altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self.altura(nodo.izq), self.altura(nodo.der))

    # --- CONTAR HOJAS ---
    def contar_hojas(self, nodo):
        if nodo is None:
            return 0
        if nodo.izq is None and nodo.der is None:
            return 1
        return self.contar_hojas(nodo.izq) + self.contar_hojas(nodo.der)

    # --- CONTAR NODOS ---
    def contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contar_nodos(nodo.izq) + self.contar_nodos(nodo.der)

    # --- ÁRBOL COMPLETO ---
    def es_completo(self, nodo):
        if nodo is None:
            return True
        q = deque([nodo])
        bandera_vacio = False
        while q:
            actual = q.popleft()
            if actual:
                if bandera_vacio:
                    return False
                q.append(actual.izq)
                q.append(actual.der)
            else:
                bandera_vacio = True
        return True

    # --- ÁRBOL LLENO ---
    def es_lleno(self, nodo):
        if nodo is None:
            return True
        if (nodo.izq is None) != (nodo.der is None):
            return False
        return self.es_lleno(nodo.izq) and self.es_lleno(nodo.der)

    # --- ELIMINAR ÁRBOL ---
    def eliminar_arbol(self):
        self.raiz = None


# --- INTERFAZ VISUAL ---
class Interfaz(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.title("Árbol Binario de Búsqueda Visual")
        self.geometry("1000x700")

        self.arbol = ArbolBinarioBusqueda()

        # --- Panel izquierdo (botones) ---
        frame_botones = ctk.CTkFrame(self)
        frame_botones.pack(side="left", fill="y", padx=10, pady=10)

        botones = [
            ("[1] Insertar", self.insertar_elemento),
            ("[2] Mostrar árbol", self.mostrar_arbol),
            ("[3] Graficar árbol", self.dibujar_arbol),
            ("[4] Buscar elemento", self.buscar_elemento),
            ("[5] PreOrden", self.mostrar_preorden),
            ("[6] InOrden", self.mostrar_inorden),
            ("[7] PostOrden", self.mostrar_postorden),
            ("[8] Eliminar PREDECESOR", self.eliminar_predecesor),
            ("[9] Eliminar SUCESOR", self.eliminar_sucesor),
            ("[10] Recorrido por niveles", self.mostrar_niveles),
            ("[11] Altura", self.mostrar_altura),
            ("[12] Cantidad de hojas", self.mostrar_hojas),
            ("[13] Cantidad de nodos", self.mostrar_nodos),
            ("[15] ¿Es completo?", self.verificar_completo),
            ("[16] ¿Es lleno?", self.verificar_lleno),
            ("[17] Eliminar árbol", self.eliminar_arbol)
        ]

        for texto, comando in botones:
            ctk.CTkButton(frame_botones, text=texto, command=comando, width=180).pack(pady=4)

        # --- Panel derecho (canvas + salida) ---
        self.canvas = ctk.CTkCanvas(self, bg="#1e1e1e", width=700, height=450, highlightthickness=0)
        self.canvas.pack(pady=10)
        self.salida = ctk.CTkTextbox(self, width=700, height=150)
        self.salida.pack(pady=10)

    # --- FUNCIONES VISUALES ---
    def insertar_elemento(self):
        valor = simpledialog.askinteger("Insertar", "Ingrese un valor entero:")
        if valor is not None:
            self.arbol.insertar(valor)
            self.dibujar_arbol()

    def mostrar_arbol(self):
        self.salida.delete("1.0", "end")
        recorrido = []
        self.arbol.inOrden(self.arbol.raiz, recorrido)
        self.salida.insert("end", f"Árbol en orden (vertical):\n{recorrido}\n")

    def dibujar_arbol(self):
        self.canvas.delete("all")
        if self.arbol.raiz:
            self._dibujar_nodo(self.arbol.raiz, 350, 50, 150)
        else:
            self.canvas.create_text(350, 200, text="Árbol vacío", fill="white", font=("Arial", 16))

    def _dibujar_nodo(self, nodo, x, y, offset):
        if nodo is None:
            return
        radio = 20
        self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="#00b894")
        self.canvas.create_text(x, y, text=str(nodo.valor), fill="white")
        if nodo.izq:
            self.canvas.create_line(x, y + radio, x - offset, y + 80 - radio, fill="white")
            self._dibujar_nodo(nodo.izq, x - offset, y + 80, offset / 1.5)
        if nodo.der:
            self.canvas.create_line(x, y + radio, x + offset, y + 80 - radio, fill="white")
            self._dibujar_nodo(nodo.der, x + offset, y + 80, offset / 1.5)

    def buscar_elemento(self):
        valor = simpledialog.askinteger("Buscar", "Ingrese el valor a buscar:")
        if valor is not None:
            nodo = self.arbol.buscar(self.arbol.raiz, valor)
            self.salida.delete("1.0", "end")
            if nodo:
                self.salida.insert("end", f"El valor {valor} SÍ se encuentra en el árbol.\n")
            else:
                self.salida.insert("end", f"El valor {valor} NO se encuentra en el árbol.\n")

    def mostrar_preorden(self):
        recorrido = []
        self.arbol.preOrden(self.arbol.raiz, recorrido)
        self.salida.delete("1.0", "end")
        self.salida.insert("end", f"PreOrden: {recorrido}\n")

    def mostrar_inorden(self):
        recorrido = []
        self.arbol.inOrden(self.arbol.raiz, recorrido)
        self.salida.delete("1.0", "end")
        self.salida.insert("end", f"InOrden: {recorrido}\n")

    def mostrar_postorden(self):
        recorrido = []
        self.arbol.postOrden(self.arbol.raiz, recorrido)
        self.salida.delete("1.0", "end")
        self.salida.insert("end", f"PostOrden: {recorrido}\n")

    def eliminar_predecesor(self):
        valor = simpledialog.askinteger("Eliminar", "Valor a eliminar (Predecesor):")
        if valor is not None:
            self.arbol.eliminar_predecesor(valor)
            self.dibujar_arbol()

    def eliminar_sucesor(self):
        valor = simpledialog.askinteger("Eliminar", "Valor a eliminar (Sucesor):")
        if valor is not None:
            self.arbol.eliminar_sucesor(valor)
            self.dibujar_arbol()

    def mostrar_niveles(self):
        recorrido = self.arbol.recorrido_niveles()
        self.salida.delete("1.0", "end")
        self.salida.insert("end", f"Recorrido por niveles: {recorrido}\n")

    def mostrar_altura(self):
        h = self.arbol.altura(self.arbol.raiz)
        self.salida.delete("1.0", "end")
        self.salida.insert("end", f"Altura del árbol: {h}\n")

    def mostrar_hojas(self):
        hojas = self.arbol.contar_hojas(self.arbol.raiz)
        self.salida.delete("1.0", "end")
        self.salida.insert("end", f"Cantidad de hojas: {hojas}\n")

    def mostrar_nodos(self):
        nodos = self.arbol.contar_nodos(self.arbol.raiz)
        self.salida.delete("1.0", "end")
        self.salida.insert("end", f"Cantidad de nodos: {nodos}\n")

    def verificar_completo(self):
        es = self.arbol.es_completo(self.arbol.raiz)
        self.salida.delete("1.0", "end")
        self.salida.insert("end", "El árbol es COMPLETO ✅\n" if es else "El árbol NO es completo ❌\n")

    def verificar_lleno(self):
        es = self.arbol.es_lleno(self.arbol.raiz)
        self.salida.delete("1.0", "end")
        self.salida.insert("end", "El árbol es LLENO ✅\n" if es else "El árbol NO es lleno ❌\n")

    def eliminar_arbol(self):
        self.arbol.eliminar_arbol()
        self.dibujar_arbol()
        self.salida.delete("1.0", "end")
        self.salida.insert("end", "Árbol eliminado correctamente.\n")


# --- EJECUTAR ---
if __name__ == "__main__":
    app = Interfaz()
    app.mainloop()
