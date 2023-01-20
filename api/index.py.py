from logging import debug
from flask import Flask, render_template, request 
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.ensemble import HistGradientBoostingRegressor
import numpy as np
import pandas 
import joblib


app = Flask(__name__)
@app.route('/') 
def home(): 
    return render_template('index.html') 

@app.route('/login') 
def login(): 
    return render_template('login.html')

@app.route('/Loan_Application') 
def Loan_Application(): 
    return render_template('Loan_Application.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/loancalculator')
def loancalculator():
    return render_template('loancalculator.html')

@app.route('/predict/', methods=['GET', 'POST'])

def predict():  
    if request.method == 'POST': 
        Gender = request.form['Gender']
        Married = request.form['Married']
        Education = request.form['Education']
        Self_Employed = request.form['Self_Employed'] 
        ApplicantIncome = request.form['ApplicantIncome']  
        CoapplicantIncome = request.form['CoapplicantIncome'] 
        LoanAmount = request.form['LoanAmount']   
        Loan_Amount_Term = request.form['Loan_Amount_Term']   
        Credit_History = request.form['Credit_History']   
        Property_Area = request.form['Property_Area']  

        Gender=Gender.lower()
        Married=Married.lower()
        Education=Education.lower()
        Self_Employed=Self_Employed.lower()
        Credit_History=Credit_History.lower()
        Property_Area=Property_Area.lower()
        error=0

        if(Gender=='male'):
            Gender=1
        else:
            Gender=0
        print(Gender)
        if(Married=='married'):
            Married=1
        else:
            Married=0

        if(Education=='graduate'):
            Education=1
        else:
            Education=0

        if(Self_Employed=='yes'):
            Self_Employed=1
        else:
            Self_Employed=0

        if(Credit_History=='yes'):
            Credit_History=1
        else:
            Credit_History=0

        if(Property_Area=='rural'):
            Property_Area=0
        elif(Property_Area=='semiurban'):
            Property_Area=1
        else:
            Property_Area=2
        try:
            ApplicantIncome=int(ApplicantIncome)
            CoapplicantIncome=int(CoapplicantIncome)
            LoanAmount=int(LoanAmount)
            Loan_Amount_Term=int(Loan_Amount_Term)
            x_app = np.array([[Gender,Married,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,Loan_Amount_Term,LoanAmount,Credit_History,Property_Area]])
            model=joblib.load('model.pkl')
            ans=model.predict(x_app)
            if(ans==1):
                print("Cong")
            else:
                print("Sorry")
            return render_template('predict.html',prediction = ans)
        except ValueError:
            return render_template('Loan_Application.html')
                

if __name__ == '__main__': 
    app.run(debug=True) 
