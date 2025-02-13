# Use an official Python runtime as a parent image
FROM python:3.11

# Create a non-root user with a UID between 10000 and 20000
RUN groupadd -g 10001 appgroup && \
    useradd -m -u 10001 -g appgroup appuser

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

# Ensure /app/data exists and has the correct ownership and permissions
RUN mkdir -p /app/data && \
    chown -R appuser:appgroup /app/data && \
    chmod -R 777 /app/data

# Set the user to the non-root user
USER 10001

# Expose the port FastAPI runs on
EXPOSE 8080

# Run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
