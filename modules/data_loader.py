import pandas as pd

def load_data(file):
    try:
        if file.name.endswith('.csv'):
            data = pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            data = pd.read_excel(file)
        else:
            raise ValueError("Unsupported file format.")
        return data
    except Exception as e:
        raise ValueError(f"Error loading data: {e}")