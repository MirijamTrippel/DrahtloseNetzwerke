# topics, pins & settings

# Datenpin des DHT Senors
#bei ESP32 pin 21, bei nodeMCU pin 4, bei ESP8266-01 pin 2
#D2 = PIN 4
DHT22PIN=4

# BMP280 Pins
sclPin=22
sdaPin=21

# Messintervall in sek
message_interval = 20

mqtt_server = '10.10.10.199' # oder Webadresse
#mqtt_server = "192.168.0.217"

#temp_topic = b'HTWIoT/temp/572665'
#humi_topic = b'HTWIoT/humi/572665'
temp_topic = b"Home/Temperature"
humi_topic = b"Home/Humidity"
#pres_topic = b'HTWIoT/pres/572665'
# Subscription topic für nodes um Nachrichten an sie zu senden
topic_sub = b'Projektwoche/notification'
