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
################################################################################
#Creando diagramas de barras y mapas
#Que país publica más libros

# figBarCases = px.bar(df_tabla_libro.head(20), x="country", y="amount")
# figMapCases = px.choropleth(df_tabla_libro, locations="country",
# locationmode="country names",
# color="amount",
# hover_name="country",
# color_continuous_scale=["#99ccff", "#ff3333"])
#
# figBarCases = px.bar(df_tabla_autor.head(20), x="country", y="amount")
#
# figBarCases = px.bar(df_tabla_autor_libro.head(20), x="country", y="amount")
#
# figBarCases = px.bar(df_tabla_idioma.head(20), x="country", y="amount")
#
# figBarCases = px.bar(df_tabla_editorial.head(20), x="country", y="amount")


###############################################################################

###############################################################################
#consultas a las tablas
# print(df_tabla_libro)
#print(df_tabla_autor)
# print(df_tabla_editorial)
# print(df_tabla_autor_libro)
# print(df_tabla_idioma)

#print(df_tabla_pa_num_pa)
###############################################################################

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
print("sdjkgfjasdfhlsdjfjlsdhfjlsdhfjksdhfljsdhfjkdshljkdhlfkjdsjfkdsjkflasdlfjkhdsjklfhdsjkfhdasjhdflsjh")
query = pd.read_sql_query(diez_mas_populares_ranking(), con.connection)
dfdiez_mas_comentados = pd.DataFrame(query, columns=["titulo", "num_comentarios"])
print(dfdiez_mas_comentados)
figBardiez_mas_comentados = px.bar(dfdiez_mas_comentados.head(20), x="titulo", y="num_comentarios")

 #Mejores editoriales por califacion de los libros.

query = pd.read_sql_query(mejores_editoriales(), con.connection)
dfMejores_editoriales = pd.DataFrame(query, columns=["nombre_editorial", "ranking"])
print(dfMejores_editoriales)
figBarMejores_editoriales = px.bar(dfMejores_editoriales.head(20), x="nombre_editorial", y="ranking")


 #Editoriales más prolifereas

query = pd.read_sql_query(mas_proliferas_por_votos(), con.connection)
dfEditoriales_proliferas = pd.DataFrame(query, columns=["nombre_editorial", "num_votantes"])
print(dfEditoriales_proliferas)
figBarEditoriales_proliferas= px.bar(dfEditoriales_proliferas.head(20), x="nombre_editorial", y="num_votantes")







 #Mejores autores





con.closeConnection()
