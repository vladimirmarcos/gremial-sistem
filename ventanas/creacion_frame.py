import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,Menu
import datetime
import sqlite3
from models.conexion_db import ConexionDB
from docxtpl import DocxTemplate
from models.creditos_dao import Ordenes_Compras



doc_amepp = DocxTemplate("OrdendeCompraenBlancoAMEPPMODELO.docx")
doc_adepp =DocxTemplate("OrdendeCompraenBlancoADEPPMODELO.docx")
class frame_orden_compra_amepp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        
        self.campos_datos_orden_compra()
        self.desahabilitar_campos()
        #self.abrirventana2()

    def campos_datos_orden_compra(self):
        #label de campos
        self.label_nombre=tk.Label(self,text='Nombre')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        self.label_dni=tk.Label(self,text='DNI')
        self.label_dni.config(font=('Arial',12,'bold'))
        self.label_dni.grid(row=1,column=0,padx=10,pady=10)

        self.label_domicilio=tk.Label(self,text='Domicilio')
        self.label_domicilio.config(font=('Arial',12,'bold'))
        self.label_domicilio.grid(row=2,column=0,padx=10,pady=10)

        self.label_Importe=tk.Label(self,text='Importe en texto')
        self.label_Importe.config(font=('Arial',12,'bold'))
        self.label_Importe.grid(row=3,column=0,padx=10,pady=10)  

        
        self.label_dinero=tk.Label(self,text='Importe en número')
        self.label_dinero.config(font=('Arial',12,'bold'))
        self.label_dinero.grid(row=4,column=0,padx=10,pady=10)


        self.label_porcentaje=tk.Label(self,text='Porcentaje de descuento ( en caso de no tener colocar 0)')
        self.label_porcentaje.config(font=('Arial',12,'bold'))
        self.label_porcentaje.grid(row=5,column=0,padx=10,pady=10)

        self.label_cuota=tk.Label(self,text='cuotas ( en caso de no tener colocar 0)')
        self.label_cuota.config(font=('Arial',12,'bold'))
        self.label_cuota.grid(row=6,column=0,padx=10,pady=10)

        self.label_mes=tk.Label(self,text='Mes')
        self.label_mes.config(font=('Arial',12,'bold'))
        self.label_mes.grid(row=7,column=0,padx=10,pady=10)

        self.label_dias=tk.Label(self,text='Días de vigencia')
        self.label_dias.config(font=('Arial',12,'bold'))
        self.label_dias.grid(row=8,column=0,padx=10,pady=10)

       

        #Entrys de cada Campo

        self.mi_nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50,font=('Arial',12))
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

        self.mi_dni=tk.StringVar()
        self.entry_dni=tk.Entry(self,textvariable=self.mi_dni)
        self.entry_dni.config(width=50,font=('Arial',12))
        self.entry_dni.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.mi_domicilio=tk.StringVar()
        self.entry_domicilio=tk.Entry(self,textvariable=self.mi_domicilio)
        self.entry_domicilio.config(width=50,font=('Arial',12))
        self.entry_domicilio.grid(row=2,column=1,padx=10,pady=10,columnspan=2)


        self.mi_importe=tk.StringVar()
        self.entry_importe=tk.Entry(self,textvariable=self.mi_importe)
        self.entry_importe.config(width=50,font=('Arial',12))
        self.entry_importe.grid(row=3,column=1,padx=10,pady=10,columnspan=2)


        self.mi_dinero=tk.StringVar()
        self.entry_dinero=tk.Entry(self,textvariable=self.mi_dinero)
        self.entry_dinero.config(width=50,font=('Arial',12))
        self.entry_dinero.grid(row=4,column=1,padx=10,pady=10,columnspan=2)


        self.mi_porcentaje=tk.StringVar()
        self.entry_porcentaje=tk.Entry(self,textvariable=self.mi_porcentaje)
        self.entry_porcentaje.config(width=50,font=('Arial',12))
        self.entry_porcentaje.grid(row=5,column=1,padx=10,pady=10,columnspan=2) 

        self.mi_cuotas=tk.StringVar()
        self.entry_cuotas=tk.Entry(self,textvariable=self.mi_cuotas)
        self.entry_cuotas.config(width=50,font=('Arial',12))
        self.entry_cuotas.grid(row=6,column=1,padx=10,pady=10,columnspan=2)

        self.mi_mes=tk.StringVar()
        self.entry_mes=tk.Entry(self,textvariable=self.mi_mes)
        self.entry_mes.config(width=50,font=('Arial',12))
        self.entry_mes.grid(row=7,column=1,padx=10,pady=10,columnspan=2)


        self.mi_dias=tk.StringVar()
        self.entry_dias=tk.Entry(self,textvariable=self.mi_dias)
        self.entry_dias.config(width=50,font=('Arial',12))
        self.entry_dias.grid(row=8,column=1,padx=10,pady=10,columnspan=2)


        self.boton_nuevo=tk.Button(self,text="Nueva orden de compra",command=self.habilitar_campos)
        self.boton_nuevo.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_nuevo.grid(row=9,column=0,padx=10,pady=10)

        self.boton_generar=tk.Button(self,text="Generar",command=self.generar_orden_compra)
        self.boton_generar.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#BD152E',cursor='pirate',activebackground='#E15370')
        self.boton_generar.grid(row=9,column=1,padx=10,pady=10)
          
          
        self._frame = None

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_dni.config(state='normal')
        self.entry_domicilio.config(state='normal')
        self.entry_importe.config(state='normal')
        self.entry_dinero.config(state='normal')
        self.entry_porcentaje.config(state='normal')
        self.entry_cuotas.config(state='normal')
        self.entry_mes.config(state='normal')
        self.entry_dias.config(state='normal')
        self.boton_generar.config(state='normal')

    def desahabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_dni.set('')
        self.mi_domicilio.set('')
        self.mi_importe.set('')
        self.mi_dinero.set('')
        self.mi_porcentaje.set('')
        self.mi_cuotas.set('')
        self.mi_mes.set('')
        self.mi_dias.set('')
       
        self.entry_nombre.config(state='disabled')
        self.entry_dni.config(state='disabled')
        self.entry_domicilio.config(state='disabled')
        self.entry_importe.config(state='disabled')
        self.entry_dinero.config(state='disabled')
        self.entry_porcentaje.config(state='disabled')
        self.entry_cuotas.config(state='disabled')
        self.entry_mes.config(state='disabled')
        self.entry_dias.config(state='disabled')
        self.boton_generar.config(state='disabled') 
    def generar_orden_compra(self):
        nombre=self.mi_nombre.get()
        nombre=nombre.lower()
        nombre=nombre.strip()
        dni=self.mi_dni.get()
        dni=dni.strip()
        domicilio=self.mi_domicilio.get()
        domicilio=domicilio.lower()
        domicilio=domicilio.strip()
        importe=self.mi_importe.get()
        importe=importe.lower()
        importe=importe.strip()
        dinero=self.mi_dinero.get()
        dinero=dinero.lower()
        dinero=dinero.strip()
        porcentaje=self.mi_porcentaje.get()
        porcentaje=porcentaje.lower()
        porcentaje=porcentaje.strip()
        cuotas=self.mi_cuotas.get()
        cuotas=cuotas.lower()
        cuotas=cuotas.strip()
        mes=self.mi_mes.get()
        mes=mes.lower()
        mes=mes.strip()
        dia=self.mi_dias.get()
        dia=dia.lower()
        dia=dia.strip()
        self.desahabilitar_campos()
        fecha_actual=datetime.datetime.now()
        fecha_dia=datetime.datetime.strftime(fecha_actual,'%d')
        fecha_mes=self.convertir_mes( int(datetime.datetime.strftime(fecha_actual,'%m')))
        ano=datetime.datetime.strftime(fecha_actual,'%Y')
        try:
          conexion=ConexionDB()   
          sql=f""" SELECT orden_amepp,pagare FROM ordenes_compras WHERE id_ordenes=1"""
          conexion.cursor.execute(sql)
          datos=conexion.cursor.fetchone()
          conexion.cerrar()
          if datos==None:
             return None
          else:
             
             datos=list(datos)
             numero_orden_amepp=datos[0]
             pagare=datos[1]
             try: 
                 
                Ordenes_Compra_Nueva=Ordenes_Compras(numero_orden_amepp+1,1,pagare+1)
                conexion=ConexionDB()
                sql=f"""    update ordenes_compras set orden_amepp='{Ordenes_Compra_Nueva.orden_amepp}', pagare='{Ordenes_Compra_Nueva.pagare}'  WHERE id_ordenes=1;    
                """
                conexion.cursor.execute(sql)
                conexion.cerrar() 
                self.context = {'orden_amep': numero_orden_amepp,
            'fecha_dia': fecha_dia,
            'pagare': pagare,
            'fecha_mes': fecha_mes,
            'ano' : ano,           
            'nombre' : nombre ,
           'dni': dni,
           'domicilio': domicilio,
           'importe': importe,
           'dinero': dinero,
           'porcentaje': porcentaje,
           'cuotas': cuotas,
           'mes':mes,
           'dias':dia}
                doc_amepp.render(self.context)
                self.name="orden_compra_amepp/orden-de-compra-de-"+nombre+".docx"
                doc_amepp.save(self.name)
             except:
                 titulo=" error al registrar la orden de compra de ADEPP"
                 mensaje= "No fue posible acceder a la base de datos, es posible que este siendo utilizada" 
                 messagebox.showerror(titulo,mensaje) 
        except: 
             titulo=" error al registrar la orden de compra de AMEPP"
             mensaje= "No fue posible acceder a la base de datos, es posible que el servidor este apagado" 
             messagebox.showerror(titulo,mensaje) 
    def convertir_mes(self,mes):
    
        if mes==1:
            return "Enero"
        if mes==2:
            return "Febrero"
        if mes==3:
            return "Marzo"
        if mes==4:
            return "Abril"
        if mes==5:
            return "Mayo"
        if mes==6:
            return "Junio"
        if mes==7:
            return "Julio"
        if mes==8:
            return "Agosto"
        if mes==9:
            return "Septiembre"
        if mes==10:
            return "Octubre"
        if mes==11:
            return "Noviembre"
        if mes==12:
            return "Diciembre"
        
        
    def borrar(self):
        self.pack_forget()
        self.destroy()

class frame_orden_compra_adepp(tk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        
        self.campos_datos_orden_compra()
        self.desahabilitar_campos()
        #self.abrirventana2()

    def campos_datos_orden_compra(self):
        #label de campos
        self.label_nombre=tk.Label(self,text='Nombre')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        self.label_dni=tk.Label(self,text='DNI')
        self.label_dni.config(font=('Arial',12,'bold'))
        self.label_dni.grid(row=1,column=0,padx=10,pady=10)

        self.label_domicilio=tk.Label(self,text='Domicilio')
        self.label_domicilio.config(font=('Arial',12,'bold'))
        self.label_domicilio.grid(row=2,column=0,padx=10,pady=10)

        self.label_Importe=tk.Label(self,text='Importe en texto')
        self.label_Importe.config(font=('Arial',12,'bold'))
        self.label_Importe.grid(row=3,column=0,padx=10,pady=10)  

        
        self.label_dinero=tk.Label(self,text='Importe en número')
        self.label_dinero.config(font=('Arial',12,'bold'))
        self.label_dinero.grid(row=4,column=0,padx=10,pady=10)


        self.label_porcentaje=tk.Label(self,text='Porcentaje de descuento ( en caso de no tener colocar 0)')
        self.label_porcentaje.config(font=('Arial',12,'bold'))
        self.label_porcentaje.grid(row=5,column=0,padx=10,pady=10)

        self.label_cuota=tk.Label(self,text='cuotas ( en caso de no tener colocar 0)')
        self.label_cuota.config(font=('Arial',12,'bold'))
        self.label_cuota.grid(row=6,column=0,padx=10,pady=10)

        self.label_mes=tk.Label(self,text='Mes')
        self.label_mes.config(font=('Arial',12,'bold'))
        self.label_mes.grid(row=7,column=0,padx=10,pady=10)

        self.label_dias=tk.Label(self,text='Días de vigencia')
        self.label_dias.config(font=('Arial',12,'bold'))
        self.label_dias.grid(row=8,column=0,padx=10,pady=10)

       

        #Entrys de cada Campo

        self.mi_nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50,font=('Arial',12))
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

        self.mi_dni=tk.StringVar()
        self.entry_dni=tk.Entry(self,textvariable=self.mi_dni)
        self.entry_dni.config(width=50,font=('Arial',12))
        self.entry_dni.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.mi_domicilio=tk.StringVar()
        self.entry_domicilio=tk.Entry(self,textvariable=self.mi_domicilio)
        self.entry_domicilio.config(width=50,font=('Arial',12))
        self.entry_domicilio.grid(row=2,column=1,padx=10,pady=10,columnspan=2)


        self.mi_importe=tk.StringVar()
        self.entry_importe=tk.Entry(self,textvariable=self.mi_importe)
        self.entry_importe.config(width=50,font=('Arial',12))
        self.entry_importe.grid(row=3,column=1,padx=10,pady=10,columnspan=2)


        self.mi_dinero=tk.StringVar()
        self.entry_dinero=tk.Entry(self,textvariable=self.mi_dinero)
        self.entry_dinero.config(width=50,font=('Arial',12))
        self.entry_dinero.grid(row=4,column=1,padx=10,pady=10,columnspan=2)


        self.mi_porcentaje=tk.StringVar()
        self.entry_porcentaje=tk.Entry(self,textvariable=self.mi_porcentaje)
        self.entry_porcentaje.config(width=50,font=('Arial',12))
        self.entry_porcentaje.grid(row=5,column=1,padx=10,pady=10,columnspan=2) 

        self.mi_cuotas=tk.StringVar()
        self.entry_cuotas=tk.Entry(self,textvariable=self.mi_cuotas)
        self.entry_cuotas.config(width=50,font=('Arial',12))
        self.entry_cuotas.grid(row=6,column=1,padx=10,pady=10,columnspan=2)

        self.mi_mes=tk.StringVar()
        self.entry_mes=tk.Entry(self,textvariable=self.mi_mes)
        self.entry_mes.config(width=50,font=('Arial',12))
        self.entry_mes.grid(row=7,column=1,padx=10,pady=10,columnspan=2)


        self.mi_dias=tk.StringVar()
        self.entry_dias=tk.Entry(self,textvariable=self.mi_dias)
        self.entry_dias.config(width=50,font=('Arial',12))
        self.entry_dias.grid(row=8,column=1,padx=10,pady=10,columnspan=2)


        self.boton_nuevo=tk.Button(self,text="Nueva orden de compra",command=self.habilitar_campos)
        self.boton_nuevo.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#158645',cursor='pirate',activebackground='#35BD6F')
        self.boton_nuevo.grid(row=9,column=0,padx=10,pady=10)

        self.boton_generar=tk.Button(self,text="Generar",command=self.generar_orden_compra)
        self.boton_generar.config(width=20,font=('Arial',12,'bold'),fg='#DAD5D6',bg='#BD152E',cursor='pirate',activebackground='#E15370')
        self.boton_generar.grid(row=9,column=1,padx=10,pady=10)


        self.label_titulo=tk.Label(self,text='Orden de Compra ADEPP')
        self.label_titulo.config(font=('Arial',20,'bold'))
        self.label_titulo.grid(row=11,column=0,padx=10,pady=10)
          
        self._frame = None

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_dni.config(state='normal')
        self.entry_domicilio.config(state='normal')
        self.entry_importe.config(state='normal')
        self.entry_dinero.config(state='normal')
        self.entry_porcentaje.config(state='normal')
        self.entry_cuotas.config(state='normal')
        self.entry_mes.config(state='normal')
        self.entry_dias.config(state='normal')
        self.boton_generar.config(state='normal')

    def desahabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_dni.set('')
        self.mi_domicilio.set('')
        self.mi_importe.set('')
        self.mi_dinero.set('')
        self.mi_porcentaje.set('')
        self.mi_cuotas.set('')
        self.mi_mes.set('')
        self.mi_dias.set('')
       
        self.entry_nombre.config(state='disabled')
        self.entry_dni.config(state='disabled')
        self.entry_domicilio.config(state='disabled')
        self.entry_importe.config(state='disabled')
        self.entry_dinero.config(state='disabled')
        self.entry_porcentaje.config(state='disabled')
        self.entry_cuotas.config(state='disabled')
        self.entry_mes.config(state='disabled')
        self.entry_dias.config(state='disabled')
        self.boton_generar.config(state='disabled') 
    def generar_orden_compra(self):
        nombre=self.mi_nombre.get()
        nombre=nombre.lower()
        nombre=nombre.strip()
        dni=self.mi_dni.get()
        dni=dni.strip()
        domicilio=self.mi_domicilio.get()
        domicilio=domicilio.lower()
        domicilio=domicilio.strip()
        importe=self.mi_importe.get()
        importe=importe.lower()
        importe=importe.strip()
        dinero=self.mi_dinero.get()
        dinero=dinero.lower()
        dinero=dinero.strip()
        porcentaje=self.mi_porcentaje.get()
        porcentaje=porcentaje.lower()
        porcentaje=porcentaje.strip()
        cuotas=self.mi_cuotas.get()
        cuotas=cuotas.lower()
        cuotas=cuotas.strip()
        mes=self.mi_mes.get()
        mes=mes.lower()
        mes=mes.strip()
        dia=self.mi_dias.get()
        dia=dia.lower()
        dia=dia.strip()
        self.desahabilitar_campos()
        fecha_actual=datetime.datetime.now()
        fecha_dia=datetime.datetime.strftime(fecha_actual,'%d')
        fecha_mes=self.convertir_mes( int(datetime.datetime.strftime(fecha_actual,'%m')))
        ano=datetime.datetime.strftime(fecha_actual,'%Y')
        try:
          conexion=ConexionDB()   
          sql=f""" SELECT orden_adepp,pagare FROM ordenes_compras WHERE id_ordenes=1"""
          conexion.cursor.execute(sql)
          datos=conexion.cursor.fetchone()
          conexion.cerrar()
          if datos==None:
             return None
          else:
             
             datos=list(datos)
             numero_orden_adepp=datos[0]
             pagare=datos[1]
             try: 
                 
                Ordenes_Compra_Nueva=Ordenes_Compras(1,numero_orden_adepp+1,pagare+1)
                conexion=ConexionDB()
                sql=f"""    update ordenes_compras set orden_adepp='{Ordenes_Compra_Nueva.orden_adepp}', pagare='{Ordenes_Compra_Nueva.pagare}'  WHERE id_ordenes=1;    
                """
                conexion.cursor.execute(sql)
                conexion.cerrar() 
                self.context = {'orden_adepp': numero_orden_adepp,
            'fecha_dia': fecha_dia,
            'pagare': pagare,
            'fecha_mes': fecha_mes,
            'ano' : ano,           
            'nombre' : nombre ,
           'dni': dni,
           'domicilio': domicilio,
           'importe': importe,
           'dinero': dinero,
           'porcentaje': porcentaje,
           'cuotas': cuotas,
           'mes':mes,
           'dias':dia}
                doc_adepp.render(self.context)
                self.name="orden_compra_adepp/orden-de-compra-de-"+nombre+".docx"
                doc_adepp.save(self.name)
             except:
                 titulo=" error al registrar la orden de compra de ADEPP"
                 mensaje= "No fue posible acceder a la base de datos, es posible que este siendo utilizada" 
                 messagebox.showerror(titulo,mensaje) 
        except: 
             titulo=" error al registrar la orden de compra de ADEPP"
             mensaje= "No fue posible acceder a la base de datos, es posible que el servidor este apagado" 
             messagebox.showerror(titulo,mensaje) 
    def convertir_mes(self,mes):
        if mes==1:
            return "Enero"
        if mes==2:
            return "Febrero"
        if mes==3:
            return "Marzo"
        if mes==4:
            return "Abril"
        if mes==5:
            return "Mayo"
        if mes==6:
            return "Junio"
        if mes==7:
            return "Julio"
        if mes==8:
            return "Agosto"
        if mes==9:
            return "Septiembre"
        if mes==10:
            return "Octubre"
        if mes==11:
            return "Noviembre"
        if mes==12:
            return "Diciembre"
        
        
    def borrar(self):
        self.pack_forget()
        self.destroy()
