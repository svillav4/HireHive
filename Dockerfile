FROM python:3.12

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /HireHive

COPY . /HireHive/

RUN apt-get update && \
    apt-get install -y gettext && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
