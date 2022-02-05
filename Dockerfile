FROM python:3.8.8
ENV UNA_SERVICE=/una
RUN mkdir -p $UNA_SERVICE
RUN mkdir -p $UNA_SERVICE/static
RUN mkdir -p $UNA_SERVICE/logs
WORKDIR $UNA_SERVICE
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY . .
RUN cat requirements.txt|xargs pip install
ENV PATH="${PATH}:/root/.local/bin"
