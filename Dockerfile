FROM python:3.10-alpine
WORKDIR /code
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install flask
EXPOSE 5000
COPY main.py .
CMD ["flask", "run"]
