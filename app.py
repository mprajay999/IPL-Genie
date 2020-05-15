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
    return render_template('Message.html',p='Team A Has a Winning Probability of {} %'.format(P*100))

@app.route('/calculate')
def calculate():
    return render_template('Message.html',m='Team A rating = (1-(0.1*position of team A on points table))+(No. of matches Team A has won Against Team B in the past / Total no. of Matches Played Between Team A and Team B)',
                           m1='Team B rating = (1-(0.1*position of team B on points table))+(No. of matches Team B has won Against Team A in the past / Total no. of Matches Played Between Team A and Team B)')


if __name__ == '__main__':
    app.run()
