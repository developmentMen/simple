import sqlite3

conexion = sqlite3.connect("BaseDatosContactos.db")
cursor = conexion.cursor()
#|crea una tabla|
#cursor.execute("CREATE TABLE contactos (nombre VARCHAR(50),edad INTEGER, fecha_Nacimiento INTEGER)")

#|inserta informacion|
#cursor.execute("INSERT INTO contactos VALUES ('jose',53,23051997)")

#|devolviendo informacion|
#cursor.execute("SELECT * FROM contactos")
#informacion=cursor.fetchone() #primer fila|tipo tupla
#informacion=cursor.fetchall() #tabla completa|tipo lista

#|multliple|
#varios=[
#	("pablo",43,24101987),
#	("raul",23,17081997)]
#cursor.executemany("INSERT INTO contactos VALUES (?,?,?)", varios)

#aplicamos los cambios
conexion.commit()

conexion.close() 
