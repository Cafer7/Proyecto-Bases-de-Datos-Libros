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
	"Id" serial NOT NULL,
	titulo varchar,
	"fecha_publicación" date,
	"num_páginas" smallint,
	ranking double precision,
	num_votantes_libro smallint,
	num_comentarios smallint,
	"Id_idioma" char(4) NOT NULL,
	"Id_editorial" integer NOT NULL,
	CONSTRAINT "Libro_pk" PRIMARY KEY ("Id")

);
-- ddl-end --
-- ALTER TABLE public.libro OWNER TO postgres;
-- ddl-end --

-- object: public.autor | type: TABLE --
-- DROP TABLE IF EXISTS public.autor CASCADE;
CREATE TABLE public.autor (
	"Id" serial NOT NULL,
	nombre varchar,
	CONSTRAINT "Autor_pk" PRIMARY KEY ("Id")

);
-- ddl-end --
-- ALTER TABLE public.autor OWNER TO postgres;
-- ddl-end --

-- object: public.autor_libro | type: TABLE --
-- DROP TABLE IF EXISTS public.autor_libro CASCADE;
CREATE TABLE public.autor_libro (
	"Id_autor" integer NOT NULL,
	"Id_libro" integer NOT NULL
);
-- ddl-end --
-- ALTER TABLE public.autor_libro OWNER TO postgres;
-- ddl-end --

-- object: public.editorial | type: TABLE --
-- DROP TABLE IF EXISTS public.editorial CASCADE;
CREATE TABLE public.editorial (
	"Id" serial NOT NULL,
	nombre_editorial varchar,
	CONSTRAINT "Editorial_pk" PRIMARY KEY ("Id")

);
-- ddl-end --
-- ALTER TABLE public.editorial OWNER TO postgres;
-- ddl-end --

-- object: public.idioma | type: TABLE --
-- DROP TABLE IF EXISTS public.idioma CASCADE;
CREATE TABLE public.idioma (
	"Id" char(4) NOT NULL,
	nombre_idioma char(20),
	CONSTRAINT "Idioma_pk" PRIMARY KEY ("Id")

);
-- ddl-end --
-- ALTER TABLE public.idioma OWNER TO postgres;
-- ddl-end --

-- object: idioma_fk | type: CONSTRAINT --
-- ALTER TABLE public.libro DROP CONSTRAINT IF EXISTS idioma_fk CASCADE;
ALTER TABLE public.libro ADD CONSTRAINT idioma_fk FOREIGN KEY ("Id_idioma")
REFERENCES public.idioma ("Id") MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: editorial_fk | type: CONSTRAINT --
-- ALTER TABLE public.libro DROP CONSTRAINT IF EXISTS editorial_fk CASCADE;
ALTER TABLE public.libro ADD CONSTRAINT editorial_fk FOREIGN KEY ("Id_editorial")
REFERENCES public.editorial ("Id") MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: autor_fk | type: CONSTRAINT --
-- ALTER TABLE public.autor_libro DROP CONSTRAINT IF EXISTS autor_fk CASCADE;
ALTER TABLE public.autor_libro ADD CONSTRAINT autor_fk FOREIGN KEY ("Id_autor")
REFERENCES public.autor ("Id") MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: libro_fk | type: CONSTRAINT --
-- ALTER TABLE public.autor_libro DROP CONSTRAINT IF EXISTS libro_fk CASCADE;
ALTER TABLE public.autor_libro ADD CONSTRAINT libro_fk FOREIGN KEY ("Id_libro")
REFERENCES public.libro ("Id") MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --


