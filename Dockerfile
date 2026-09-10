#docker image hai
FROM python:3.11-slim    


WORKDIR /Health_system


COPY ./requirements.txt /Health_system/requirements.txt
RUN pip install --no-cache-dir -r /Health_system/requirements.txt


# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /Health_system/app


# CMD ["fastapi", "run", "app/main.py", "--port", "80"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]




