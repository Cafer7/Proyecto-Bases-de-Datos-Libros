-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.2
-- PostgreSQL version: 12.0
-- Project Site: pgmodeler.io
-- Model Author: ---


-- Database creation must be done outside a multicommand file.
-- These commands were put in this file only as a convenience.
-- -- object: new_database | type: DATABASE --
-- -- DROP DATABASE IF EXISTS new_database;
-- CREATE DATABASE new_database;
-- -- ddl-end --
-- 

-- object: public.libro | type: TABLE --
-- DROP TABLE IF EXISTS public.libro CASCADE;
CREATE TABLE public.libro (
	id serial NOT NULL,
	titulo varchar,
	fecha_publicacion date,
	num_paginas smallint,
	ranking double precision,
	num_votantes_libro bigint,
	num_comentarios bigint,
	"Id_idioma" char(4) NOT NULL,
	id_editorial integer NOT NULL,
	CONSTRAINT "Libro_pk" PRIMARY KEY (id)

);
-- ddl-end --
-- ALTER TABLE public.libro OWNER TO postgres;
-- ddl-end --

-- object: public.autor | type: TABLE --
-- DROP TABLE IF EXISTS public.autor CASCADE;
CREATE TABLE public.autor (
	id serial NOT NULL,
	nombre varchar,
	CONSTRAINT "Autor_pk" PRIMARY KEY (id)

);
-- ddl-end --
-- ALTER TABLE public.autor OWNER TO postgres;
-- ddl-end --

-- object: public.autor_libro | type: TABLE --
-- DROP TABLE IF EXISTS public.autor_libro CASCADE;
CREATE TABLE public.autor_libro (
	id_autor integer NOT NULL,
	id_libro integer NOT NULL
);
-- ddl-end --
-- ALTER TABLE public.autor_libro OWNER TO postgres;
-- ddl-end --

-- object: public.editorial | type: TABLE --
-- DROP TABLE IF EXISTS public.editorial CASCADE;
CREATE TABLE public.editorial (
	id serial NOT NULL,
	nombre_editorial varchar,
	CONSTRAINT "Editorial_pk" PRIMARY KEY (id)

);
-- ddl-end --
-- ALTER TABLE public.editorial OWNER TO postgres;
-- ddl-end --

-- object: public.idioma | type: TABLE --
-- DROP TABLE IF EXISTS public.idioma CASCADE;
CREATE TABLE public.idioma (
	id char(4) NOT NULL,
	nombre_idioma char(20),
	CONSTRAINT "Idioma_pk" PRIMARY KEY (id)

);
-- ddl-end --
-- ALTER TABLE public.idioma OWNER TO postgres;
-- ddl-end --

-- object: idioma_fk | type: CONSTRAINT --
-- ALTER TABLE public.libro DROP CONSTRAINT IF EXISTS idioma_fk CASCADE;
ALTER TABLE public.libro ADD CONSTRAINT idioma_fk FOREIGN KEY ("Id_idioma")
REFERENCES public.idioma (id) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: editorial_fk | type: CONSTRAINT --
-- ALTER TABLE public.libro DROP CONSTRAINT IF EXISTS editorial_fk CASCADE;
ALTER TABLE public.libro ADD CONSTRAINT editorial_fk FOREIGN KEY (id_editorial)
REFERENCES public.editorial (id) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: autor_fk | type: CONSTRAINT --
-- ALTER TABLE public.autor_libro DROP CONSTRAINT IF EXISTS autor_fk CASCADE;
ALTER TABLE public.autor_libro ADD CONSTRAINT autor_fk FOREIGN KEY (id_autor)
REFERENCES public.autor (id) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: libro_fk | type: CONSTRAINT --
-- ALTER TABLE public.autor_libro DROP CONSTRAINT IF EXISTS libro_fk CASCADE;
ALTER TABLE public.autor_libro ADD CONSTRAINT libro_fk FOREIGN KEY (id_libro)
REFERENCES public.libro (id) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --


