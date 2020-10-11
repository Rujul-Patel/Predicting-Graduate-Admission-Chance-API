FROM python:3.8-slim
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -U pip && pip install -r requirements.txt
COPY . /app
RUN ["python","model/model.py"] 
ENTRYPOINT ["gunicorn","app.wsgi:app"]
