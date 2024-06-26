# -*- coding: utf-8 -*-
"""Logistic_regression_model.ipynb

"""

# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the Titanic dataset
titanic = pd.read_csv('Titanic_train.csv')
titanic

# Dropping unnecessary columns and handling missing values
titanic = titanic.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].mean())
titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].mode()[0])

# Creating dummy variables for categorical columns
titanic = pd.get_dummies(titanic, columns=['Sex', 'Embarked'], drop_first=True)

# Splitting the data into features and target variable
X = titanic.drop('Survived', axis=1)
y = titanic['Survived']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Logistic Regression model
lr = LogisticRegression(max_iter=1000)

# Training the model
lr.fit(X_train, y_train)

# Making predictions
y_pred = lr.predict(X_test)

# Calculating the accuracy
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy of Logistic Regression model:', accuracy)

# Training the model using the entire dataset
lr = LogisticRegression(max_iter=1000)
lr.fit(X, y)

