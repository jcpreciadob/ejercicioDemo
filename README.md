# ejercicioDemo
Ejercicio de Prueba Tecnica


Construcción de la imagen:
--------------------------
docker build -t ejemplo .

--------------------------------
Correr el ejemplo de manera local: 
---------------------------------
docker run -d -p 8000:8000 -v ./app ejemplo

--------------------------------

PARA PROBAR EL APP
------------------
Entrar al navegador a las siguientes direcciones:

1) http://localhost:8000
2) http://localhost:8000/visitors
3) http://localhost:8000/visitor/reset

Para ver las diferentes respuestas del app

PARA DETENER LA IMAGEN
----------------------
docker ps

validar el id de la imagen: Ejemplo: a675dab694ef

Para detener ejecutar: docker stop a675dab694ef