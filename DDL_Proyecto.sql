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

-- object: public."Libro" | type: TABLE --
-- DROP TABLE IF EXISTS public."Libro" CASCADE;
CREATE TABLE public."Libro" (
	"Id" serial NOT NULL,
	titulo varchar,
	"fecha_publicación" date,
	"num_páginas" smallint,
	ranking smallint,
	num_votantes_libro smallint,
	num_comentarios smallint,
	"Id_Idioma" integer NOT NULL,
	"Id_Editorial" integer NOT NULL,
	CONSTRAINT "Libro_pk" PRIMARY KEY ("Id")

);
-- ddl-end --
-- ALTER TABLE public."Libro" OWNER TO postgres;
-- ddl-end --

-- object: public."Autor" | type: TABLE --
-- DROP TABLE IF EXISTS public."Autor" CASCADE;
CREATE TABLE public."Autor" (
	"Id" serial NOT NULL,
	nombre varchar,
	apellido varchar,
	CONSTRAINT "Autor_pk" PRIMARY KEY ("Id")

);
-- ddl-end --
-- ALTER TABLE public."Autor" OWNER TO postgres;
-- ddl-end --

-- object: public."Autor_Libro" | type: TABLE --
-- DROP TABLE IF EXISTS public."Autor_Libro" CASCADE;
CREATE TABLE public."Autor_Libro" (
	"Id_Autor" integer NOT NULL,
	"Id_Libro" integer NOT NULL
);
-- ddl-end --
-- ALTER TABLE public."Autor_Libro" OWNER TO postgres;
-- ddl-end --

-- object: public."Editorial" | type: TABLE --
-- DROP TABLE IF EXISTS public."Editorial" CASCADE;
CREATE TABLE public."Editorial" (
	"Id" serial NOT NULL,
	nombre_editorial smallint,
	CONSTRAINT "Editorial_pk" PRIMARY KEY ("Id")

);
-- ddl-end --
-- ALTER TABLE public."Editorial" OWNER TO postgres;
-- ddl-end --

-- object: public."Idioma" | type: TABLE --
-- DROP TABLE IF EXISTS public."Idioma" CASCADE;
CREATE TABLE public."Idioma" (
	"Id" serial NOT NULL,
	nombre_idioma char(10),
	CONSTRAINT "Idioma_pk" PRIMARY KEY ("Id")

);
-- ddl-end --
-- ALTER TABLE public."Idioma" OWNER TO postgres;
-- ddl-end --

-- object: "Idioma_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Libro" DROP CONSTRAINT IF EXISTS "Idioma_fk" CASCADE;
ALTER TABLE public."Libro" ADD CONSTRAINT "Idioma_fk" FOREIGN KEY ("Id_Idioma")
REFERENCES public."Idioma" ("Id") MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: "Editorial_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Libro" DROP CONSTRAINT IF EXISTS "Editorial_fk" CASCADE;
ALTER TABLE public."Libro" ADD CONSTRAINT "Editorial_fk" FOREIGN KEY ("Id_Editorial")
REFERENCES public."Editorial" ("Id") MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: "Autor_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Autor_Libro" DROP CONSTRAINT IF EXISTS "Autor_fk" CASCADE;
ALTER TABLE public."Autor_Libro" ADD CONSTRAINT "Autor_fk" FOREIGN KEY ("Id_Autor")
REFERENCES public."Autor" ("Id") MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: "Libro_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Autor_Libro" DROP CONSTRAINT IF EXISTS "Libro_fk" CASCADE;
ALTER TABLE public."Autor_Libro" ADD CONSTRAINT "Libro_fk" FOREIGN KEY ("Id_Libro")
REFERENCES public."Libro" ("Id") MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --


