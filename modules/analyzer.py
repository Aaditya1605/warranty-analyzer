import pandas as pd

def analyze_data(data):
    try:
        
        failure_rate = data.groupby('part_id')['issue_code'].count() / len(data)
        analysis_results = pd.DataFrame({
            'Part ID': failure_rate.index,
            'Failure Rate': failure_rate.values
        })
        return analysis_results
    except Exception as e:
        raise ValueError(f"Error analyzing data: {e}")