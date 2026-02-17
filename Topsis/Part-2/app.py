import os
import smtplib
import pandas as pd
import numpy as np
from email.message import EmailMessage
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secretkey"

email_add = "prannaykamal9@gmail.com"
email_pswd = "wyjvutlfieqtimav"   # Revoked

def run_topsis(file_path, weights_inp, impacts_inp):
    df = pd.read_csv(file_path)
    if df.shape[1] < 3:
        raise ValueError("Input file must contain more than 2 columns")
    
    criteria = df.iloc[:, 1:].copy()
    criteria = criteria.apply(pd.to_numeric, errors='coerce')
    if criteria.isnull().values.any():
        raise ValueError("Columns from 2nd to end must contain numeric values only")
    n_crit = criteria.shape[1]
    weights = np.array([float(w.strip()) for w in weights_inp.split(',')], dtype=float)
    impacts = [s.strip() for s in impacts_inp.split(',')]

    if len(weights) != n_crit or len(impacts) != n_crit:
        raise ValueError("Weights and impacts count must match criteria columns")

    col_norm = np.sqrt((criteria ** 2).sum(axis=0).astype(float))
    norm = criteria / col_norm
    weighted = norm * weights 

    best, worst = [], []
    for i in range(n_crit):
        col = weighted.iloc[:, i]
        if impacts[i] == '+':
            best.append(col.max()); worst.append(col.min())
        else:
            best.append(col.min()); worst.append(col.max())

    best, worst = np.array(best), np.array(worst)
    best_dist = np.sqrt(((weighted - best) ** 2).sum(axis=1))
    worst_dist = np.sqrt(((weighted - worst) ** 2).sum(axis=1))
    denom = best_dist + worst_dist
    
    df['Topsis Score'] = np.where(denom == 0, 0.0, worst_dist / denom).round(4)
    df['Rank'] = df['Topsis Score'].rank(ascending=False, method='dense').astype(int)
    
    out_path = "result.csv"
    df.to_csv(out_path, index=False)
    return out_path

def send_email(rec_mail, attachment_path):
    msg = EmailMessage()
    msg['Subject'] = 'Your TOPSIS Result File'
    msg['From'] = email_add
    msg['To'] = rec_mail
    msg.set_content("Please find the attached TOPSIS result.")

    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='csv', filename='result.csv')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_add, email_pswd)
        smtp.send_message(msg)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            file = request.files['file']
            weights = request.form['weights']
            impacts = request.form['impacts']
            email = request.form['email']

            if file and email:
                file_path = "temp_input.csv"
                file.save(file_path)
                result_file = run_topsis(file_path, weights, impacts)
                send_email(email, result_file)
                flash("Success! Result emailed to " + email, "success")
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)