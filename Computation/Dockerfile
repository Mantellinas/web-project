# FROM python:3.8.11-alpine3.14

# WORKDIR /app

# COPY . . 

# RUN pip --no-cache-dir install -r requirements.txt

# ENV PYTHONUNBUFFERED=0

# EXPOSE 3000

# CMD ["python", "-u", "graph_server.py"]

FROM python:3.9

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app


ENV PYTHONUNBUFFERED=0

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]


CMD ["graph_server.py" ]