import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,Menu
from ventanas.creacion_frame import frame_orden_compra_amepp,frame_orden_compra_adepp

class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.menu = tk.Menu(parent)
        self.menu_inicio = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Ordenes de compra",menu=self.menu_inicio)
        self.menu_inicio.add_command(label="Crear orden de compra AMEPP",command=self.crear_orden_compra_amepp)
        self.menu_inicio.add_command(label="Crear orden de compra ADEPP",command=self.crear_orden_compra_adepp)
        parent.config(menu=self.menu)
        
        self.menu_afiliados= tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Afiliados", menu=self.menu_afiliados)
        self.menu_afiliados.add_command(label="Agregar afiliados Amepp",command="self.crear_frame_busqueda_dni")
        self.menu_afiliados.add_command(label="Agregar afiliados Adepp",command="self.crear_frame_busqueda_cuenta")
        parent.config(menu=self.menu)


        self._frame = None


    
    def crear_orden_compra_amepp(self):
         if self._frame is not None:
            self._frame.borrar()
            self._frame = None
         if self._frame is None:
            self._frame = frame_orden_compra_amepp(self)

    def crear_orden_compra_adepp(self):      
         if self._frame is not None:
            self._frame.borrar()
            self._frame = None
         if self._frame is None:
            self._frame = frame_orden_compra_adepp(self)