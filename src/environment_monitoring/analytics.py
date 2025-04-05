
"""AI/ML Module - Enhanced Predictive Analytics Models"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import joblib

def preprocess_data(X):
    """Scale the dataset for better performance"""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler

def train_linear_model(X, y):
    """Train a simple linear regression model"""
    model = LinearRegression()
    model.fit(X, y)
    return model

def train_random_forest_model(X, y, n_estimators=100):
    """Train a Random Forest regression model"""
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=42)
    model.fit(X, y)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model using MSE and R²"""
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    return {"mse": mse, "r2": r2}

def save_model(model, filepath):
    """Save the trained model to a file"""
    joblib.dump(model, filepath)

def load_model(filepath):
    """Load a model from a file"""
    return joblib.load(filepath)
