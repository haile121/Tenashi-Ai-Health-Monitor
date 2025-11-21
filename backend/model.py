# model utilities: training and inference helpers
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib


MODEL_PATH = "anomaly_model.joblib"


def train_model(df):
    # train IsolationForest on heart_rate and blood_oxygen
    X = df[["heart_rate", "blood_oxygen"]].values
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(X)
    joblib.dump(model, MODEL_PATH)
    return model


def load_model():
    # load model if exists else None
    try:
        return joblib.load(MODEL_PATH)
    except Exception:
        return None


def predict_anomaly(model, heart_rate, blood_oxygen):
    # return True if anomaly detected
    x = np.array([[heart_rate, blood_oxygen]])
    pred = model.predict(x)
    return bool(pred[0] == -1)
