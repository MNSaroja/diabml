import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
df = pd.read_csv('diabetes.csv')

# Define features and target
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

# Train the model
model = LogisticRegression()
model.fit(X, y)

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
