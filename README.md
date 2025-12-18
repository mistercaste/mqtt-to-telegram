# mqtt-telegram-security
A Docker container listening to an MQTT bus, and sending notifications to Telegram when spotting items maked as vulnerable.

## Docker Compose
```                                                                            
# MQTT alerts to Telegram                                                                                                             
  mqtt-telegram-security:                                                                                                             
    container_name: mqtt-telegram-security                                                                                            
    image: mistercaste/mqtt-telegram-security:latest                                                                                   
    restart: unless-stopped                                                                                                           
    environment:                                                                                                                      
      - TELEGRAM_TOKEN=your_token
      - TELEGRAM_CHAT_ID=your_chat_id
      - MQTT_BROKER=192.168...
      - MQTT_PORT=1883
      - MQTT_TOPIC=security/#    # Monitors all sub-topics of security
      - MQTT_USER=my_username
      - MQTT_PASS=********
```

## Testing MQTT
You can test the setup by sending a manual message to the MQTT broker:
```
mosquitto_pub -h localhost -t "security/vulnerabilities" -m "Test: Found exploit CVE-2023-XXXX"
```
