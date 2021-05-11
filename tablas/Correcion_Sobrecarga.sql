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
SELECT DISTINCT id_editorial, titulo, nombre_editorial, AVG(ranking)::real as prom_salario 
FROM libro NATURAL JOIN editorial
GROUP BY id_editorial, ranking, titulo, nombre_editorial
ORDER BY nombre_editorial DESC
/* mas proliferas */
SELECT DISTINCT id_editorial, titulo, nombre_editorial, SUM(num_votantes_libro) as num_votantes
FROM libro NATURAL JOIN editorial
GROUP BY id_editorial, ranking, titulo, nombre_editorial
ORDER BY num_votantes DESC
/* mejores autores */

