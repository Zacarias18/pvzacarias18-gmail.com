# pvzacarias18-gmail.com
PROYECTO RESTAURANTE
Unimar
Programación II

Integrantes:
Javismar Brito
Silvanna Rojas
Patricia Zacarias
	
NOTA: LA LIBRERIA <Tkinter> ES COMPLETAMENTE NECESARIA PARA LA INTERFAZ. LA VERSION DE PYTHON ES LA 2.7.

El proyecto tiene como empresa un restaurante, en donde existen dos tipos de usuario; administrador y cliente.
Asi pues, al iniciar el programa, ejecuta la funcion "ventana_principal" y a partir de esa funcion se procesan
todas las demas, explicadas a continuacion:

- LOGIN:
	El inicio de sesion es para Administrador o cualquier persona que desee registrarse,
  en caso de no estar registrado, el programa no avanzara de esa ventana. 
	Tiene 2 botones los cuales son: Iniciar sesion y registrar un nuevo usuario. 
	Si deja los espacios de "Usuario y contraseña" vacios se mostrara un mensaje solicitando que los llene.

- REGISTRAR USUARIO:
	Al presionar el boton de "registrar usuario", se abre una ventana un poco más pequeña, donde se solicita
  el usuario que desea registrar y la contraseña.
	Luego de llenar los campos, se crea un un archivo con el nombre del usuario que registro y dentro va a
  contener la contraseña de dicho usuario.

- MENU DE ADMINISTRADOR:
	Al entrar como "Administrador" con la contraseña "admin" por defecto se abrira un menu con 3 opciones,
  las cuales seran; "Ver menu, modificar precios y Ver las ventas realizadas":

	1.- Ver menu: 
		Mostrara el menu de la semana, que consta de 3 platos diferentes y podra elegir uno de ellos, al
    seleccionarlo, se abrira una ventana donde se muestra la informacion de cada plato, con su respectivo precio.

	2.- Modificar precios:
		Permitira cambiar el precios de cualquiera de los 3 platos, cabe destacar que < AL INICIAR EL PROGRAMA POR
    PRIMERA VEZ ES NECESARIO DARLE PRECIO A LOS PLATOS DISPONIBLES > ya que iniciaran sin precio. 
		Sera solo la primera vez, porque al darle precios, se crean archivos para cada plato con su correspondiente
    precio, que puede ser modificado desde el usuario de Administrador.

	3.- Ver las ventas realizadas:
		En esta ventana, se mostrara una lista de ventas que han sido procesadas, las cuales mostraran; la comida,
    el precio y la cantidad.

- MENU DE USUARIO:
	Solo muestra UNA opcion y es la de "Ver menu", para solicitar sus pedidos.
