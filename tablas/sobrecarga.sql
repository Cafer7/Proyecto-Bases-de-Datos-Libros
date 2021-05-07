--Agregar direccion de las tablas
set datestyle = mdy;
Copy autor from 'autor.csv' delimiter ',' CSV HEADER;
Copy editorial from 'editoriales.csv' delimiter ',' CSV HEADER;
Copy idioma from 'idioma.csv' delimiter ',' CSV HEADER;
Copy libro from 'libross.csv' delimiter ',' CSV HEADER;
Copy autor_libro from 'libro_autor.csv' delimiter ',' CSV HEADER;

