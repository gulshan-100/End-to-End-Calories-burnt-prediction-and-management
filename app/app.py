from flask import Flask, request, render_template, send_from_directory, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model_path = r'C:\Users\DELL\Downloads\End-to-End-Calories-burnt-prediction-and-management\app\models\calories_burnt_prediction.sav'

# Load the machine learning model
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/styles.css')
def styles():
    return send_from_directory('templates', 'styles.css')

@app.route('/image.jpg')
def image():
    return send_from_directory('templates', 'image.jpg')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input from the HTML form
        gender = request.form['gender']
        age = int(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        duration = float(request.form['duration'])
        heart_rate = float(request.form['heart-rate'])
        body_temp = float(request.form['body-temperature'])

        # Encode gender
        gender_encoded = 0 if gender.lower() == 'male' else 1

        # Create input data array for prediction
        input_data = np.array([[gender_encoded, age, height, weight, duration, heart_rate, body_temp]])

        # Make prediction
        prediction = model.predict(input_data)

        prediction = round(float(prediction[0]), 2)

        # Return prediction as JSON response
        return jsonify(success=True, prediction=prediction)
    except Exception as e:
        return jsonify(success=False, error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
