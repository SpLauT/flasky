FROM python:alpine

EXPOSE 5000

COPY * /app/

WORKDIR /app

RUN pip install -r requirements.txt
ENV FLASK_APP=flasky.py

ENTRYPOINT [ "flask" ]

CMD ["run", "--host=0.0.0.0"]