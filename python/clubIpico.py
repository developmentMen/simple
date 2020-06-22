import pickle

def CrearAbrir():
	var = input("fecha-->")
	return("{}.txt".format(var))

class Pedido():
	estado	= " "
	monto	= 0
	info	= " "

	def __init__(self, estado,monto):
		self.estado	= estado
		self.monto	= monto

	def setInfo(self):
		self.info 	= crearPedido()


def crearPedido():
	nombre	= input("nombre-->")
	pedido 	= input("pedido-->")
	mesa 	= input("mesa-->")
	final 	= "nombre: "+ nombre +"\npedido: "+ pedido +"\nmesa: "+ mesa +"\n---------------------------------------\n"
	return final
		
def terminar(Pedido,archivo):
	archivo.write(Pedido.estado+"\n"+Pedido.info)
	print("pedido escrito")

def mostrar(archivo):
	archivo.seek(0)
	contenido = archivo.read()
	print(contenido)


salir = False

while salir == False:
	eleccion = input("comando-->")
	if eleccion == "":
		archivo = open(CrearAbrir() , "a+")
	elif eleccion == "t":
		terminar(var,archivo)
	elif eleccion == "ver":
		print(var.estado)
	elif eleccion == "c":
		nuevo 	= input("actualizar estado-->")
		var.estado = nuevo
	elif eleccion == "nuevo" or eleccion == "n":
		est 	= input("estado-->")
		monto	= int(input("monto-->"))
		var		= Pedido(est,monto)
		var.setInfo()
	elif eleccion == "salir":
		archivo.close()
		salir = True