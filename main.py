from src.data_preprocessing import load_data
from src.train_model import train_model
from src.evaluate_model import evaluate_model
from src.predict import predict_score

import matplotlib.pyplot as plt
import seaborn as sns


def generate_graphs(df):

    sns.heatmap(df.corr(), annot=True)

    plt.title("Correlation Heatmap")

    plt.savefig("images/heatmap.png")

    plt.close()

    plt.scatter(df["study_hours"],
                df["exam_score"])

    plt.xlabel("Study Hours")

    plt.ylabel("Exam Score")

    plt.title("Study Hours vs Exam Score")

    plt.savefig("images/scatter_plot.png")

    plt.close()


def main():

    df = load_data("data/students.csv")

    generate_graphs(df)

    model, X_test, y_test = train_model(df)

    evaluate_model(model, X_test, y_test)

    predicted_score = predict_score(
        attendance=85,
        previous_marks=80,
        study_hours=4
    )

    print("\nPredicted Exam Score:",
          round(predicted_score, 2))


if __name__ == "__main__":
    main()