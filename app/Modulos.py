import psycopg2
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
class Connection:
    def __init__(self):
        self.connection = None
    def openConnection(self):
        try:
            self.connection = psycopg2.connect(host="localhost",port="5432",dbname="proyecto",user="postgres",password="031101")
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

def obtener_libros_con_max_pag_idioma(): #Por idiomas
    return  """select max_pag.titulo, idioma.nombre_idioma, max_pag.num_paginas from
                idioma join
                (select id, titulo, id_idioma, num_paginas from libro
                where (id_idioma, num_paginas) in
                (select id_idioma, max(num_paginas) from libro
                group by id_idioma)) max_pag on (idioma.id = max_pag.id_idioma)"""

def diez_con_mas_votantes():
    return  """
            SELECT titulo, num_votantes_libro
            FROM libro
            ORDER BY num_votantes_libro DESC
            LIMIT 10;
            """

def diez_mas_populares_ranking():
    return  """
            SELECT titulo ,ranking
            FROM libro
            WHERE num_votantes_libro>1000
            ORDER BY ranking DESC
            LIMIT 10
            """

def diez_mas_comentados():
    return  """SELECT titulo, num_comentarios
            FROM libro
            ORDER BY num_comentarios DESC
            LIMIT 10;"""

def mejores_editoriales():
    return   """SELECT nombre_editorial, ranking FROM (SELECT * FROM editorial NATURAL JOIN (SELECT nombre_editorial FROM (
                	SELECT COUNT(ed.id) as cuenta, ed.nombre_editorial
                	FROM libro lib JOIN editorial ed ON(ed.id = lib.id_editorial)
                	GROUP BY ed.nombre_editorial) h
                WHERE cuenta > 10) ld) edi NATURAL JOIN (SELECT nombre_editorial, AVG(ranking)::real as ranking
                FROM (SELECT * FROM libro WHERE ranking > 0) l JOIN editorial e ON(l.id_editorial = e.id)
                GROUP BY nombre_editorial
                ORDER BY ranking DESC) ld
                LIMIT 10"""

def mas_proliferas_por_votos():
    return  """SELECT DISTINCT id_editorial, titulo, nombre_editorial, SUM(num_votantes_libro) as num_votantes
            FROM libro NATURAL JOIN editorial
            GROUP BY id_editorial, ranking, titulo, nombre_editorial
            ORDER BY num_votantes DESC
            Limit 10"""

def mas_proliferas_por_comentarios():
    return  """SELECT DISTINCT id_editorial, titulo, nombre_editorial, SUM(num_comentarios) as numero_comentarios
            FROM libro NATURAL JOIN editorial
            GROUP BY id_editorial, ranking, titulo, nombre_editorial
            ORDER BY numero_comentarios DESC
            Limit 10"""

def mejores_autores_por_calificacion():
    return  """SELECT AVG(ranking) ranking_autor,nombre, count(titulo) numero_libros
            FROM libro INNER JOIN autor_libro ON libro.id=autor_libro.id_libro INNER JOIN autor ON id_autor=autor.id
            group by autor,nombre
            HAVING count(titulo)>3
            ORDER BY ranking_autor DESC
            Limit 10"""

def autores_mas_famosos_comentarios():
    return """SELECT SUM(num_comentarios) comentarios, nombre, count(titulo) numero_libros
            FROM libro INNER JOIN autor_libro ON libro.id=autor_libro.id_libro INNER JOIN autor ON id_autor=autor.id
            group by autor,nombre
            ORDER BY comentarios DESC
            Limit 10"""

def autores_mas_famosos_por_num_votantes():
    return  """SELECT SUM(num_votantes_libro) num_votantes, nombre, count(titulo) numero_libros
            FROM libro INNER JOIN autor_libro ON libro.id=autor_libro.id_libro INNER JOIN autor ON id_autor=autor.id
            group by autor,nombre
            ORDER BY num_votantes DESC LIMIT 10"""

def buscar_libro_por_titulo(frase):
    return """select distinct * from libro
              where titulo like '{0}%' limit 10;
           """.format(frase)
