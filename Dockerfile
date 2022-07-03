FROM python:3.7
WORKDIR /api_test_framework
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv lock -r > requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD python3 -m pytest -s --alluredir=allure_results /api_test_framework/tests