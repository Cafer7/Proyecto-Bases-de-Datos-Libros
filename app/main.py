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

con.closeConnection()
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
print(df_tabla_autor)
# print(df_tabla_editorial)
# print(df_tabla_autor_libro)
# print(df_tabla_idioma)

print(df_tabla_pa_num_pa)
###############################################################################
 #Rating y numero de votantes para saber cuales son los lbros más populares

 #Mejores editoriales por califacion de los libros.

 #Editoriales más prolifereas

 #Mejores autores

 
