import os
import joblib
import pandas as pd


class WineQualityPredictor:

    def __init__(self):

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        model_path = os.path.join(BASE_DIR, "artifacts", "best_model.pkl")
        scaler_path = os.path.join(BASE_DIR, "artifacts", "scaler.pkl")

        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)

        self.feature_names = [
            "fixed acidity",
            "volatile acidity",
            "citric acid",
            "residual sugar",
            "chlorides",
            "free sulfur dioxide",
            "total sulfur dioxide",
            "density",
            "pH",
            "sulphates",
            "alcohol"
        ]

    def predict(self, features):

        df = pd.DataFrame([features], columns=self.feature_names)

        scaled = self.scaler.transform(df)

        prediction = self.model.predict(scaled)[0]

        confidence = self.model.predict_proba(scaled).max() * 100

        return prediction, confidence