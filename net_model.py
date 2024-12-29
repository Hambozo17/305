# net_model.py

import joblib
import os

class NetTrafficModel:
    def __init__(self, model_path='net_model.pkl'):
        if not os.path.exists(model_path):
            raise FileNotFoundError("Network model file not found.")
        data = joblib.load(model_path)
        self.model = data['model']
        self.feature_names = data['feature_names']

    def predict_request_type(self, features):
        # features: a dict like {"ip_rate": 3, "user_agent_score": 0.5, ...}
        # Convert to the correct feature order/array
        X = [[features.get(name, 0) for name in self.feature_names]]
        prediction = self.model.predict(X)
        return prediction[0]  # "normal" or "suspicious"
