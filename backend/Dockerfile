# Use official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only requirements first (for Docker caching)
COPY backend/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend source code
COPY backend/ .

# Expose FastAPI default port
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
