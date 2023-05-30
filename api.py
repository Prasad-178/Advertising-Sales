from flask import Flask, request, jsonify
import joblib
import pandas as pd

# CREATE FLASK APP
app = Flask(__name__)

# CONNECT POST API CALL --> PREDICT() FUNCTION
@app.route('/predict', methods=['POST'])
def predict():
    # GET THE JSON REQUEST
    feature_data = request.json
    
    # CONVERT JSON TO PANDAS DF
    df = pd.DataFrame(feature_data)
    df = df.reindex(columns=col_names)
    
    # PREDICT
    prediction = list(model.predict(df))
    
    return jsonify({'prediction':str(prediction)})


# LOAD MODEL AND COLUMN NAMES
if __name__ == '__main__':
    model = joblib.load("final_model.pkl")
    col_names = joblib.load("col_names.pkl")
    
    app.run(debug=True)