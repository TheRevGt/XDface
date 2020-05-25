DROP DATABASE IF EXISTS xdface;
CREATE DATABASE xdface;
USE xdface;
SELECT * FROM estudiante;
CREATE TABLE estudiante (nombre VARCHAR(60), facultad VARCHAR(60), carnet INT PRIMARY KEY, edad INT(100));
INSERT INTO estudiante VALUES ( 'Santos Jeremías García Tzul', 'Ingenieria', 151057, 22 );