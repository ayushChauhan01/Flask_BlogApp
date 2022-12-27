From python:3.10.9
WORKDIR /app
ADD ./app
RUN pip install -r requirement.txt
Expose 5000
CMD ["python", "main.py"]