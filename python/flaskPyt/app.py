from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	titulo = "Home!"
	lista  = ["hola", "soy una lista", 4, "otro elem"]
	return render_template('index.html', titulo=titulo, lista=lista)

if __name__ == "__main__":
	app.run(debug=True, port=33699)
