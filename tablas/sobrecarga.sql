--Agregar direccion de las tablas
set datestyle = mdy;
Copy autor from 'autor.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
Copy editorial from 'editoriales.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
Copy idioma from 'idioma.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
Copy libro from 'libross.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
Copy autor_libro from 'libro_autor.csv' delimiter ',' encoding 'UTF-8' CSV HEADER;
