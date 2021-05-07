Copy autor(nombre) from 'C:\Sobrecarga Postgres\autor.csv' delimiter ',' CSV HEADER;
Copy editorial(nombre_editorial) from 'C:\Sobrecarga Postgres\editoriales.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
Copy idioma from 'C:\Sobrecarga Postgres\idioma.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
Copy libro(titulo, fecha_publicacion, num_paginas, ranking, num_votantes_libro, num_comentarios, Id_idioma,Id_editorial) from 'C:\Sobrecarga Postgres\librosss.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
Copy autor_libro from 'C:\Sobrecarga Postgres\libro_autor.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;

select * from autor
select * from idioma
select * from libro
delete from autor

