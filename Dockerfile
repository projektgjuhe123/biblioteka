# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/projektgjuhe123/biblioteka .

RUN git pull

RUN pip install -r requirements.txt

ENV PATH="$PATH:/home/mac/.local/bin"

EXPOSE 80

EXPOSE 443

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:80/_stcore/health

ENTRYPOINT ["streamlit", "run", "biblioteka.py", "--server.port=80"]
