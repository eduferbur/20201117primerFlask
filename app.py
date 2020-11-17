from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Ruta raiz"

@app.route('/home')
@app.route('/home2')     # Podemos usar varios rutas
def hello_world():
    return 'Hello World'

@app.route("/hola/<string:nombre>")
def contanto(nombre):   # Escribir comandos de html y pasar parámetros
    return f"<h1>Hola {nombre}</h1>"    # No es lo normal, ver siguiente.

# ........... FLASK + HTML + JINJA .................
@app.route('/htmlRead')
def htmlread():
    return render_template('index.html')  #Enlazar archivo html

@app.route('/htmlJINJAVariable')  # Pasar variables
def htmlJINJAVariable():
    nombre = "Eduardo" # Creamos una variable de python normal.
    return render_template('JINJAleeVariable.html', parametro=nombre)
    # En el archivo html: <h1>Hola {{parametro}}</h1>

@app.route('/usandoJINJA')
def htmlJINJAVariableIF():
    variableIF = 1
    variableFOR = [1, 2, 3, 4]
    return render_template('usandoJINJA.html', parametro1=variableIF, parametro2=variableFOR)

# --------- JINJA LEE FORMULARIO, ALMACENA Y MUESTRA ---------------
@app.route('/htmlDinamicoLee')
def htmlDinamicaGET():
    return render_template('dinamicoGET.html')

@app.route('/htmlDinamicoEscribe', methods =['POST'])
def htmlDinamicaPOST():
    variableGET = request.form.get("nombreEscrito")
    print(variableGET)
    return render_template('dinamicoPOST.html', variablePOST=variableGET)


if __name__ == '__main__':
    app.run(debug=True)
