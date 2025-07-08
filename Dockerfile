# Use Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install supervisor
RUN apt-get update && apt-get install -y supervisor

# Expose Streamlit UI port
EXPOSE 8501

# Launch both processes via supervisor
CMD ["/usr/bin/supervisord", "-c", "/app/supervisord.conf"]