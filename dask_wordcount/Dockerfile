FROM python:3.9.8-slim-buster

# Set working directory
WORKDIR /app

# Copy dask_wordcount folder into working directory
COPY . /app

# Create and active virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Dask using pip
RUN pip install dask[complete]