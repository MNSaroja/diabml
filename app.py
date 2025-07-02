from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_file', methods=['POST'])
def predict_file():
    try:
        # Extract and prepare features
        features = [[float(request.form[f]) for f in [
            "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
            "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]]]
        
        # Make prediction
        prediction = model.predict(features)
        #result = f"Prediction: {int(prediction[0])}"
        result = f"Prediction (0=No Diabetes, 1=Diabetes): {int(prediction[0])}"

    except Exception as e:
        result = f"Error: {str(e)}"

    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
