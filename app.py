from flask import Flask, render_template,request
from Predictor import Predict
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    A=request.form.get('TeamA')
    B=request.form.get('TeamB')
    H=request.form.get('Homeground')
    T=request.form.get('Toss')
    P=Predict(float(A),float(B),float(H),float(T))
    return render_template('Message.html',p=P)


if __name__ == '__main__':
    app.run()
