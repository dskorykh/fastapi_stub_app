FROM python:3.10-slim-bullseye

WORKDIR "/app"
COPY requirements.txt requirements.txt
RUN ["pip", "install", "-r", "requirements.txt"]

COPY fastapi_app.py fastapi_app.py
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8888", "fastapi_app:app"]
