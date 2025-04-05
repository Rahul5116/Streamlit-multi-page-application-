# Base Python image
FROM python:3.9

# Set working directory in container
WORKDIR /app

# Copy all files
COPY . .

# Install required Python packages
RUN pip install -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Start the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
