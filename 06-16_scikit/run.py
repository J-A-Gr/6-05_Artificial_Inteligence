from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()
# X, y = iris.data, iris.target
 
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
 
# labai svarbu susipažinti su duomenimis
print(df.head())
print(df.describe())
print(df.info())
 
# Plot some data
import matplotlib.pyplot as plt
import seaborn as sns
 
# print(sns.load_dataset("titanic"))
 
sns.pairplot(df, hue='target', markers=["o", "s", "D"])
plt.show()
 
# DUomenys sutvarkyti # ir paruošti mokymui
from sklearn.model_selection import train_test_split
 
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_test, y_train, y_test  = train_test_split(df, df['target'], test_size=0.20, random_state=42, stratify=df['target'])
# strify=df['target'] - tai svarbu, kad duomenys būtų subalansuoti
print(X_train.shape)
print(X_test.shape)
 
from sklearn.linear_model import LogisticRegression
 
model = LogisticRegression()
model.fit(X_train, y_train) # Treniravimas (training)
# Model evaluation
from sklearn.metrics import accuracy_score, confusion_matrix
y_pred = model.predict(X_test) # Predicting(Inference) Spejimas
 
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)
 