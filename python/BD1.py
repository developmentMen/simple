import sqlite3
from tkinter import *
from tkinter import filedialog


def verTabla(ver):
	for i in ver:
		print(i)

def conectar():
	return(filedialog.askopenfilename())

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


def Select(conectar):
	conexion = sqlite3.connect(conectar)
	cursor = conexion.cursor()
	cursor.execute("SELECT * FROM persona")
	info = cursor.fetchall()
	texto = " "
	for e in info:
		texto += e
	pantalla.config(text = texto)
	conexion.commit()
	conexion.close()
	

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

def salir():
	conexion.commit()
	conexion.close()

ventana=Tk()
ventana.title("Administrator Base Data")
ventana.geometry("650x500")

Button(ventana,text="Salir",command=quit).grid(column=0,row=0,padx=10,pady=10)

Label(ventana,width=40,height=8,padx=15,pady=15,text="hola").grid(column=1,row=1)

con = Button(ventana,text="Conectar",command=conectar).grid(column=2,row=0)

Button(ventana,text="ver",command=print(con)).grid(column=1,row=2)

Button(ventana,text="guardar",command=salir).grid(column=0,row=2)

ventana.mainloop()