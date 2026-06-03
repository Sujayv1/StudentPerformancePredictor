from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib


def train_model(df):

    X = df[['attendance', 'previous_marks', 'study_hours']]
    y = df['exam_score']

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()

    model.fit(X_train, y_train)

    joblib.dump(model, "student_model.pkl")

    return model, X_test, y_test