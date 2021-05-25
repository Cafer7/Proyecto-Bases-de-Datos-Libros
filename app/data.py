from title import *
external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Análisis de Goodreads"
#libros
libros_votados = crear_fila_columna_fig(titulo1="10 Libros mas votados", fig1=figBarLibros_10mvotados, id1="10Libros+Votados")
libros_rankeados = crear_fila_columna_fig(titulo2="10 Libros mejor Rankeados",fig2=figBarLibros_10mvotados_1000votos,id2="10Libros+Rankeados")
libros_comentados = crear_fila_columna_fig(titulo1="10 Libros mas comentados",fig1=figBardiez_mas_comentados,id1="10Libros+comentados")
figuras_libros = [libros_votados, libros_comentados, libros_rankeados]

#Editoriales
editores_votados = crear_fila_columna_fig(titulo1="Mejores editoriales por votos",fig1=figBarEditoriales_proliferasvotos,id1="Editoriales_pvotos")
editores_rankeados = crear_fila_columna_fig(titulo2="10 Mejores editoriales por ranking",fig2=figBarmejores_editoriales_por_ranking,id2="10Mejoreseditoriales")
editores_comentados = crear_fila_columna_fig(titulo2="Mejores editoriales por comentarios",fig2=figBarEditoriales_proliferascomentarios,id2="Editoriales_pcoments")
figuras_editoriales = [editores_votados, editores_comentados, editores_rankeados]

#Autores
autores_votados = crear_fila_columna_fig(titulo1="Autores mas famosos por votantes de sus libros",fig1=figBarautores_mas_famosos_por_num_votantes,id1="mejoresautoresporvotantes",)
autores_rankeados = crear_fila_columna_fig(titulo2="Mejores autores segun la calificacion de sus libros",fig2=figBarmejores_autores_por_calificacion,id2="mejoresautoresporcalificacion")
autores_comentados = crear_fila_columna_fig(titulo1="Autores famosos segun el numero de comentarios",fig1=figBarautores_mas_famosos_comentarios,id1="Autoresfamososcomentarios")
figuras_autores = [autores_votados, autores_comentados, autores_rankeados]
#Layout
app.layout = html.Div(className="container-fluid", style={"overflow": "hidden"},children=[
    app_bar(),
    html.Div(id='lista_buscados',),
    html.Div(className="container-fluid", children=[
        #Libros
        html.H2(children="Libros"),
        dcc.Tabs([
            dcc.Tab(label="Votos", children=[figuras_libros[0]]),
            dcc.Tab(label="Comentarios", children=[figuras_libros[1]]),
            dcc.Tab(label="Ranking", children=[figuras_libros[2]])
        ]
        ),
        #Editoriales
        html.H2(children="Editoriales"),
        dcc.Tabs([
            dcc.Tab(label="Votos", children=[figuras_editoriales[0]]),
            dcc.Tab(label="Comentarios", children=[figuras_editoriales[1]]),
            dcc.Tab(label="Ranking", children=[figuras_editoriales[2]])
        ]
        ),

        #Autores
        html.H2(children="Autores"),
        dcc.Tabs([
            dcc.Tab(label="Votos", children=[figuras_autores[0]]),
            dcc.Tab(label="Comentarios", children=[figuras_autores[1]]),
            dcc.Tab(label="Ranking", children=[figuras_autores[2]])
        ]
        ),
        #Idiomas
        html.H2(children="Idiomas"),
        crear_fila_columna_fig(
        titulo2="Porcentaje de idiomas en la base de datos",
        fig2=fignumero_libros_por_idiomas,
        id2="piedemanzana"
        )
    ]),
])

#Se actualiza el html cada vez que se ingresa un valor en la barra de busqueda
@app.callback(
    Output("lista_buscados", "children"),
    Input("input_search", "value"),
)
#Se ejecuta la sentencia segun lo que este en la barra de busqueda
def cb_render(*vals):
    if vals[0] != None and vals[0] != "":
        busquedas = []
        con.openConnection()
        busqueda = pd.read_sql_query(buscar_libro_por_titulo(vals[0].lower()), con.connection)
        con.closeConnection()
        df_busqueda = pd.DataFrame(busqueda, columns=["Libro","Numero de paginas"])
        table = dbc.Table.from_dataframe(df_busqueda, striped=True, bordered=True, hover=False)
        busquedas = df_busqueda.astype(str).values.tolist()
        return table
    else:
        return [""]
