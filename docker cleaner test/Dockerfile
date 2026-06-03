FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt . 
RUN pip install -r requirements.txt 
COPY main.py . 
COPY Data/ ./Data/
ENTRYPOINT ["python","main.py"]