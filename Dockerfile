FROM python:3.12.4-slim-bookworm


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set Poetry environment variables (prevent it from creating virtualenv)
ENV POETRY_VIRTUALENV_BASE /opt/poetry
ENV POETRY_NO_INTERACTION 1
ENV POETRY_HOME /opt/poetry

# Set the working directory in the container
WORKDIR /app

# Copy only the dependencies definition
COPY pyproject.toml poetry.lock /app/

# Install project dependencies
RUN poetry install --no-dev --no-root

# Copy the entire project
COPY . /app

# Command to run the application
CMD ["poetry", "run", "python", "main.py"]
