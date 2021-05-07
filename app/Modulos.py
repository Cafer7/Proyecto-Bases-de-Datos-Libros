import psycopg2
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
class Connection:
    def __init__(self):
        self.connection = None
    def openConnection(self):
        try:
            self.connection = psycopg2.connect(host="localhost",port="5432",dbname="proyecto-libros",user="postgres",password="linux123")
        except Exception as e:
            print (e)

    def closeConnection(self):
        self.connection.close()

def leer_tabla_autor():
    return "SELECT * FROM autor"

def leer_tabla_libro():
    return "SELECT * FROM libro"

def leer_tabla_autor_libro():
    return "SELECT * FROM autor_libro"

def leer_tabla_idioma():
    return "SELECT * FROM idioma"

def leer_tabla_editorial():
    return "SELECT * FROM editorial"

def obtener_libros_con_max_pag_idioma():
    return  """select max_pag.titulo, idioma.nombre_idioma, max_pag.num_paginas from
                idioma join
                (select id, titulo, id_idioma, num_paginas from libro
                where (id_idioma, num_paginas) in
                (select id_idioma, max(num_paginas) from libro
                group by id_idioma)) max_pag on (idioma.id = max_pag.id_idioma)"""
