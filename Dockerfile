FROM python:3.10.2

WORKDIR /usr/src/task

RUN pip install Django

COPY . /usr/src/task/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
