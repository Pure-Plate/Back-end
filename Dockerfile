FROM python:3.9.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /pure_plate

COPY . /pure_plate/.

# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Expose the port the app runs on
EXPOSE 80

# Command to run on container start
CMD python manage.py runserver
# gunicorn --bind 0.0.0.0:8000 pure_plate.wsgi:application

