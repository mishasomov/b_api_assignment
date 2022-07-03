# API tests

#Starting Tests in Docker
Docker container build and start commands look like:

`docker build -t pytest_runner .`

`docker run --rm -it --mount type=bind,source="$(pwd)",target=/api_test_framework/ pytest_runner`