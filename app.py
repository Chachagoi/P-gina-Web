from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encuesta')
def encuesta():
    return render_template('encuesta.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        age = int(data['age'])
        symptoms = 1 if data['symptoms'].lower() == 'sí' else 0
        # Aquí deberías cargar tu modelo y hacer la predicción
        # Ejemplo de predicción
        prediction = 'Enfermedad' if age > 30 and symptoms == 1 else 'No Enfermedad'
        return jsonify({'prediction': prediction}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)