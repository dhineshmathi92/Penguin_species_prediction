from flask import Flask, jsonify, request
import joblib
import pandas as pd

app = Flask(__name__)


@app.route("/", methods=['get'])
def welcome():
    return jsonify({"message": "Hello world"})


@app.route('/predict', methods=['POST'])
def get_prediction():
    try:
        # Extract JSON payload from the request
        data = request.get_json()
        # Validate input data
        required_fields = ["island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex"]
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "success": False,
                    "message": f"Missing field: {field}"
                }), 400
        
        # Extract individual values
        island = data['island']
        bill_length_mm = data['bill_length_mm']
        bill_depth_mm = data['bill_depth_mm']
        flipper_length_mm = data['flipper_length_mm']
        body_mass_g = data['body_mass_g']
        sex = data['sex']

        model = joblib.load("pipeline.pkl")

        input = pd.DataFrame([island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex]).T

        input.columns = required_fields

        prediction = model.predict(input)[0]

        response = {"species": prediction}

        print(response)

        return jsonify(response), 200

    except Exception as e:
        print(e)
    


if __name__=="__main__":
    app.run(debug=True)