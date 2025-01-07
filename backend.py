from flask import Flask, request, render_template
import numpy as np
import xgboost as xgb
import pickle

# Monkey patch the old module path
import sys
sys.modules['xgboost.sklearn'] = xgb

# Load the trained model
model = pickle.load(open('pre trained models/XGB.pkl', 'rb'))

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve form inputs
        data = {
            'Age': float(request.form['Age']),
            'Annual_Income': float(request.form['Annual_Income']),
            'Monthly_Inhand_Salary': float(request.form['Monthly_Inhand_Salary']),
            'Num_Bank_Accounts': int(request.form['Num_Bank_Accounts']),
            'Num_Credit_Card': int(request.form['Num_Credit_Card']),
            'Interest_Rate': float(request.form['Interest_Rate']),
            'Num_of_Loan': int(request.form['Num_of_Loan']),
            'Delay_from_due_date': int(request.form['Delay_from_due_date']),
            'Num_of_Delayed_Payment': int(request.form['Num_of_Delayed_Payment']),
            'Changed_Credit_Limit': float(request.form['Changed_Credit_Limit']),
            'Num_Credit_Inquiries': int(request.form['Num_Credit_Inquiries']),
            'Outstanding_Debt': float(request.form['Outstanding_Debt']),
            'Credit_Utilization_Ratio': float(request.form['Credit_Utilization_Ratio']),
            'Total_EMI_per_month': float(request.form['Total_EMI_per_month']),
            'Amount_invested_monthly': float(request.form['Amount_invested_monthly']),
            'Monthly_Balance': float(request.form['Monthly_Balance']),
            'Credit_History_Age_Months': int(request.form['Credit_History_Age_Months']),
            'Occupation': request.form['Occupation'],  # Mapping required
            'Credit_Mix': int(request.form['Credit_Mix']),
            'Payment_Behaviour': request.form['Payment_Behaviour'],  # Mapping required
            'Payment_of_Min_Amount': request.form['Payment_of_Min_Amount']  # Mapping required
        }

        # Apply mappings to categorical inputs
        occupation_map = {
            'Scientist': 1, 'Other': 2, 'Teacher': 3, 'Engineer': 4,
            'Entrepreneur': 5, 'Developer': 6, 'Lawyer': 7, 'Media_Manager': 8,
            'Doctor': 9, 'Journalist': 10, 'Manager': 11, 'Accountant': 12,
            'Musician': 13, 'Mechanic': 14, 'Writer': 15, 'Architect': 16
        }
        payment_behaviour_map = {
            'Low_spent_Small_value_payments': 0,
            'Low_spent_Medium_value_payments': 1,
            'Low_spent_Large_value_payments': 2,
            'High_spent_Small_value_payments': 3,
            'High_spent_Medium_value_payments': 4,
            'High_spent_Large_value_payments': 5
        }
        payment_min_map = {'Yes': 1, 'No': 0, 'NM': -1}

        data['Occupation'] = occupation_map[data['Occupation']]
        data['Payment_Behaviour'] = payment_behaviour_map[data['Payment_Behaviour']]
        data['Payment_of_Min_Amount'] = payment_min_map[data['Payment_of_Min_Amount']]

        # Convert data to numpy array for model input
        input_features = np.array(list(data.values())).reshape(1, -1)

        # Predict using the model

        prediction = model.predict(input_features)[0]

        # Map prediction to credit score
        credit_score_mapping = {0: 'Poor', 1: 'Standard', 2: 'Good'}
        credit_score = credit_score_mapping.get(prediction, "Unknown")

        # Return mapped prediction result
        return render_template('result.html', credit_score=credit_score)

if __name__ == '__main__':
    app.run(debug=True)