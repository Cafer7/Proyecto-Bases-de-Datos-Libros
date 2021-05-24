from tablas.con_crea import *
def app_bar():
    return  dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        html.H1(children = "Análisis de Goodreads", className = "text-center"),
                    ),
                    width=7
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
                    width=3
                ),
            ],
            justify="between",
        )
