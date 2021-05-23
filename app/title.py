from tablas.con_crea import *
def app_bar():
    return  dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        html.H1(children = "titulo op", className = "text-center"),
                    ),
                    width=9
                ),
                dbc.Col(
                    html.Div(
                        html.Center(
                            dcc.Input(
                                id="input_{}".format("search"),
                                type="search",
                                placeholder="Ingrese un titulo",
                            ),
                        ),
                    ),
                    width=2
                ),
            ],
            justify="between",
        )

def cb_render(*vals):
    if vals[0] != None and vals[0] != "":
        busquedas = []
        con.openConnection()
        busqueda = pd.read_sql_query(buscar_libro_por_titulo(vals[0].lower()), con.connection)
        con.closeConnection()
        df_busqueda = pd.DataFrame(busqueda, columns=["titulo"])
        table = dbc.Table.from_dataframe(df_busqueda, striped=True, bordered=True, hover=False)
        busquedas = df_busqueda["titulo"].astype(str).values.tolist()
        return table
        # return html.Ul(children=[html.Li(i) for i in busquedas])
    else:
        return [""]