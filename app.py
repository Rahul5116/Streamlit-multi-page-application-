import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Survey Analyzer", layout="wide")

# Sidebar Navigation
st.sidebar.title("📊 Survey Analyzer")
page = st.sidebar.radio("Navigate to", ["Home", "Upload Survey", "Analyze Data", "Generate Charts"])

# Shared data holder
if "df" not in st.session_state:
    st.session_state.df = None

# Page 1: Home
if page == "Home":
    st.title("📊 Welcome to the Survey Analyzer App")
    st.write("Use this app to upload, analyze, and visualize survey data.")

# Page 2: Upload Survey
elif page == "Upload Survey":
    st.title("📤 Upload Your Survey CSV File")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file:
        st.session_state.df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        st.dataframe(st.session_state.df.head())

# Page 3: Analyze Data
elif page == "Analyze Data":
    st.title("📈 Survey Data Summary")
    if st.session_state.df is not None:
        st.write("**Basic Info:**")
        st.write(st.session_state.df.info())
        st.write("**Descriptive Stats:**")
        st.write(st.session_state.df.describe(include='all'))
    else:
        st.warning("Please upload a file first on the 'Upload Survey' page.")

# Page 4: Generate Charts
elif page == "Generate Charts":
    st.title("📉 Survey Data Visualization")
    if st.session_state.df is not None:
        column = st.selectbox("Choose a column to visualize", st.session_state.df.columns)

        chart_type = st.radio("Select chart type", ["Bar Chart", "Pie Chart"])

        if chart_type == "Bar Chart":
            st.bar_chart(st.session_state.df[column].value_counts())
        else:
            data = st.session_state.df[column].value_counts()
            fig, ax = plt.subplots()
            ax.pie(data, labels=data.index, autopct='%1.1f%%')
            st.pyplot(fig)
    else:
        st.warning("Please upload a file first on the 'Upload Survey' page.")
