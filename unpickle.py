import joblib

# Load the object directly using joblib
model = joblib.load('./student_model.pkl')

# Print the model to verify it loaded
print(model)
print("Type:", type(model))
