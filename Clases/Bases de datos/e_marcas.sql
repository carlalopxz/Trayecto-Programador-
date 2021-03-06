#JERCICIO 1
SELECT * FROM marcas;
#EJERCICIO 2
SELECT * FROM categorias;
#EJERCICIO 3
SELECT * FROM productos;
#EJERCICIO 4
SELECT NOMBRE, MODELO,DESCRIPCION,PRECIO,PUNTUACION 
	FROM productos;
#EJERCICIO 5
SELECT NOMBRE,(PRECIO/PUNTUACION)
	FROM productos;
#EJERCICIO 6
SELECT * FROM productos
	WHERE PRECIO < 1000;
#EJERCICIO 7
SELECT * FROM productos
	WHERE NOMBRE = "Wii";
#EJERCICIO 8
SELECT NOMBRE,PRECIO FROM productos
	WHERE PRECIO < 1000 AND PRECIO > 1000;
#EJERCICIO 9
SELECT NOMBRE,PRECIO FROM productos
	WHERE PRECIO < 1000 OR PRECIO > 1000;
#EJERCICIO 10
SELECT NOMBRE, PRECIO,PUNTUACION FROM productos
	WHERE PRECIO >= 1000 AND PRECIO <= 10000 OR PUNTUACION > 4;
#EJERCICIO 11
SELECT NOMBRE FROM clientes 
	ORDER BY NOMBRE ASC;
#EJERCICIO 12
SELECT NOMBRE,APELLIDO FROM clientes
	ORDER BY NOMBRE, APELLIDO ASC;
#EJERCICIO 13
SELECT NOMBRE,APELLIDO,TELEFONO,FECHA_DE_NACIMIENTO FROM clientes
	WHERE TELEFONO IS NOT NULL
	ORDER BY FECHA_DE_NACIMIENTO DESC;
#EJERCICIO 14
SELECT NOMBRE,PUNTUACION FROM productos
	ORDER BY PUNTUACION DESC LIMIT 5;
#EJERCICIO 15
SELECT NOMBRE,PUNTUACION FROM productos
	ORDER BY PUNTUACION DESC LIMIT 10,5;
#EJERCICIO 16
SELECT NOMBRE FROM productos
	WHERE NOMBRE LIKE "IPHONE%";
#EJERCICIO 17
SELECT NOMBRE FROM productos
	WHERE NOMBRE LIKE "%P%";
#EJERCICIO 18
SELECT NOMBRE FROM productos
	WHERE NOMBRE LIKE "%P%P%";
#EJERCICIO 19
SELECT "HOLA MUNDO" FROM clientes;
#EJERCICIO 20
SELECT CONCAT_WS(', ', nombre, apellido) AS NOMBRE_COMPLETO FROM clientes;
#EJERCICIO 21
SELECT * FROM productos,marcas;
#EJERCICIO 22
SELECT productos.NOMBRE,marcas.NOMBRE FROM productos,marcas;
#EJERCICIO 23
SELECT productos.ID, marcas.ID FROM productos,marcas;
#EJERCICIO 24
SELECT PRODUCTOS.NOMBRE, MARCAS.NOMBRE, PRODUCTOS.PUNTUACION, PRODUCTOS.PRECIO FROM PRODUCTOS,MARCAS
	WHERE PUNTUACION > 3
	ORDER BY PRECIO DESC;
#EJERCICIO 25
SELECT CLIENTES.NOMBRE, CLIENTES.APELLIDO,PRODUCTOS.NOMBRE FROM CLIENTES,productos, ventas
	WHERE clientes.id = ventas.id_cliente AND productos.id = ventas.id_producto;
