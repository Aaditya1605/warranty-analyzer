import streamlit as st
from modules.data_loader import load_data
from modules.analyzer import analyze_data
from modules.ml_model import detect_anomalies
from modules.reporting import generate_report

def main():
    st.title("Warranty Analyzer")
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Menu", ["Upload Data", "Analyze Data", "Detect Fraud", "Generate Report"])

    if menu == "Upload Data":
        st.header("Upload and Validate Data")
        uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])
        if uploaded_file:
            data = load_data(uploaded_file)
            st.write("Data Preview:")
            st.write(data)

    elif menu == "Analyze Data":
        st.header("Component Failure Rate Analysis")
        data = st.session_state.get("data")
        if data is not None:
            analysis_results = analyze_data(data)
            st.write("Analysis Results:")
            st.write(analysis_results)
        else:
            st.warning("Please upload data first.")

    elif menu == "Detect Fraud":
        st.header("Anomaly Detection")
        data = st.session_state.get("data")
        if data is not None:
            anomalies = detect_anomalies(data)
            st.write("Detected Anomalies:")
            st.write(anomalies)
        else:
            st.warning("Please upload data first.")

    elif menu == "Generate Report":
        st.header("Export Reports")
        data = st.session_state.get("data")
        if data is not None:
            report_path = generate_report(data)
            st.success(f"Report generated: {report_path}")
        else:
            st.warning("Please upload data first.")

if __name__ == "__main__":
    main()