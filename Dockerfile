# Use official Python 3.9 image
FROM python:3.11-slim


COPY . /app
# Set working directory
WORKDIR /app
 
RUN pip install -r requirements.txt

# Expose the port Streamlit runs on
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
