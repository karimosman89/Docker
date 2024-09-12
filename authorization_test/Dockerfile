FROM python:3.9

WORKDIR /app

COPY authorization_test.py /app/authorization_test.py
RUN pip install requests

CMD ["python", "authorization_test.py"]
