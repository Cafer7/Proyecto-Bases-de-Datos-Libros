/*10 con mas votantes */
SELECT titulo, num_votantes_libro
FROM libro
ORDER BY num_votantes_libro DESC
LIMIT 10;
/*10 mas populares con mas de 1000 votos*/
SELECT titulo, num_votantes_libro, ranking
FROM libro
WHERE num_votantes_libro>1000
ORDER BY ranking DESC
LIMIT 10;
/*10 mas comentados */
SELECT titulo, num_comentarios
FROM libro
ORDER BY num_comentarios DESC
LIMIT 10;
/* mejores editoriales */
SELECT DISTINCT id_editorial, titulo, nombre_editorial, AVG(ranking)::real as ranking 
FROM libro NATURAL JOIN editorial
GROUP BY id_editorial, ranking, titulo, nombre_editorial

ORDER BY nombre_editorial DESC

/* mas proliferas votos */
SELECT DISTINCT id_editorial, titulo, nombre_editorial, SUM(num_votantes_libro) as num_votantes
FROM libro NATURAL JOIN editorial
GROUP BY id_editorial, ranking, titulo, nombre_editorial
ORDER BY num_votantes DESC
/* mas proliferas comentarios */
SELECT DISTINCT id_editorial, titulo, nombre_editorial, SUM(num_comentarios) as numero_comentarios
FROM libro NATURAL JOIN editorial
GROUP BY id_editorial, ranking, titulo, nombre_editorial
ORDER BY numero_comentarios DESC

/* mejores autores por calificacion*/
SELECT AVG(ranking) ranking_autor,nombre, count(titulo) numero_libros
FROM libro INNER JOIN autor_libro ON libro.id=autor_libro.id_libro INNER JOIN autor ON id_autor=autor.id
group by autor,nombre 
HAVING count(titulo)>3
ORDER BY ranking_autor DESC

/* autores mas famosos comentarios */
SELECT SUM(num_comentarios) n, nombre, count(titulo) numero_libros
FROM libro INNER JOIN autor_libro ON libro.id=autor_libro.id_libro INNER JOIN autor ON id_autor=autor.id
group by autor,nombre 

ORDER BY n DESC

/* autores mas famosos segun numero votantes */
SELECT SUM(num_votantes_libro) n, nombre, count(titulo) numero_libros
FROM libro INNER JOIN autor_libro ON libro.id=autor_libro.id_libro INNER JOIN autor ON id_autor=autor.id
group by autor,nombre 
ORDER BY n DESC






