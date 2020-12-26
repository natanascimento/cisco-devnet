#specify the version of python
FROM python:3.7

#specify the port for the docker release
EXPOSE 8501

# making app as the container directory
WORKDIR /usr/src/app

# copying dependencies
COPY requirements.txt ./

# installing dependencies
RUN pip install -r requirements.txt

# Copying all files of current directory for container directory
COPY . .