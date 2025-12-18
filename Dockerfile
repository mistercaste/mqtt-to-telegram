FROM python:3.9-slim
WORKDIR /app
RUN pip install paho-mqtt pyTelegramBotAPI
COPY monitor.py .
CMD ["python", "monitor.py"]
