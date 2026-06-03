import joblib
import pandas as pd


def predict_score(attendance,
                  previous_marks,
                  study_hours):

    model = joblib.load("student_model.pkl")

    data = pd.DataFrame({
        'attendance': [attendance],
        'previous_marks': [previous_marks],
        'study_hours': [study_hours]
    })

    prediction = model.predict(data)

    return prediction[0]