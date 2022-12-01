FROM python:3.8

WORKDIR /validbitcoinaddress

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./telegram ./telegram

CMD ["python" , "./telegram/main.py"]
