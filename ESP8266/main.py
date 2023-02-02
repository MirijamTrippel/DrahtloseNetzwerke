# MQTT example
#main.py

#------- DHT22 ----------

#----------- Sensor --------------
import dht
from mysettings import DHT22PIN as DHT22PIN

# ------- Werte abhängig vom Sensor---------------
from mysettings import message_interval as message_interval
print('imported message_interval as:')
print(message_interval)
from mysettings import temp_topic as temp_topic
print('imported temp_topic as:')
print(temp_topic)
from mysettings import humi_topic as humi_topic
print('imported humi_topic as:')
print(humi_topic)

print('Free Memory')
print(gc.mem_free())

d=dht.DHT22(machine.Pin(DHT22PIN))
try:
    print('First Measurement ...')
    d.measure()
    tem="temp:%s" % d.temperature()
    hum="humi:%s" % d.humidity()
    print(tem)
    print(hum)
except:
    print('Exception measure ...')
    time.sleep(5)

print('---------Start Measurement-----------')
while True:
  try:
    client.check_msg() #
    if (time.time() - last_message) > message_interval:
        #msg = b'Hello #%d' % counter
        # Messwert vom DHT Sensor
        d.measure()
        tem=b'temp:%s' % d.temperature()
        hum=b'humi:%s' % d.humidity()
        print(tem)
        print(hum)
        print('Free Memory')
        print(gc.mem_free())
        client.publish(temp_topic, tem)
        client.publish(humi_topic, hum)
        last_message = time.time()
  except OSError as e:
      print(e)
      restart_and_reconnect()
