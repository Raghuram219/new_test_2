FROM python:3.10.0

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    postgresql-client \
    libjpeg-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    python3-dev \
    tzdata \
    zlib1g-dev \
    libpq-dev \
    gcc \
    libssl-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    libxslt1-dev \
    libblas-dev \
    liblapack-dev \
    gfortran \
    dos2unix \
    && rm -rf /var/lib/apt/lists/*

COPY req.txt .

RUN pip install setuptools==67.8.0 
RUN pip install -r req.txt

COPY . .

# FIX: line endings + permission (ONLY ONCE, before ENTRYPOINT)
RUN dos2unix /app/django.sh && \
    chmod +x /app/django.sh

# Optional optimization
RUN python -m compileall -b /app \
    && find /app -name "*.py" -not -name "django.sh" -delete

EXPOSE 8000

ENTRYPOINT ["/app/django.sh"]