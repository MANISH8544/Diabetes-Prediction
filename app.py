from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load('c3.joblib')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get user inputs from form
            pregnancies = float(request.form['pregnancies'])
            glucose = float(request.form['glucose'])
            blood_pressure = float(request.form['blood_pressure'])
            skin_thickness = float(request.form['skin_thickness'])
            insulin = float(request.form['insulin'])
            bmi = float(request.form['bmi'])
            dpf = float(request.form['dpf'])
            age = float(request.form['age'])

            # Create feature array
            features = np.array([[pregnancies, glucose, blood_pressure, 
                                skin_thickness, insulin, bmi, dpf, age]])

            # Make prediction
            prediction = model.predict(features)
            result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"

            return render_template('index.html', result=result)
        
        except Exception as e:
            return render_template('index.html', result=f"Error: {str(e)}")

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
