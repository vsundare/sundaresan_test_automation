FROM python:3.12-slim
RUN mkdir -p /app/
WORKDIR /app

# Copy everything from the context provided by docker-compose.yml
COPY /app/ /app/

# Copy requirements from the relative path
COPY docker/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "/app/src/flask_area_calculator/app.py"]