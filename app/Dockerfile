# base image to build from - slim variant is a minimal python install, smaller image size
FROM python:3.11-slim

# set the working directory inside the container - all future commands run from here
WORKDIR /app

# copy requirements.txt from host machine into the container's /app directory
COPY requirements.txt .

# install python dependencies inside the container (installs flask)
RUN pip install -r requirements.txt

# copy app.py from host machine into the container's /app directory
COPY app.py .

# documents that the container listens on port 5000 (informational, doesn't actually open the port)
EXPOSE 5000

# the command that runs when the container starts
CMD ["python", "app.py"]