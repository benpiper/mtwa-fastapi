FROM python:3-slim
COPY . /
RUN pip3 install -r requirements.txt
EXPOSE 5000/tcp
CMD ["python3", "main.py"]