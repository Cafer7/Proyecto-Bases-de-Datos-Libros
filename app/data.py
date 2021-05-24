from title import *
external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#Layout
app.layout = html.Div(children=[
    app_bar(),
    html.Div(id='Container',),
    html.Div(className="container-fluid", children=[
        #fila 1
        crear_fila_columna_fig(
            titulo1="10 Libros mas votados",
            fig1=figBarLibros_10mvotados,
            id1="10Libros+Votados",
            titulo2="10 Libros mejor Rankeados",
            fig2=figBarLibros_10mvotados_1000votos,
            id2="10Libros+Rankeados"
        ),
        #Fila2
        crear_fila_columna_fig(
            titulo1="10 Libros mas comentados",
            fig1=figBardiez_mas_comentados,
            id1="10Libros+comentados",
            titulo2="10 Mejores editoriales por ranking",
            fig2=figBarmejores_editoriales_por_ranking,
            id2="10Mejoreseditoriales"
        ),
        #Fila3
        crear_fila_columna_fig(
            titulo1="Mejores editoriales por votos",
            fig1=figBarEditoriales_proliferasvotos,
            id1="Editoriales_pvotos",
            titulo2="Mejores editoriales por comentarios",
            fig2=figBarEditoriales_proliferascomentarios,
            id2="Editoriales_pcoments"
        ),
        #Fila4
        crear_fila_columna_fig(
            titulo1="Autores famosos segun el numero de comentarios",
            fig1=figBarautores_mas_famosos_comentarios,
            id1="Autoresfamososcomentarios",
            titulo2="Mejores autores segun la calificacion de sus libros",
            fig2=figBarmejores_autores_por_calificacion,
            id2="mejoresautoresporcalificacion"
        ),
        #Fila5
        crear_fila_columna_fig(
            titulo1="Autores mas famosos por votantes de sus libros",
            fig1=figBarautores_mas_famosos_por_num_votantes,
            id1="mejoresautoresporvotantes",
        ),
        #fila 6
        crear_fila_columna_fig(
        titulo2="Porcentaje de idiomas en la base de datos",
        fig2=fignumero_libros_por_idiomas,
        id2="piedemanzana"
        )
    ]),
])

@app.callback(
    Output("Container", "children"),
    Input("input_search", "value"),
)

def cb_render(*vals):
    if vals[0] != None and vals[0] != "":
        busquedas = []
        con.openConnection()
        busqueda = pd.read_sql_query(buscar_libro_por_titulo(vals[0].lower()), con.connection)
        con.closeConnection()
        df_busqueda = pd.DataFrame(busqueda, columns=["libro","autor"])
        table = dbc.Table.from_dataframe(df_busqueda, striped=True, bordered=True, hover=False)
        busquedas = df_busqueda.astype(str).values.tolist()
        return table
        # return html.Ul(children=[html.Li(i) for i in busquedas])
    else:
        return [""]
