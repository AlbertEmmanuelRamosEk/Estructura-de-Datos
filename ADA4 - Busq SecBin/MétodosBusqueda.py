import customtkinter as ctk
import time

# --- CONFIGURACIÓN DE LA APP ---
ctk.set_appearance_mode("Dark")       # Modo oscuro
ctk.set_default_color_theme("blue")   # Tema de color azul

class BusquedaVisualApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Visualizador de Algoritmos de Búsqueda")
        self.geometry("1000x600")

        # Variables de estado
        self.datos = []     # Lista interna de números
        self.cajas_ui = []  # Referencias a los objetos visuales (cuadritos)

        # --- DISEÑO DE LA INTERFAZ (LAYOUT) ---
        
        # 1. Panel Izquierdo (Controles)
        self.panel_control = ctk.CTkFrame(self, width=280, corner_radius=0)
        self.panel_control.pack(side="left", fill="y", padx=0, pady=0)

        self.lbl_titulo = ctk.CTkLabel(self.panel_control, text="Panel de Control", font=("Roboto", 20, "bold"))
        self.lbl_titulo.pack(pady=20)

        # Sección: Ingreso de Datos
        self.lbl_datos = ctk.CTkLabel(self.panel_control, text="1. Ingresa la lista (ej: 5,10,2):")
        self.lbl_datos.pack(pady=(10, 0))
        
        self.entrada_datos = ctk.CTkEntry(self.panel_control, placeholder_text="Ej: 20, 5, 8, 30")
        self.entrada_datos.pack(pady=5, padx=20, fill="x")

        self.btn_cargar = ctk.CTkButton(self.panel_control, text="Crear Lista Visual", command=self.cargar_datos, fg_color="#2CC985", hover_color="#25A970")
        self.btn_cargar.pack(pady=10, padx=20, fill="x")

        # Separador visual
        ctk.CTkFrame(self.panel_control, height=2, fg_color="gray30").pack(fill="x", padx=20, pady=10)

        # Sección: Objetivo a Buscar
        self.lbl_obj = ctk.CTkLabel(self.panel_control, text="2. ¿Qué número buscas?")
        self.lbl_obj.pack(pady=(10, 0))

        self.entrada_objetivo = ctk.CTkEntry(self.panel_control, placeholder_text="Número objetivo")
        self.entrada_objetivo.pack(pady=5, padx=20, fill="x")

        # Botones de Algoritmos
        self.btn_secuencial = ctk.CTkButton(self.panel_control, text="Búsqueda Secuencial", command=self.run_secuencial)
        self.btn_secuencial.pack(pady=10, padx=20, fill="x")

        self.btn_binaria = ctk.CTkButton(self.panel_control, text="Búsqueda Binaria", command=self.run_binaria)
        self.btn_binaria.pack(pady=10, padx=20, fill="x")

        self.btn_hash = ctk.CTkButton(self.panel_control, text="Búsqueda Hash (Directa)", command=self.run_hash)
        self.btn_hash.pack(pady=10, padx=20, fill="x")

        # Consola de Estado (Texto abajo)
        self.lbl_status = ctk.CTkLabel(self.panel_control, text="Esperando datos...", text_color="gray", wraplength=250, font=("Roboto", 14))
        self.lbl_status.pack(side="bottom", pady=30)

        # 2. Panel Derecho (Visualización)
        self.panel_visual = ctk.CTkScrollableFrame(self, label_text="Área de Visualización")
        self.panel_visual.pack(side="right", expand=True, fill="both", padx=10, pady=10)

    # --- LÓGICA DE DIBUJO ---

    def cargar_datos(self):
        try:
            texto = self.entrada_datos.get()
            # Convertimos el texto "1, 2, 3" en lista [1, 2, 3]
            self.datos = [int(x.strip()) for x in texto.split(',')]
            self.dibujar_elementos(self.datos)
            self.lbl_status.configure(text=f"Lista cargada con {len(self.datos)} elementos.", text_color="white")
        except ValueError:
            self.lbl_status.configure(text="Error: Asegúrate de usar solo números enteros separados por comas.", text_color="#FF5555")

    def dibujar_elementos(self, lista_datos):
        # Limpiar panel derecho
        for widget in self.panel_visual.winfo_children():
            widget.destroy()
        self.cajas_ui = []

        # Crear un botón (caja) por cada número
        for i, num in enumerate(lista_datos):
            # Usamos botones porque es fácil cambiarles el color y se ven bien
            caja = ctk.CTkButton(
                self.panel_visual, 
                text=str(num), 
                width=60, height=60, 
                font=("Arial", 20, "bold"),
                fg_color="#3B8ED0", # Color base (Azul)
                hover=False # Desactivar efecto hover para controlarlo nosotros
            )
            caja.grid(row=0, column=i, padx=5, pady=50) # Usamos grid para alinearlos
            self.cajas_ui.append(caja)

    def obtener_objetivo(self):
        try:
            val = int(self.entrada_objetivo.get())
            return val
        except ValueError:
            self.lbl_status.configure(text="Error: Ingresa un número objetivo válido.", text_color="#FF5555")
            return None

    def resetear_colores(self):
        for caja in self.cajas_ui:
            caja.configure(fg_color="#3B8ED0") # Volver a azul

    # --- ALGORITMOS DE BÚSQUEDA ---

    # 1. SECUENCIAL
    def run_secuencial(self):
        obj = self.obtener_objetivo()
        if obj is None or not self.datos: return
        
        self.resetear_colores()
        self.lbl_status.configure(text="Iniciando Secuencial...", text_color="#F1C40F")
        self.update()

        encontrado = False
        for i, caja in enumerate(self.cajas_ui):
            val = int(caja.cget("text"))
            
            # Animación: Amarillo (Comparando)
            caja.configure(fg_color="#F1C40F") 
            self.lbl_status.configure(text=f"¿Es {val} igual a {obj}?")
            self.update()
            time.sleep(0.5) # Velocidad de animación

            if val == obj:
                caja.configure(fg_color="#2CC985") # Verde (Éxito)
                self.lbl_status.configure(text=f"¡ENCONTRADO en índice {i}!", text_color="#2CC985")
                encontrado = True
                break
            else:
                caja.configure(fg_color="#C0392B") # Rojo (Fallo)
        
        if not encontrado:
            self.lbl_status.configure(text="No encontrado en la lista.", text_color="#FF5555")

    # 2. BINARIA
    def run_binaria(self):
        obj = self.obtener_objetivo()
        if obj is None or not self.datos: return

        # Paso Obligatorio: Ordenar visualmente primero
        self.lbl_status.configure(text="Ordenando datos para Binaria...", text_color="#F1C40F")
        self.datos.sort()          # Ordenar lógica
        self.dibujar_elementos(self.datos) # Ordenar visual
        self.update()
        time.sleep(1)

        low = 0
        high = len(self.datos) - 1
        encontrado = False

        while low <= high:
            mid = (low + high) // 2
            caja_mid = self.cajas_ui[mid]
            val_mid = int(caja_mid.cget("text"))

            # Animación Centro
            caja_mid.configure(fg_color="#F1C40F")
            self.lbl_status.configure(text=f"Pivote medio: {val_mid}. Comparando con {obj}...")
            self.update()
            time.sleep(0.8)

            if val_mid == obj:
                caja_mid.configure(fg_color="#2CC985")
                self.lbl_status.configure(text=f"¡ENCONTRADO en índice {mid}!", text_color="#2CC985")
                encontrado = True
                break
            elif val_mid < obj:
                # Descartar mitad izquierda (Oscurecer)
                for i in range(low, mid + 1):
                    self.cajas_ui[i].configure(fg_color="#222222") 
                low = mid + 1
            else:
                # Descartar mitad derecha (Oscurecer)
                for i in range(mid, high + 1):
                    self.cajas_ui[i].configure(fg_color="#222222")
                high = mid - 1
        
        if not encontrado:
            self.lbl_status.configure(text="El número no existe.", text_color="#FF5555")

    # 3. HASH
    def run_hash(self):
        obj = self.obtener_objetivo()
        if obj is None or not self.datos: return

        # Para Hash, redibujamos la lista actual para limpiar colores previos
        self.resetear_colores()
        self.lbl_status.configure(text="Creando Tabla Hash en memoria...", text_color="#9B59B6")
        self.update()
        time.sleep(0.8)

        # Crear el diccionario (Tabla Hash)
        # Clave: Numero, Valor: Indice
        tabla_hash = {valor: i for i, valor in enumerate(self.datos)}

        if obj in tabla_hash:
            idx = tabla_hash[obj]
            # Acceso Directo (Animación rápida)
            caja = self.cajas_ui[idx]
            
            self.lbl_status.configure(text="¡Calculando posición directa!", text_color="#9B59B6")
            caja.configure(fg_color="#9B59B6") # Morado (Magia/Hash)
            self.update()
            time.sleep(0.5)
            
            caja.configure(fg_color="#2CC985") # Verde
            self.lbl_status.configure(text=f"Acceso directo O(1) al índice {idx}", text_color="#2CC985")
        else:
            self.lbl_status.configure(text="La clave no existe en la Tabla Hash.", text_color="#FF5555")

# --- PUNTO DE ENTRADA ---
if __name__ == "__main__":
    app = BusquedaVisualApp()
    app.mainloop()