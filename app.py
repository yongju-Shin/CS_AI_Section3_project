from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

with open("encoder.pkl", "rb") as encoder_file:
    encoder = pickle.load(encoder_file)

with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    new_data = [[data1, data2, data3, data4, data5]]
    new_data = pd.DataFrame(new_data, columns=['price', 'tasty1', 'tasty2', 'blend', 'roasting'])
    now_data = encoder.transform(new_data)
    pred = model.predict(now_data)
    return render_template('after.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)