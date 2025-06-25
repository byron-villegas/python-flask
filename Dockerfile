FROM python:3.12-slim

# Create app directory
WORKDIR /app

# Copy app
COPY . .

# Update package list
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Environment variables for flask
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Start the application
CMD ["flask", "run"]