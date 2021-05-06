Copy autor(nombre) from 'C:\Sobrecarga Postgres\autor.csv' delimiter ',' CSV HEADER;
Copy editorial(editorial) from 'C:\Sobrecarga Postgres\editoriales.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
Copy idioma from 'C:\Sobrecarga Postgres\idioma.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
Copy libro(titulo, fecha_publicacion, num_paginas, ranking, num_votantes, num_comentarios, Id_idioma) from 'C:\Sobrecarga Postgres\libross.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
Copy autor_libro from 'C:\Sobrecarga Postgres\libro_autor.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;

select * from autor

delete from autor

