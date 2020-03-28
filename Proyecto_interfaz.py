from Tkinter import *
import md5
from tkMessageBox import *
from io import open
import os


plato1 = ["Pabellon", 10, 0]
plato2 = ["Cachapa", 5, 0]
plato3 = ["Ensalada", 3, 0]


def ventana_principal():
	global ventana
	ventana = Tk()

	ventana.title("Restaurant...")
	ventana.resizable (width = True, height = False)
	ventana.geometry ("800x600")
	ventana.config (bg= "lightblue")
	 
	 
	global myima
	myima = PhotoImage (file ="12345.gif")
	image = myima.subsample(1,1)
	label= Label(ventana ,image = myima)
	label.place(x = 0, y = 0, relwidth = 1.0, relheight = 1.0)

	global logo
	logo = PhotoImage (file = "logo.gif")
	label1 = Label(ventana, image = logo)
	image = logo.subsample(5,5)
	label1.place(x = 345, y = 60)

def elementos_login():
	global verifica_usuario 
	global verifica_clave

	verifica_usuario = StringVar()
	verifica_clave = StringVar()

	global cuadro_usuario
	global cuadro_password


	usuario = Label (ventana, text = "Usuario:", bg = "white", font = ("Arial", 12))
	usuario.place(x = 390, y = 240)


	
	cuadro_usuario = Entry(ventana)
	cuadro_usuario.place(x = 360, y = 270)


	password = Label (ventana, text = "Contrasena:", bg = "white", font = ("Arial", 12))
	password.place(x = 379, y = 300)

 
	 
	cuadro_password = Entry(ventana)
	cuadro_password.place(x = 360, y = 330)
	cuadro_password.config(show = "*")


	boton_ingresar = Button(ventana, text = "Ingresar", command = codigo_boton_ingresar)
	boton_ingresar.place(x = 394, y = 360)

	boton_registrar = Button(ventana, text = "Registrar un nuevo usuario...", command = codigo_boton_registrar)
	boton_registrar.place(x = 345, y = 400)



def guardarMod():
	datos = cuadroMod.get()

	archivo = open ("Precio pabellon", "wb")
	for datos in datos:
		archivo.write(str(datos))
	archivo.close()

	showinfo (title="Precio modificado", message ="Se ha modificado correctamente. Puede cerrar la ventana")

def guardarModC():
	datos = cuadroMod.get()

	archivo = open ("Precio Cachapa", "wb")
	for datos in datos:
		archivo.write(str(datos))
	archivo.close()

	showinfo (title="Precio modificado", message ="Se ha modificado correctamente. Puede cerrar la ventana")

def guardarModE():
	datos = cuadroMod.get()

	archivo = open ("Precio Ensalada", "wb")
	for datos in datos:
		archivo.write(str(datos))
	archivo.close()

	showinfo (title="Precio modificado", message ="Se ha modificado correctamente. Puede cerrar la ventana")

def modificar_Plato1():
	ventanaMod = Tk()

	ventanaMod.title("Modificar precio: Pabellon")
	ventanaMod.resizable(width = True, height = False)
	ventanaMod.geometry ("250x250")
	ventanaMod.config (bg = "black")

	titulo = Label (ventanaMod, text = "Indique nuevo precio del pabellon: $", bg = "black", fg = "white", font = ("Cursive", 11))
	titulo.place (x = 10, y = 50)
	global cuadroMod
	cuadroMod = Entry(ventanaMod)
	cuadroMod.place(x = 55, y = 75)

	boton_completarReg = Button (ventanaMod, text = "Modificar", command = guardarMod)
	boton_completarReg.place (x = 85, y = 100)

def modificar_Plato2():
	ventanaMod = Tk()

	ventanaMod.title("Modificar precio: Cachapa")
	ventanaMod.resizable(width = True, height = False)
	ventanaMod.geometry ("250x250")
	ventanaMod.config (bg = "black")

	titulo = Label (ventanaMod, text = "Indique nuevo precio de la Cachapa: $", bg = "black", fg = "white", font = ("Cursive", 11))
	titulo.place (x = 10, y = 50)
	global cuadroMod
	cuadroMod = Entry(ventanaMod)
	cuadroMod.place(x = 55, y = 75)

	boton_completarReg = Button (ventanaMod, text = "Modificar", command = guardarModC)
	boton_completarReg.place (x = 85, y = 100)

def modificar_Plato3():
	ventanaMod = Tk()

	ventanaMod.title("Modificar precio: Ensalada")
	ventanaMod.resizable(width = True, height = False)
	ventanaMod.geometry ("250x250")
	ventanaMod.config (bg = "black")

	titulo = Label (ventanaMod, text = "Indique nuevo precio de la Ensalada: $", bg = "black", fg = "white", font = ("Cursive", 11))
	titulo.place (x = 10, y = 50)
	global cuadroMod
	cuadroMod = Entry(ventanaMod)
	cuadroMod.place(x = 55, y = 75)

	boton_completarReg = Button (ventanaMod, text = "Modificar", command = guardarModE)
	boton_completarReg.place (x = 85, y = 100)

def modificarPrecios():
	global modificar_precios
	modificar_precios = Tk()

	modificar_precios.title("Modificar")
	modificar_precios.resizable(width = True, height = False)
	modificar_precios.geometry ("800x400")
	modificar_precios.config (bg = "black")

	titulo = Label (modificar_precios, text = "Modificar precios", bg = "black", fg = "white", font = ("Cursive", 25))
	titulo.place (x = 260, y = 30)

	comida1 = Button (modificar_precios,text = "Pabellon", width = 25, height = 10, command = modificar_Plato1)
	comida1.place(x = 60, y = 100)
	comida2 = Button (modificar_precios,text = "Cachapa", width = 25, height = 10, command = modificar_Plato2)
	comida2.place(x = 300, y = 100)
	comida3 = Button (modificar_precios ,text = "Ensalada" ,width = 25, height = 10, command = modificar_Plato3)
	comida3.place(x = 540, y = 100)



def pedir_plato1():
	nombre = plato1[0]
	cantidad = cuadro1.get()

	archivo = open ("ventas_realizadas", "ab")
	archivo2 = open ("Precio pabellon", "rb")

	precio = archivo2.read()

	archivo.write(nombre)
	archivo.write(", Precio: "+str(precio)+"$")
	archivo.write(", Cantidad: "+str(cantidad))
	archivo.write("\n")
	archivo.write("--------------------------------------")
	archivo.write("\n")
	archivo2.close()
	archivo.close()
	showinfo (title="Preparando", message ="Su pedido ha sido tomado. Espere Por favor")

def pedir_plato2():
	nombre = plato2[0]
	cantidad = cuadro1.get()

	archivo = open ("ventas_realizadas", "ab")
	archivo2 = open ("Precio Cachapa", "rb")

	precio = archivo2.read()

	archivo.write(nombre)
	archivo.write(", Precio: "+str(precio)+"$")
	archivo.write(", Cantidad: "+str(cantidad))
	archivo.write("\n")
	archivo.write("--------------------------------------")
	archivo.write("\n")
	archivo2.close()
	archivo.close()
	
	showinfo (title="Preparando", message ="Su pedido ha sido tomado. Espere Por favor")

def pedir_plato3():
	nombre = plato3[0]
	cantidad = cuadro1.get()

	archivo = open ("ventas_realizadas", "ab")
	archivo2 = open ("Precio Ensalada", "rb")

	precio = archivo2.read()

	archivo.write(nombre)
	archivo.write(", Precio: "+str(precio)+"$")
	archivo.write(", Cantidad: "+str(cantidad))
	archivo.write("\n")
	archivo.write("--------------------------------------")
	archivo.write("\n")
	archivo2.close()
	archivo.close()
	
	showinfo (title="Preparando", message ="Su pedido ha sido tomado. Espere Por favor")

def Plato1():
	global ventanaInfo
	ventanaInfo = Tk()

	ventanaInfo.title ("Infomacion del pabellon")
	ventanaInfo.resizable (width = True, height = False)
	ventanaInfo.geometry ("800x600")
	ventanaInfo.config (bg = "black")

	titulo = Label (ventanaInfo, text = "EL PABELLON", bg = "black", fg = "white", font = ("Cursive", 25))
	titulo.place (x = 290, y = 30)
	frame = Frame(ventanaInfo)
	frame.place(x = 180, y = 100)
	frame.config(bg="white",width="450",height="300",bd=35,relief="groove")


	archivo = open ("Precio pabellon", "rb")
	precio = archivo.read()
	archivo.close()
	
	texto = Label(frame, text ="Se compone de Arroz Blanco, Carne Mechada, Caraotas" , bg = "white", fg = "black", font = ("Cursive", 11))
	texto.place(x = 4, y = 15)
	texto1 = Label(frame, text = "Negras y Tajadas de Platano Frito, dispuestos ",bg = "white", fg = "black", font = ("Cursive", 11) )
	texto1.place(x = 4, y = 40)
	texto2 = Label(frame, text = " todos de forma ornamental destacando al maximo",bg = "white", fg = "black", font = ("Cursive", 11) )
	texto2.place(x = 4, y = 65)
	texto3 = Label(frame, text = "su color, aroma y sabor. Precio: "+ precio+"$" ,bg = "white", fg = "black", font = ("Cursive", 11))
	texto3.place(x = 4, y = 90)

	global cuadro1
	cuadro1 = Entry(ventanaInfo)
	cuadro1.place(x = 346, y = 450) 

	text = Label (ventanaInfo, text = "Cantidad de platos:", bg = "black", fg = "white").place(x = 225, y = 448)

	boton_pedir = Button(ventanaInfo, text = "Pedir.", command = pedir_plato1).place(x = 346, y = 480)

def Plato2():
	global ventanaInfo

	ventanaInfo = Tk()

	ventanaInfo.title ("Infomacion del pabellon")
	ventanaInfo.resizable (width = True, height = False)
	ventanaInfo.geometry ("800x600")
	ventanaInfo.config (bg = "black")

	titulo = Label (ventanaInfo, text = "LA CACHAPA", bg = "black", fg = "white", font = ("Cursive", 25))
	titulo.place (x = 290, y = 30)
	frame = Frame(ventanaInfo)
	frame.place(x = 180, y = 100)
	frame.config(bg="white",width="450",height="300",bd=35,relief="groove")

	archivo = open ("Precio Cachapa", "rb")
	precio = archivo.read()
	archivo.close()
	
	texto = Label(frame, text ="Es una mezcla que se prepara con jojotos tiernos" , bg = "white", fg = "black", font = ("Cursive", 11))
	texto.place(x = 4, y = 15)
	texto1 = Label(frame, text = "Se sirven calientes, con mantequilla y rellenas",bg = "white", fg = "black", font = ("Cursive", 11) )
	texto1.place(x = 4, y = 40)
	texto2 = Label(frame, text = "con queso blanco suave",bg = "white", fg = "black", font = ("Cursive", 11) )
	texto2.place(x = 4, y = 65)
	texto3 = Label(frame, text = "(queso de mano). Precio: "+precio+"$",bg = "white", fg = "black", font = ("Cursive", 11))
	texto3.place(x = 4, y = 90)

	global cuadro1
	cuadro1 = Entry(ventanaInfo)
	cuadro1.place(x = 346, y = 450) 

	text = Label (ventanaInfo, text = "Cantidad de platos:", bg = "black", fg = "white").place(x = 225, y = 448)

	boton_pedir = Button(ventanaInfo, text = "Pedir.", command = pedir_plato2).place(x = 346, y = 480)

def Plato3():
	global ventanaInfo

	ventanaInfo = Tk()

	ventanaInfo.title ("Infomacion del pabellon")
	ventanaInfo.resizable (width = True, height = False)
	ventanaInfo.geometry ("800x600")
	ventanaInfo.config (bg = "black")

	titulo = Label (ventanaInfo, text = "ENSALADA RUSA", bg = "black", fg = "white", font = ("Cursive", 25))
	titulo.place (x = 290, y = 30)
	frame = Frame(ventanaInfo)
	frame.place(x = 180, y = 100)
	frame.config(bg="white",width="450",height="300",bd=35,relief="groove")


	archivo = open ("Precio Ensalada", "rb")
	precio = archivo.read()
	archivo.close()
	
	texto = Label(frame, text ="La ensalada es un plato que se come frio, esta" , bg = "white", fg = "black", font = ("Cursive", 11))
	texto.place(x = 4, y = 15)
	texto1 = Label(frame, text = "ensalada esta compuesta de patata, guisantes,",bg = "white", fg = "black", font = ("Cursive", 11) )
	texto1.place(x = 4, y = 40)
	texto2 = Label(frame, text = "zanahoria y huevo cocido, mezclados ",bg = "white", fg = "black", font = ("Cursive", 11) )
	texto2.place(x = 4, y = 65)
	texto3 = Label(frame, text = "con atun u otros ingredientes. Precio: "+precio+"$" ,bg = "white", fg = "black", font = ("Cursive", 11))
	texto3.place(x = 4, y = 90)

	global cuadro1
	cuadro1 = Entry(ventanaInfo)
	cuadro1.place(x = 346, y = 450) 

	text = Label (ventanaInfo, text = "Cantidad de platos:", bg = "black", fg = "white").place(x = 225, y = 448)

	boton_pedir = Button(ventanaInfo, text = "Pedir.", command = pedir_plato3).place(x = 346, y = 480)



def  mostrar_menu():
	global mostrar_menu1
	mostrar_menu1 = Tk()

	mostrar_menu1.title("Menu")
	mostrar_menu1.resizable(width = True, height = False)
	mostrar_menu1.geometry ("800x400")
	mostrar_menu1.config (bg = "black")

	titulo = Label (mostrar_menu1, text = "Menu de la semana", bg = "black", fg = "white", font = ("Cursive", 25))
	titulo.place (x = 260, y = 30)

	comida1 = Button (mostrar_menu1,text = "Pabellon", width = 25, height = 10, command = Plato1)
	comida1.place(x = 60, y = 100)
	comida2 = Button (mostrar_menu1,text = "Cachapa", width = 25, height = 10, command = Plato2)
	comida2.place(x = 300, y = 100)
	comida3 = Button (mostrar_menu1 ,text = "Ensalada" ,width = 25, height = 10, command = Plato3)
	comida3.place(x = 540, y = 100)

def menu_cliente():
    
	ventanaCliente = Tk()

	ventanaCliente.title("Usuario: Cliente")
	ventanaCliente.resizable(width = True, height = False)
	ventanaCliente.geometry ("800x600")
	ventanaCliente.config (bg = "black")

	welcome = Label(ventanaCliente, text = "Bienvenido: "+ cuadro_usuario.get(), bg = "black", fg = "white", font = ("Cursive", 25))
	welcome.place (x = 250, y = 90)

	boton_ver_menu = Button (ventanaCliente, text = "Ver Menu.", width = 50, height = 10, command = mostrar_menu)
	boton_ver_menu.place(x = 200, y = 200)

def ver_ventas():
	ventanaReg = Tk()

	ventanaReg.title("Ventas realizadas")
	ventanaReg.resizable(width = True, height = False)
	ventanaReg.geometry ("500x500")
	ventanaReg.config (bg = "black")

	frame = Frame(ventanaReg)
	frame.place(x = 50, y = 50)
	frame.config(bg="white",width="400",height="400",bd=35,relief="groove")

	archivo = open ("ventas_realizadas", "rb")
	Ventas = archivo.read()
	archivo.close()

	texto = Label(frame, text = Ventas, bg = "white", fg = "black", font = ("Cursive", 11))
	texto.place(x = 4, y = 15)

def menu_admin():
    
	ventanaAdmin = Tk()

	ventanaAdmin.title("Usuario: Administrador")
	ventanaAdmin.resizable(width = True, height = False)
	ventanaAdmin.geometry ("800x600")
	ventanaAdmin.config (bg = "black")

	titulo = Label (ventanaAdmin, text = "Bienvenido: Administrador", bg = "black", fg = "white", font = ("Cursive", 25))
	titulo.place (x = 270, y = 30)

	boton_ver_menu = Button (ventanaAdmin, text = "Ver Menu.", width = 25, height = 10, command = mostrar_menu)
	boton_ver_menu.place(x = 105, y = 100)

	boton_modificar = Button (ventanaAdmin, text = "Modificar precios.", width = 25, height = 10, command = modificarPrecios)
	boton_modificar.place(x = 105, y = 300)

	boton_ver_ventas = Button (ventanaAdmin, text = "Ver ventas realizadas", width = 55, height = 10, command = ver_ventas)
	boton_ver_ventas.place(x = 355, y = 180)

def codigo_boton_ingresar():
	provi = cuadro_usuario.get()
	datos = cuadro_password.get()
	if provi == "":
		showinfo (title="Error", message ="Introduzca un usuario...")
		
	if datos == "":
		showinfo (title="Error", message ="Introduzca una contrasena...")	
	else:
		if provi == "Administrador" and datos == "admin":
			showinfo (title="logeo correcto", message ="Se ha logueado correctamente")
			menu_admin()

		else:
			archivo = open (provi, "rb")
			datosFi = archivo.readline()
			archivo.close()


			if datosFi == datos:
				showinfo (title="logeo correcto", message ="Se ha logueado correctamente")
				menu_cliente()

		

def guardarUsuario():
	datos = cuadro_solicitud2.get()

	archivo = open (cuadro_solicitud.get(), "wb")
	for datos in datos:
		archivo.write(str(datos))
	archivo.close()

	showinfo (title="Registro completado", message ="Se ha registrado correctamente. Puede cerrar la ventana e iniciar sesion")

def  ventanaRegistro():
	ventanaReg = Tk()

	ventanaReg.title("Registrar nuevo usuario")
	ventanaReg.resizable(width = True, height = False)
	ventanaReg.geometry ("500x500")
	ventanaReg.config (bg = "black")

	Registro = Label(ventanaReg, text = "Registro de usuario", bg = "black", fg = "white", font = ("Cursive", 25))
	Registro.place (x = 115, y = 130)

	usuario = Label(ventanaReg, text = "Nuevo usuario", bg = "black", fg = "white", font = ("Arial", 11))
	usuario.place (x = 120, y = 249)

	password = Label(ventanaReg, text = "Contrasena", bg = "black", fg = "white", font = ("Arial", 11))
	password.place (x = 120, y = 279)

	global cuadro_solicitud
	cuadro_solicitud = Entry(ventanaReg)
	cuadro_solicitud.place(x = 220, y = 250)

	global cuadro_solicitud2
	cuadro_solicitud2 = Entry(ventanaReg)
	cuadro_solicitud2.place (x = 220, y = 280)
	cuadro_solicitud2.config (show = "*")

	boton_completarReg = Button (ventanaReg, text = "Registrarse", command = guardarUsuario)
	boton_completarReg.place (x = 230, y = 310)


def codigo_boton_registrar():
	ventanaRegistro()


ventana_principal()

elementos_login()


ventana.mainloop()