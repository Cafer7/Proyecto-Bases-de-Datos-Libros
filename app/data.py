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
            titulo1="10Libros+Votados",
            fig1=figBarLibros_10mvotados,
            id1="10Libros+Votados",
            titulo2="10Libros+Rankeados",
            fig2=figBarLibros_10mvotados_1000votos,
            id2="10Libros+Rankeados"
        ),
        #Fila2
        crear_fila_columna_fig(
            titulo1="10Libros+comentados",
            fig1=figBardiez_mas_comentados,
            id1="10Libros+comentados",
            titulo2="10Mejoreseditoriales",
            fig2=figBarMejores_editoriales,
            id2="10Mejoreseditoriales"
        ),
        #Fila3
        crear_fila_columna_fig(
            titulo1="Editoriales_pvotos",
            fig1=figBarEditoriales_proliferasvotos,
            id1="Editoriales_pvotos",
            titulo2="Editoriales_pcoments",
            fig2=figBarEditoriales_proliferascomentarios,
            id2="Editoriales_pcoments"
        ),
        #Fila4
        crear_fila_columna_fig(
            titulo1="Autoresfamososcomentarios",
            fig1=figBarautores_mas_famosos_comentarios,
            id1="Autoresfamososcomentarios",
            titulo2="mejoresautoresporcalificacion",
            fig2=figBarmejores_autores_por_calificacion,
            id2="mejoresautoresporcalificacion"
        ),
        #Fila5
        crear_fila_columna_fig(
            titulo1="Mejores Autores Por Votantes",
            fig1=figBarautores_mas_famosos_por_num_votantes,
            id1="mejoresautoresporvotantes"
        )
    ]),
])

@app.callback(
    Output("Container", "children"),
    Input("input_search", "value"),
)


