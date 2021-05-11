/* ======= Agregar direccion de las tablas (windows)*/
/*correr una por una, reiniciar secuencias cada vez que se inserte una tabla*/
Copy autor(nombre) from 'C:\autor.csv' delimiter ',' CSV HEADER;
ALTER SEQUENCE autor_id_seq RESTART WITH 1;
ALTER SEQUENCE editorial_id_seq RESTART WITH 1;
ALTER SEQUENCE libro_id_seq RESTART WITH 1;
/*-------------------------*/
Copy editorial(nombre_editorial) from 'C:\editoriales.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
ALTER SEQUENCE autor_id_seq RESTART WITH 1;
ALTER SEQUENCE editorial_id_seq RESTART WITH 1;
ALTER SEQUENCE libro_id_seq RESTART WITH 1;
/*-------------------------*/
Copy idioma from 'C:\idioma.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
ALTER SEQUENCE autor_id_seq RESTART WITH 1;
ALTER SEQUENCE editorial_id_seq RESTART WITH 1;
ALTER SEQUENCE libro_id_seq RESTART WITH 1;
/*-------------------------*/
set datestyle = mdy;
Copy libro(titulo, fecha_publicacion, num_paginas, ranking, num_votantes_libro, num_comentarios, Id_idioma,Id_editorial) from 'C:\libros.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
ALTER SEQUENCE autor_id_seq RESTART WITH 1;
ALTER SEQUENCE editorial_id_seq RESTART WITH 1;
ALTER SEQUENCE libro_id_seq RESTART WITH 1;
/*-------------------------*/
Copy autor_libro from 'C:\libro_autor.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
/*-------------------------*/
select * from autor
select * from idioma
select * from libro
select * from editorial




delete from editorial