FROM python:3.8-slim

# Set the working directory
WORKDIR /

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8051", "--server.address=0.0.0.0"]