FROM python:3.7
WORKDIR /api_test_framework/
COPY .env Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --ignore-pipfile
CMD pipenv shell
CMD python -m pytest -s --alluredir=allure_results/ /api_test_framework/tests/