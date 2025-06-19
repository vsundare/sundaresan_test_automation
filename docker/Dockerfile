FROM python:3.9-slim

# Set environment variables
ENV ALLURE_RESULTS_DIR=/app/allure-results
ENV ALLURE_REPORT_DIR=/app/allure-report

# Define the application's directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Allure command-line tool
RUN apt-get update &&\
    apt-get install -y openjdk-11-jre-headless wget &&\
    wget -qO - https://dl.bintray.com/qameta/generic/io.qameta.allure/allure/<allure-version>/allure-<allure-version>.tgz | tar -xz -C /opt/ &&\
    ln -s /opt/allure-<allure-version>/bin/allure /usr/bin/allure

# Expose the application port
EXPOSE 5000

# Run tests and start app
CMD sh -c   "mkdir -p ${ALLURE_RESULTS_DIR} &&
            pytest --alluredir=${ALLURE_RESULTS_DIR} test_app.py &&
            allure generate ${ALLURE_RESULTS_DIR} -o ${ALLURE_REPORT_DIR} --clean && python app.py"