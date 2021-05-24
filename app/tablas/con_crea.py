from .Modulos import *
import getpass
import psycopg2
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

class Connection:
    def __init__(self, usuario="postgres", contra="linux123", puerto="5432"):
        self.user = usuario
        self.password = contra
        self.port = puerto
        self.connection = None
    def openConnection(self):
        try:
            self.connection = psycopg2.connect(host="localhost",port=self.port,dbname="proyecto",user=self.user,password=self.password)
        except Exception as e:
            print (e)

    def closeConnection(self):
        self.connection.close()
###############################################################################
#Conexión a la base de datos
user = input("Ingrese usuario: \n")
password = getpass.getpass("Ingrese su clave:\n")
port = input("Ingrese el puuerto: \n")
con = Connection()
con.openConnection()
print("Creando Tablas...")
tabla_libro = pd.read_sql_query(leer_tabla_libro(), con.connection)
tabla_autor = pd.read_sql_query(leer_tabla_autor(), con.connection)
tabla_autor_libro = pd.read_sql_query(leer_tabla_autor_libro(), con.connection)
tabla_idioma = pd.read_sql_query(leer_tabla_idioma(), con.connection)
tabla_editorial = pd.read_sql_query(leer_tabla_editorial(), con.connection)

tabla_pa_num_pa = pd.read_sql_query(obtener_libros_con_max_pag_idioma(), con.connection)
###############################################################################
#Creando DataFrame de cada tabla
df_tabla_libro = pd.DataFrame(tabla_libro, columns=["id","titulo","fecha_publicación","num_páginas","ranking","num_votantes_libro","num_comentarios","id_idioma","id_editorial"])
df_tabla_autor = pd.DataFrame(tabla_autor, columns=["id", "nombre"])
df_tabla_autor_libro = pd.DataFrame(tabla_autor_libro, columns=["id_autor","id_libro"])
df_tabla_idioma = pd.DataFrame(tabla_idioma, columns=["id","nombre_idioma"])
df_tabla_editorial = pd.DataFrame(tabla_editorial, columns=["id","nombre_editorial"])
df_tabla_pa_num_pa = pd.DataFrame(tabla_pa_num_pa)

 #Rating y numero de votantes para saber cuales son los lbros más populares

query = pd.read_sql_query(diez_con_mas_votantes(), con.connection)
dfLibros_10mvotados = pd.DataFrame(query, columns=["titulo", "num_votantes_libro"])
figBarLibros_10mvotados = px.bar(dfLibros_10mvotados.head(20), x="titulo", y="num_votantes_libro")

#10 + populares con + de 1000 votos

query = pd.read_sql_query(diez_mas_populares_ranking(), con.connection)
dfLibros_10mvotados_1000votos = pd.DataFrame(query, columns=["titulo", "ranking"])
figBarLibros_10mvotados_1000votos = px.bar(dfLibros_10mvotados_1000votos.head(20), x="titulo", y="ranking")

#10 libros diez_mas_comentados
query = pd.read_sql_query(diez_mas_comentados(), con.connection)
dfdiez_mas_comentados = pd.DataFrame(query, columns=["titulo", "num_comentarios"])
figBardiez_mas_comentados = px.bar(dfdiez_mas_comentados.head(20), x="titulo", y="num_comentarios")

 #Mejores editoriales por calificacion de los libros.

query = pd.read_sql_query(mejores_editoriales_por_ranking(), con.connection)
dfmejores_editoriales_por_ranking = pd.DataFrame(query, columns=["nombre_editorial", "ranking"])
figBarmejores_editoriales_por_ranking  = px.bar(dfmejores_editoriales_por_ranking .head(20), x="nombre_editorial", y="ranking")

 #Editoriales más prolifereas por votos

query = pd.read_sql_query(mas_proliferas_por_votos(), con.connection)
dfEditoriales_proliferasvotos = pd.DataFrame(query, columns=["nombre_editorial", "num_votantes"])
figBarEditoriales_proliferasvotos= px.bar(dfEditoriales_proliferasvotos.head(20), x="nombre_editorial", y="num_votantes")

#Editoriales mas proliferas por comentarios

query = pd.read_sql_query(mas_proliferas_por_comentarios(), con.connection)
dfEditoriales_proliferascomentarios = pd.DataFrame(query, columns=["nombre_editorial", "numero_comentarios"])
figBarEditoriales_proliferascomentarios= px.bar(dfEditoriales_proliferascomentarios.head(20), x="nombre_editorial", y="numero_comentarios")

#Mejores autores por calificacion

query = pd.read_sql_query(mejores_autores_por_calificacion(), con.connection)
dfmejores_autores_por_calificacion = pd.DataFrame(query, columns=["nombre", "ranking_autor"])
figBarmejores_autores_por_calificacion= px.bar(dfmejores_autores_por_calificacion.head(20), x="nombre", y="ranking_autor")

#Autores mas famosos por comentarios

query = pd.read_sql_query(autores_mas_famosos_comentarios(), con.connection)
dfautores_mas_famosos_comentarios = pd.DataFrame(query, columns=["nombre", "comentarios"])
figBarautores_mas_famosos_comentarios= px.bar(dfautores_mas_famosos_comentarios.head(20), x="nombre", y="comentarios")

#Autores mas famosos por numero de votantes

query = pd.read_sql_query(autores_mas_famosos_por_num_votantes(), con.connection)
dfautores_mas_famosos_por_num_votantes = pd.DataFrame(query, columns=["nombre", "num_votantes"])
figBarautores_mas_famosos_por_num_votantes= px.bar(dfautores_mas_famosos_por_num_votantes.head(20), x="nombre", y="num_votantes")
#para crear scatterplot
# fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp",
# 	         size="pop", color="continent",
#                  hover_name="country", log_x=True, size_max=60)
# numero de Libros por idioma
query = pd.read_sql_query(cantidad_libros_por_idioma(), con.connection)
dfnumero_libros_por_idiomas = pd.DataFrame(query, columns=["idioma", "total"])
fignumero_libros_por_idiomas= px.pie(dfnumero_libros_por_idiomas.head(20), values="total", names="idioma").update_traces(textposition='inside', textinfo='percent+label')


con.closeConnection()

def crear_fila_columna_fig(titulo1 = None, fig1 = None, id1 = None, titulo2 = None, fig2 = None, id2 = None):
    if (titulo1 != None and titulo2 != None):
        return html.Div(className="row", children=[
                    html.Div(className="col-12 col-xl-6", children=[
                        html.Div(className="card border-info", children=[
                            html.Div(className="card-header bg-info text-light", children=[
                                html.H3(children= titulo1),
                            ]),
                            html.Div(className="card-body", children=[
                                dcc.Graph(
                                    style={'color': 'green', 'fontSize': 14, 'height':'500px'},
                                    id=id1,
                                    figure  = fig1
                                ),
                            ]),
                        ]),
                    ]),
                    html.Div(className="col-12 col-xl-6", children=[
                        html.Div(className="card border-info", children=[
                            html.Div(className="card-header bg-info text-light", children=[
                                html.H3(children= titulo2),
                            ]),
                            html.Div(className="card-body", children=[
                                dcc.Graph(
                                    style={'color': 'green', 'fontSize': 14, 'height':'500px'},
                                    id=id2,
                                    figure  = fig2
                                ),
                            ]),
                        ]),
                    ]),
                ])
    elif (titulo1 != None and titulo2 == None):
        return  html.Div(className="row", children=[
                    html.Div(className="col-12", children=[
                        html.Div(className="card border-info", children=[
                            html.Div(className="card-header bg-info text-light", children=[
                                html.H3(children= titulo1),
                            ]),
                            html.Div(className="card-body", children=[
                                dcc.Graph(
                                    style={'color': 'green', 'fontSize': 14, 'height':'500px'},
                                    id=id1,
                                    figure  = fig1
                                ),
                            ]),
                        ]),
                    ]),
                ])
    elif (titulo2 != None and titulo1 == None):
        return  html.Div(className="row", children=[
                    html.Div(className="col-12", children=[
                        html.Div(className="card border-info", children=[
                            html.Div(className="card-header bg-info text-light", children=[
                                html.H3(children= titulo2),
                            ]),
                            html.Div(
                                className="card-body",
                                children=[
                                dcc.Graph(
                                    style={'color': 'green', 'fontSize': 14, 'height':'500px'},
                                    id=id2,
                                    figure  = fig2
                                ),
                            ]),
                        ]),
                    ]),
                ],)
    else:
        return html.H1("Uoops, error")
