<<<<<<< HEAD
--Agregar direccion de las tablas
set datestyle = mdy;
Copy autor from 'autor.csv' delimiter ',' CSV HEADER;
Copy editorial from 'editoriales.csv' delimiter ',' CSV HEADER;
Copy idioma from 'idioma.csv' delimiter ',' CSV HEADER;
Copy libro from 'libross.csv' delimiter ',' CSV HEADER;
Copy autor_libro from 'libro_autor.csv' delimiter ',' CSV HEADER;
=======
Copy autor(nombre) from 'C:\Sobrecarga Postgres\autor.csv' delimiter ',' CSV HEADER;
Copy editorial(nombre_editorial) from 'C:\Sobrecarga Postgres\editoriales.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
Copy idioma from 'C:\Sobrecarga Postgres\idioma.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
Copy libro(titulo, fecha_publicacion, num_paginas, ranking, num_votantes_libro, num_comentarios, Id_idioma,Id_editorial) from 'C:\Sobrecarga Postgres\librosss.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
Copy autor_libro from 'C:\Sobrecarga Postgres\libro_autor.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;

select * from autor
select * from idioma
select * from libro
select * from editorial

ALTER SEQUENCE autor_id_seq RESTART WITH 1;
ALTER SEQUENCE editorial_id_seq RESTART WITH 1;
ALTER SEQUENCE libro_id_seq RESTART WITH 1;


delete from editorial



