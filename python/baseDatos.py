import sqlite3

def verTabla(ver):
	for i in ver:
		print(i)

def conectar():
	print("			   |si no existe se crea|")
	var=input("nombre de base de datos--->")
	return("{}.db".format(var))

def Create():
	var1=input("CRATE TABLE->")
	var2=input("ColumnName Datatype PRIMARY KEY|NULL|NOT NULL->")
	return("CREATE TABLE {} ({})".format(var1,var2))

def Drop():
	var1=input("DROP TABLE->")
	return("DROP TABLE {}".format(var1))

def AlterAdd():
	var1=input("ALTER TABLE->")
	var2=input("nombre de la nueva columna->")
	return("ALTER TABLE {} ADD {} VARCHAR(20)".format(var1,var2))

def AlterRename():
	var1=input("nombre tabla a modificar->")
	var2=input("nombre tabla nuevo->")
	return("ALTER TABLE {} RENAME TO {}".format(var1,var2))

def AlterRenamecolum():
	var1=input("nombre tabla a modificar->")
	var2=input("nombre de columna a modificar->")
	var3=input("nombre nueva columna")
	return("ALTER TABLE {} RENAME COLUMN {} TO {}".format(var1,var2,var3))


def Select():
	var1=input("SELECT->")
	var2=input("FROM->")
	return("SELECT {} FROM {}".format(var1,var2))

def Insert():
	var1=input("INSERT_INTO->")
	var2=input("VALUES->")
	return("INSERT INTO {} VALUES ({})".format(var1,var2))

def Update():
	var1=input("UPDATE->")
	var2=input("SET->")
	var3=input("WHERE->")
	return("UPDATE {} SET {} WHERE {}".format(var1,var2,var3))

def Delete():
	var1=input("DELETE FROM->")
	var2=input("WHERE->")
	return("DELETE FROM {} WHERE {}".format(var1,var2))

con=sqlite3.connect(conectar())
cur=con.cursor()

salir=False
while salir==False:
	try:
		a=int(input("Menu--->\n	1.DDL/DML\n 	2.ver Info\n 	3.ver schem\n 	4.guardar & salir\n 	"))

		if a == 1:
			eleccion=int(input("1.CREATE 2.DROP 3.ALTER | 4.SELECT 5.INSERT 6.UPDATE 7.DELETE\n"))
			if eleccion == 1:
				cur.execute(Create())
			elif eleccion == 2:
				cur.execute(Drop())
			elif eleccion == 3:
				eleccion1=int(input("1.add | 2.rename\n"))
				if eleccion1 == 1:
					cur.execute(AlterAdd())
				elif eleccion1 == 2:
					cur.execute(AlterRename())
				#elif eleccion1 == 3:
					#cur.execute(AlterRenamecolum())
				else:
					print("valor invalido")
			elif eleccion == 4:
				cur.execute(Select())
				imprim=cur.fetchall()
				verTabla(imprim)
			elif eleccion == 5:
				cur.execute(Insert())
			elif eleccion == 6:
				cur.execute(Update())
			elif eleccion == 7:
				cur.execute(Delete())
			else:
				print("valor invalido")

		elif a == 2:
			infor=input("nombre de tabla--->")
			cur.execute("SELECT * FROM {}".format(infor))
			informacion=cur.fetchall()
			verTabla(informacion)
		elif a == 3:
			cur.execute("SELECT * FROM SQLite_master")
			imprim=cur.fetchall()
			q=0
			for e in imprim:
				print(imprim[q][4])
				q+=1
		elif a == 4:
			salir=True
		else:
			print("opcion erronea")
	except:
		print("opcion erronea")
con.commit()
con.close()
