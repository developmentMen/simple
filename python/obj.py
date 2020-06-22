
class perro():
	
	def __init__(self, patas,cabeza,nombre):
		self.patas 	= patas
		self.cabeza = cabeza
		self.nombre = nombre

	def __str__(self):
		return "{} tiene {} cabezas y {} patas".format(self.nombre,self.cabeza,self.patas)

	def imprimirNombre(self):
		print(self.nombre)

p1 = perro(4,1,"thor")

print(p1.__str__())