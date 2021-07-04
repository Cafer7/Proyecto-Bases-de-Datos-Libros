
copy idioma from program 'curl "https://raw.githubusercontent.com/Cafer7/Proyecto-Bases-de-Datos-Libros/master/tablas/idioma.csv"' delimiter ',' encoding 'UTF-8' CSV HEADER;

copy editorial from program 'curl "https://raw.githubusercontent.com/Cafer7/Proyecto-Bases-de-Datos-Libros/master/tablas/editoriales.csv"' delimiter ',' encoding 'UTF-8' CSV HEADER;

copy autor from program 'curl "https://raw.githubusercontent.com/Cafer7/Proyecto-Bases-de-Datos-Libros/master/tablas/autor.csv"' delimiter ',' encoding 'UTF-8' CSV HEADER;

copy libro from program 'curl "https://raw.githubusercontent.com/Cafer7/Proyecto-Bases-de-Datos-Libros/master/tablas/libros.csv"' delimiter ',' encoding 'UTF-8' CSV HEADER;

copy autor_libro from program 'curl "https://raw.githubusercontent.com/Cafer7/Proyecto-Bases-de-Datos-Libros/master/tablas/libro_autor.csv"' delimiter ',' encoding 'UTF-8' CSV HEADER;

/*-------------------------*/

-- select * from autor;
-- select * from idioma;
-- select * from libro;
-- select * from editorial;
-- select * from autor_libro;

