from .conexion_db import ConexionDB
from tkinter import messagebox
def crear_tabla():
    conexion=ConexionDB()
    sql="""
    CREATE TABLE "afiliados" (
	"orden_amepp"	INTEGER NOT NULL,
	"orden_adepp"	INTEGER NOT NULL,
	"pagare"	    INTEGER NOT NULL
	
);

"""
  

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()      
    except:
        pass
def borrar_tabla():
        conexion=ConexionDB()
        sql='DROP TABLE creditos'
        conexion.cursor.execute(sql)
        conexion.cerrar()
class Ordenes_Compras:
    def __init__(self,orden_amepp,orden_adepp,pagare):
        self.id_ordenes=None
        self.orden_amepp=orden_amepp
        self.orden_adepp=orden_adepp
        self.pagare=pagare
       
    def __str__(self):
        return f'Ordenes_Compras[{self.orden_amepp},{self.orden_adepp},{self.pagare}]'


def buscar_orden_amepp(cuenta):
    conexion=ConexionDB()   
    sql=f""" SELECT orden_amepp FROM afiliados"""
    conexion.cursor.execute(sql)
    numero_orden_amepp=conexion.cursor.fetchone()
    conexion.cerrar()
    if numero_orden_amepp==None:
        return None
    else:
        numero_orden_amepp=list(numero_orden_amepp)
        numero_orden_amepp=numero_orden_amepp[0]
        return numero_orden_amepp



crear_tabla()