# Use an official Python runtime as a parent image
FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false


WORKDIR /opt/project

# Copy the current directory contents into the container at /app
COPY . /opt/project

# Install dependencies with Poetry
RUN poetry install


