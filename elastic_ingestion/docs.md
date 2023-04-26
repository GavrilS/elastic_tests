# This is a sample for elastic ingestion. Taken from this repository - https://github.com/GavrilS/container_env/tree/main/python_logger

- Commands for building and running the container:
  docker build --tag elastic_python .

- Command to run the container with the arguments in the CMD command in the dockerfile
  docker run --volume="C:\Users\Gari\Desktop\Projects\container_env_test\python_logger\logs:/src/logger/" --network=elastic elastic_python

- Command to run the container with new arguments provided when running the container
  docker run --volume="C:\Users\Gari\Desktop\Projects\container_env_test\python_logger\logs:/src/logger/" --network=elastic elastic_python --log_type error
