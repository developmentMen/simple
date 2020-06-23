
import pickle



class Pedido():

	def __init__(self,nombre,pedido,monto):
		self.nombre = nombre
		self.pedido = pedido
		self.monto 	= monto

	def toString(self):
		return ("cliente: "+self.nombre+"\nPedido: "+self.pedido+"\nMonto: "+self.monto)

	def Dicc(self):
		dic = { "nombre" : self.nombre,
				"pedido" : self.pedido,
				"monto"	 : int(self.monto)}
		return (dic)

	def guardar(self,diccionario,fileName):
		archivo	= open("{}.txt".format(fileName),"ab+")
		pickle.dump(diccionario, archivo)
		archivo.close()

def mostrar():
	v 		= input("nombre del archivo->")
	archivo	= open("{}.txt".format(v),"ab+")
	archivo.seek(0)
	cont 	= []
	while True:
		try:
			info =pickle.load(archivo)
		except:
			break
		cont.append(info)
	for e in cont:
		print("nombre ->"+e["nombre"].ljust(15," ")+"| pedido ->"+e["pedido"].ljust(25," ")+"| monto ->"+str(e["monto"]))
	total = 0
	for m in cont:
		total += m["monto"]
	print("\n\tpedidos total--> "+str(len(cont))+"\n\tfacturado total--> "+str(total))
	archivo.close()

def total():
	v 		= input("nombre del archivo->")
	archivo	= open("{}.txt".format(v),"ab+")
	archivo.seek(0)
	cont 	= []
	while True:
		try:
			info =pickle.load(archivo)
		except:
			break
		cont.append(info)
	archivo.close()
	total 	= 0
	for e in cont:
		total += e["monto"]
	return total

def facturar(dicc,con):
	archivo	= open("{}.txt".format(con),"ab+")
	pickle.dump(dicc, archivo)
	archivo.close()

def gasto(texto,fileName):
		archivo	= open("{}{}.txt".format(fileName,"s"),"a+")
		archivo.write(texto+"\n")
		archivo.close()


salir = False

con = input("Abrir | Crear -->")
abierto	 = []


while salir == False :
	eleccion = input("\nPedido\nAbierto\nMostrar\nGasto\nSalir\n-->")

	if eleccion == "p" or eleccion == "pedido":
		nom = input("nombre->")
		ped	= input("pedido->")
		mon	= input("monto->")
		var	= Pedido(nom,ped,mon)
		pagado = input("pedido pagado?-->[s/n]")
		if pagado == "s":
			try:
				var.guardar(var.Dicc(),con)
			except:
				print("_________________________\nhubo un error al guardar")
				print("_________________________")
		if pagado == "n":
			abierto.append(var.Dicc())
	if eleccion == "a" or eleccion == "abierto":
		try:
			for pedido in abierto:
				print (pedido)
			opc = input("facturar pedido?-->")
			if opc in pedido.values():
				facturar(pedido,con)
				pedido["nombre"] = "facturado"
		except:
			print("no hay pedidos abiertos")
	if eleccion == "m":
		mostrar()
	if eleccion == "g":
		salida = input("-->")
		gasto(salida,con)
	if eleccion == "s" or eleccion == "salir":
		salir = True

	