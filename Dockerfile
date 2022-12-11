FROM python:3.9
#RUN apt update
# Allows docker to cache installed dependencies between builds
COPY SoftwareDataBase/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Mounts the application code to the image
COPY SoftwareDataBase SoftwareDataBase
ADD .env /env_file/.env
WORKDIR /SoftwareDataBase
RUN python ./manage.py migrate
RUN python manage.py collectstatic
#EXPOSE 8000
