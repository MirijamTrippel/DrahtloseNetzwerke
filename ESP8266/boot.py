# MQTT example boot.py
# Netzwerkverbindung herstellen
# Verbindung zu MQTT Broker aufbauen

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()
print('Free Memory')
print(gc.mem_free())

# MQTT Client ID aus MAC-Adresse generieren
print('MQTT Client ID :')
client_id = ubinascii.hexlify(machine.unique_id())
print(client_id)

last_message = 0

# hier holen wir uns Variablen aus der mysettings.py
from mysettings import mqtt_server as mqtt_server
print('imported mqtt_server as:')
print(mqtt_server)
from mysettings import topic_sub as topic_sub
print('imported topic_sub as:')
print(topic_sub)

#--- import Wlan--------
from secrets import ssid
print('imported ssid as:')
print(ssid)
from secrets import pw as password

# -------------------WIFI Funktionen-------------------------------
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())



# ------------------MQTT Funktionen----------------------------------
def sub_cb(topic, msg):
  print((topic, msg))
  if topic == topic_sub and msg == b'received':
    print('ESP received message')

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  #machine.reset()
#---------------------------------------------------------------
  
do_connect()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

print('Free Memory')
print(gc.mem_free())
