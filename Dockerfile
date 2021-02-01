FROM python:3.8

WORKDIR /usr/src/datashop/app

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV FLASK_ENV=development
ENV FLASK_ENV=run.py
EXPOSE 5000
CMD ["python","run.py"]