from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score


def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    r2 = r2_score(y_test, predictions)

    print("\nModel Evaluation")
    print("----------------")
    print("Mean Absolute Error:", round(mae, 2))
    print("R2 Score:", round(r2, 2))

    return predictions