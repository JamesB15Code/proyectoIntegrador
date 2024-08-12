from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Cargar el modelo y el escalador
modelo_svm = joblib.load('./models/modelo_svm.pkl')
escalador = joblib.load('./models/escalador.pkl')

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Suponiendo que recibes los datos en formato JSON
    data_np = np.array([data['Glucosa'], data['Presion_Arterial'], 
                        data['Grosor_Pliegue_Cutaneo'], data['Insulina'], 
                        data['IMC'], data['Funcion_Pedigri_Diabetes'], 
                        data['Edad']]).reshape(1, -1)
    
    # Escalar los datos
    data_scaled = escalador.transform(data_np)
    
    # Hacer la predicción
    prediction = modelo_svm.predict(data_scaled)
    
    # Retornar la predicción
    return jsonify({'Resultado': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)