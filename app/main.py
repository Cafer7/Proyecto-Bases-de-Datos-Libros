from Modulos import *

###############################################################################
#Conexión a la base de datos
con = Connection()
con.openConnection()
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
print(dfLibros_10mvotados)
figBarLibros_10mvotados = px.bar(dfLibros_10mvotados.head(20), x="titulo", y="num_votantes_libro")

#10 + populares con + de 1000 votos

query = pd.read_sql_query(diez_mas_populares_ranking(), con.connection)
dfLibros_10mvotados_1000votos = pd.DataFrame(query, columns=["titulo", "ranking"])
print(dfLibros_10mvotados)
figBarLibros_10mvotados_1000votos = px.bar(dfLibros_10mvotados_1000votos.head(20), x="titulo", y="ranking")

#10 libros diez_mas_comentados
query = pd.read_sql_query(diez_mas_comentados(), con.connection)
dfdiez_mas_comentados = pd.DataFrame(query, columns=["titulo", "num_comentarios"])
print(dfdiez_mas_comentados)
figBardiez_mas_comentados = px.bar(dfdiez_mas_comentados.head(20), x="titulo", y="num_comentarios")

 #Mejores editoriales por calificacion de los libros.

query = pd.read_sql_query(mejores_editoriales(), con.connection)
dfMejores_editoriales = pd.DataFrame(query, columns=["nombre_editorial", "ranking"])
print(dfMejores_editoriales)
figBarMejores_editoriales = px.bar(dfMejores_editoriales.head(20), x="nombre_editorial", y="ranking")

 #Editoriales más prolifereas por votos

query = pd.read_sql_query(mas_proliferas_por_votos(), con.connection)
dfEditoriales_proliferasvotos = pd.DataFrame(query, columns=["nombre_editorial", "num_votantes"])
print(dfEditoriales_proliferasvotos)
figBarEditoriales_proliferasvotos= px.bar(dfEditoriales_proliferasvotos.head(20), x="nombre_editorial", y="num_votantes")

#Editoriales mas proliferas por comentarios

query = pd.read_sql_query(mas_proliferas_por_comentarios(), con.connection)
dfEditoriales_proliferascomentarios = pd.DataFrame(query, columns=["nombre_editorial", "numero_comentarios"])
print(dfEditoriales_proliferascomentarios)
figBarEditoriales_proliferascomentarios= px.bar(dfEditoriales_proliferascomentarios.head(20), x="nombre_editorial", y="numero_comentarios")

#Mejores autores por calificacion

query = pd.read_sql_query(mejores_autores_por_calificacion(), con.connection)
dfmejores_autores_por_calificacion = pd.DataFrame(query, columns=["nombre", "ranking_autor"])
print(dfmejores_autores_por_calificacion)
figBarmejores_autores_por_calificacion= px.bar(dfmejores_autores_por_calificacion.head(20), x="nombre", y="ranking_autor")

#Autores mas famosos por comentarios

query = pd.read_sql_query(autores_mas_famosos_comentarios(), con.connection)
dfautores_mas_famosos_comentarios = pd.DataFrame(query, columns=["nombre", "comentarios"])
print(dfautores_mas_famosos_comentarios)
figBarautores_mas_famosos_comentarios= px.bar(dfautores_mas_famosos_comentarios.head(20), x="nombre", y="comentarios")

#Autores mas famosos por numero de votantes

query = pd.read_sql_query(autores_mas_famosos_por_num_votantes(), con.connection)
dfautores_mas_famosos_por_num_votantes = pd.DataFrame(query, columns=["nombre", "num_votantes"])
print(dfautores_mas_famosos_por_num_votantes)
figBarautores_mas_famosos_por_num_votantes= px.bar(dfautores_mas_famosos_por_num_votantes.head(20), x="nombre", y="num_votantes")

con.closeConnection()
ALLOWED_TYPES = (
    "search"
)

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#Layout
app.layout = html.Div(children=[
    html.H1(children = "titulo op", className = "text-center"),
    html.Div(className="container-fluid", children=[
        #fila 1
        html.Div(className="row", children=[
        #columna1
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="10Libros+Votados"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="10Libros+Votados",
                            figure  = figBarLibros_10mvotados
                        ),
                    ]),
                ]),
            ]),
            # columna2
            html.Div(className="col-12 col-xl-5", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="10Libros+Rankeados"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="10Libros+Ranking",
                            figure = figBarLibros_10mvotados_1000votos
                        ),
                    ]),
                ]),
            ]),
        ]),
        #Fila2
        html.Div(className="row", children=[
        #columna1
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="10Libros+comentados"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="10Libros+comentados",
                            figure  = figBardiez_mas_comentados
                        ),
                    ]),
                ]),
            ]),
            # columna2
            html.Div(className="col-12 col-xl-5", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="10Mejoreseditoriales"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="10Mejoreseditoriales",
                            figure = figBarMejores_editoriales
                        ),
                    ]),
                ]),
            ]),
        ]),
        #Fila3
        html.Div(className="row", children=[
            #columna1
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="Editoriales_pvotos"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Editoriales_pvotos",
                            figure  = figBarEditoriales_proliferasvotos
                        ),
                    ]),
                ]),
            ]),
            # columna2
            html.Div(className="col-12 col-xl-5", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="Editoriales_pcoments"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Editoriales_pcoments",
                            figure = figBarEditoriales_proliferascomentarios
                        ),
                    ]),
                ]),
            ]),
        ]),
        #Fila4
        html.Div(className="row", children=[
        #columna1
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="mejoresautoresporcalificacion"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="mejoresautoresporcalificacion",
                            figure  = figBarmejores_autores_por_calificacion
                        ),
                    ]),
                ]),
            ]),
            # columna2
            html.Div(className="col-12 col-xl-5", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="Autoresfamososcomentarios"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="Autoresfamososcomentarios",
                            figure = figBarautores_mas_famosos_comentarios
                        ),
                    ]),
                ]),
            ]),
        ]),
        #Fila5
        html.Div(className="row", children=[
        #columna1
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card border-info", children=[
                    html.Div(className="card-header bg-info text-light", children=[
                        html.H3(children="mejoresautoresporvotantes"),
                    ]),
                    html.Div(className="card-body", children=[
                        dcc.Graph(
                            id="mejoresautoresporvotantes",
                            figure  = figBarautores_mas_famosos_por_num_votantes
                        ),
                    ]),
                ]),
            ]),
        ]),
    ]),
])

if __name__ == "__main__":
    app.run_server(debug=True)
