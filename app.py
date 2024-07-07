from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('C:\Users\DELL\Downloads\End-to-End-Calories-burnt-prediction-and-management\app\templates\index.html')

if __name__ == '__main__':
    app.run(debug=True)
