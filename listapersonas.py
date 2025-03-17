from flask import Flask, jsonify

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir la ruta para obtener la lista de personas
@app.route('/personas', methods=['GET'])
def index():
  
    lista_personas = [
        {'name' : 'Thair Constante Pineda'},
        {'name' : 'Carmen Mestre'},
        {'name' : 'Sofia Valentina'},
        {'name' : 'Manuel Risco'}
    ]
    return jsonify(lista_personas)

# Ejecutar la aplicación si este archivo se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)
