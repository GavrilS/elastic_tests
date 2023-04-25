FROM python:3.11-bullseye

WORKDIR /src

COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "src/test_logger.py" ]

CMD [ "--log_type", "info" ]
