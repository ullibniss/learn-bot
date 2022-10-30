FROM python:3.8

WORKDIR /opt/app

#RUN useradd -s /bin/bash -m -u 1000 learnbot && \
#    groupadd -g 1000 learnbot \
#    chown -R 1000:1000 /opt/app \

COPY requirements.txt .
RUN pip install -r requirements.txt && \
    mkdir bot

COPY bot ./bot

CMD ["python3.8", "bot/bot.py"]
