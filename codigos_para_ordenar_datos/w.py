import pandas as pd
import smtplib

#tabla reacion libro_autor
libro_autor = pd.read_csv("tablas/output.csv")
t_libro_autor = libro_autor.to_records(index=False)
tuplas_libro_autor = list(t_libro_autor)

# Tabla autor
autor = pd.read_csv("tablas/autor.csv")
t_autor = autor.to_records(index=False)
tuplas_autor = list(t_autor)
# print(tuplas_autor[0])
# Tabla libro
libro = pd.read_csv("tablas/libros.csv")
t_libro = libro.to_records(index=False)
tuplas_libro = list(t_libro)
print(tuplas_libro[0])


new_libro_autor = []
for relacion in tuplas_libro_autor:
    au = 0
    li = 0
    for a in tuplas_autor:
        if a[1] == relacion[2]:
            au = a[0]
            break

    for l in tuplas_libro:
        if l[1] == relacion[1]:
            li = l[0]
            break
    if ((au != 0) and (li != 0)):
        new_libro_autor.append((li,au))
        print((li,au))

    

df2 = pd.DataFrame(new_libro_autor)
df2.to_csv("tablas/libro_autor.csv", index=False)
