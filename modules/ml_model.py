from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(data):
    try:
        model = IsolationForest(random_state=42)
        numeric_data = data.select_dtypes(include=['number']).dropna()
        model.fit(numeric_data)
        data['Anomaly'] = model.predict(numeric_data)
        anomalies = data[data['Anomaly'] == -1]
        return anomalies
    except Exception as e:
        raise ValueError(f"Error detecting anomalies: {e}")