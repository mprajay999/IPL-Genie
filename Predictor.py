import pickle
from sklearn.linear_model import LogisticRegression
import warnings


infile = open('Model.pkl','rb')
Model = pickle.load(infile)

def Predict(A,B,H,T):
    x= Model.predict_proba([[A,B,H,T]])[:,1]
    return x[0]
