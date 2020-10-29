FROM python:3

ADD src /src

CMD ["python3", "./src/calculatorTests.py"]