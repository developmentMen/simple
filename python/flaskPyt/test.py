from flask import Flask, render_template, request

app = Flask(__name__)

#|Hola Mundo...|
@app.route('/')
def hello_world():
	return "Hola Mundo con flask"

#|utilizando variables|
@app.route('/variable/<variable_enviada>')
def variableUser(variable_enviada):
	return "|valor ingresado| <h1>{}</h1>".format(variable_enviada)

#|enviando post|
@app.route('/enviar')
def env():
	return render_template('index.html')

@app.route('/funciona', methods = ['POST'])
def testeando():
	if request.method == 'POST':
		datosRecibidos = request.form['datos']
		print(datosRecibidos)
	return "enviado satisfactoriamente"

#|Para correr con python3 <archivo.py>		|
#|nota:permite editar sin reiniciar el servidor	|
if __name__ == '__main__':
	app.run(port = 3336, debug = True)
