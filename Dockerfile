# Use an official Python runtime as a parent image
FROM python:3.11

# Create a non-root user and group
RUN groupadd -g 1001 appgroup && \
    useradd -m -u 1001 -g appgroup appuser

# Set the working directory in the container
WORKDIR /app

# Change ownership of the working directory to the non-root user
RUN chown -R appuser:appgroup /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies as root
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Set the user to the non-root user
USER appuser

# Expose the port FastAPI runs on
EXPOSE 8080

# Run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
