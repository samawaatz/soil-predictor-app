import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load the dataset
df = pd.read_csv(r"C:\Users\Samawaat\soil_data.csv")

# Features and target
# Features and target
X = df.drop("Category", axis=1)
y = df["Category"]


# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
with open("soil_model.pkl", "wb") as f:
    pickle.dump(model, f)
print(df.columns)


