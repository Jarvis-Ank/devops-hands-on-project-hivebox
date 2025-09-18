# Use an official Python runtime as a parent image
FROM python:3.12-slim 

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .

#creating a user other than root
# Combined into a single RUN instruction
RUN pip install --no-cache-dir -r requirements.txt \
    && adduser --disabled-password --gecos '' appuser

# Copy the current directory contents into the container at /app
COPY . .

USER appuser

# Start FastAPI app 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#CMD ["python", "hivebox_app.py"] // Phase 3 changes
