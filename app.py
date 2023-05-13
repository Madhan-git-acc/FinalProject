from flask import Flask, jsonify, render_template, request, redirect
import joblib
import os
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic here, validate credentials, etc.
        # Redirect to the home page or handle authentication
        return redirect('/home.html')
    return render_template('login.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST', 'GET'])
def result():
    item_weight = float(request.form['item_weight'])
    item_fat_content = float(request.form['item_fat_content'])
    item_visibility = float(request.form['item_visibility'])
    item_type = float(request.form['item_type'])
    item_mrp = float(request.form['item_mrp'])
    outlet_establishment_year = float(request.form['outlet_establishment_year'])
    outlet_size = float(request.form['outlet_size'])
    outlet_location_type = float(request.form['outlet_location_type'])
    outlet_type = float(request.form['outlet_type'])

    X = np.array([[item_weight, item_fat_content, item_visibility, item_type, item_mrp, outlet_establishment_year,
                   outlet_size, outlet_location_type, outlet_type]])

    scalar_path = r'C:\Users\madha\Downloads\BigMart Prediction\Model\sc.sav'
    sc = joblib.load(scalar_path)

    X_std = sc.transform(X)

    model_path = r'C:\Users\madha\Downloads\BigMart Prediction\Model\random_forest_grid.sav'

    model = joblib.load(model_path)


    Y_pred = model.predict(X_std)

    prediction = float(Y_pred[0])

    return render_template('output.html', prediction=prediction)



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=94567)
