from flask import Flask
from flask import render_template
from flask import request

import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("student_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    attendance = 85
    previous_marks = 75
    study_hours = 2

    if request.method == "POST":

        attendance = float(
            request.form["attendance"]
        )

        previous_marks = float(
            request.form["previous_marks"]
        )

        study_hours = float(
            request.form["study_hours"]
        )

        input_data = pd.DataFrame({
            "attendance": [attendance],
            "previous_marks": [previous_marks],
            "study_hours": [study_hours]
        })

        result = model.predict(input_data)

        raw_prediction = float(result[0])
        prediction = min(max(raw_prediction, 0.0), 100.0)
        prediction = round(prediction, 2)

    return render_template(
        "index.html",
        prediction=prediction,
        attendance=attendance,
        previous_marks=previous_marks,
        study_hours=study_hours
    )


if __name__ == "__main__":
    app.run(debug=True)