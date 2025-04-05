# 📊 Survey Analyzer App (Streamlit + Docker)

A multi-page **Streamlit** app that allows users to upload survey data, analyze it, and visualize trends using charts — all inside a Docker container.


LIVE DEMO - https://fxyn8ouvnmodhdilheqbsy.streamlit.app/

---

## 🚀 Features

- ✅ Upload `.csv` files
- 📈 Analyze uploaded data using `pandas`
- 📉 Generate bar and pie charts
- 🧭 Multi-page sidebar navigation
- 🐳 Fully containerized with Docker

---

## 📂 Folder Structure

```
survey-analyzer-app/
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── annual-enterprise-survey-2023-financial-year-provisional.csv
```

---

## 🧪 Dataset Used

**File:** `annual-enterprise-survey-2023-financial-year-provisional.csv`  
**Source:** [New Zealand Government Stats](https://www.stats.govt.nz/)  
**Description:** Official statistics with financial performance data of different sectors for 2023. Includes industry type, income, profit, and more.

---

## 🛠 How to Run with Docker

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/survey-analyzer-app.git
cd survey-analyzer-app
```

### 2. Build Docker Image

```bash
docker build -t survey-analyzer .
```

### 3. Run Docker Container

```bash
docker run -p 8501:8501 survey-analyzer
```

Then go to 👉 [http://localhost:8501](http://localhost:8501)

---

## 🐞 Common Error & Solution

### ❌ ERROR

```text
ERROR: failed to read dockerfile: open Dockerfile: no such file or directory
```

### ✅ FIX
- Ensure the file is named `Dockerfile` (exact spelling, no extension).
- Run `docker build` from the folder that contains the Dockerfile:
  
```bash
cd survey-analyzer-app
docker build -t survey-analyzer .
```

---

## 📦 requirements.txt

```txt
streamlit
pandas
matplotlib
```

---

## 📜 Dockerfile

```dockerfile
FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 🧠 app.py

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Survey Analyzer", layout="wide")

# Sidebar for navigation
page = st.sidebar.selectbox("Select a page", ["Home", "Upload Survey", "Analyze Data", "Generate Charts"])

# Global variable to store uploaded file
if 'df' not in st.session_state:
    st.session_state.df = None

# Page 1: Home
if page == "Home":
    st.title("📊 Survey Analyzer")
    st.markdown("""
    Welcome to the **Survey Analyzer App** built using Streamlit + Docker!  
    Upload any CSV file with survey data and analyze it visually across multiple pages.
    """)

# Page 2: Upload
elif page == "Upload Survey":
    st.title("📁 Upload Survey Data")
    file = st.file_uploader("Upload a CSV file", type=["csv"])

    if file:
        df = pd.read_csv(file)
        st.session_state.df = df
        st.success("File uploaded successfully!")
        st.dataframe(df.head())

# Page 3: Analyze
elif page == "Analyze Data":
    st.title("📊 Data Summary")
    if st.session_state.df is not None:
        st.subheader("Info:")
        buffer = []
        st.session_state.df.info(buf=buffer.append)
        st.text('\n'.join(buffer))

        st.subheader("Description:")
        st.write(st.session_state.df.describe())
    else:
        st.warning("Please upload a CSV file first.")

# Page 4: Charts
elif page == "Generate Charts":
    st.title("📈 Generate Charts")

    if st.session_state.df is not None:
        cols = st.session_state.df.select_dtypes(include=['object', 'category']).columns.tolist()

        if cols:
            column = st.selectbox("Select a categorical column", cols)
            chart_type = st.radio("Select chart type", ["Bar", "Pie"])

            if chart_type == "Bar":
                st.subheader("Bar Chart")
                chart_data = st.session_state.df[column].value_counts()
                st.bar_chart(chart_data)

            elif chart_type == "Pie":
                st.subheader("Pie Chart")
                fig, ax = plt.subplots()
                st.session_state.df[column].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
                ax.set_ylabel("")
                st.pyplot(fig)
        else:
            st.warning("No categorical columns found to plot.")
    else:
        st.warning("Please upload a CSV file first.")
```

---

## ✅ Pages in the App

- **Home:** Intro & overview
- **Upload Survey:** Upload `.csv` file & view raw data
- **Analyze Data:** Summary using `.info()` and `.describe()`
- **Generate Charts:** Visualize any categorical column (bar & pie)

---

## 📃 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Stats NZ Dataset](https://www.stats.govt.nz/)

---


