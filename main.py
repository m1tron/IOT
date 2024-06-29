import dht
import machine

import time                   # Allows use of time.sleep() for delays
from mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
import machine                # Interfaces with hardware components
import micropython            # Needed to run any MicroPython code
import keys                   # Contain all keys used here
import wifiConnection         # Contains functions to connect/disconnect from WiFi 


tempSensor = dht.DHT11(machine.Pin(27))     # DHT11 Constructor 

TEMP_INTERVAL = 20000
last_temp_sent = 0  # milliseconds

# Function to temp to Adafruit IO MQTT server at fixed interval
def send_temp_humid():
    global last_temp_sent
    global TEMP_INTERVAL

    if ((time.ticks_ms() - last_temp_sent) < TEMP_INTERVAL):
        return; # Too soon since last one sent.
    try:
        tempSensor.measure()
        temperature = tempSensor.temperature()
        humidity = tempSensor.humidity()
        log_str = "Temperature is {} degrees Celsius and Humidity is {}%".format(temperature, humidity)

        print("Publishing: {0} to {1} ... ".format(temperature, keys.AIO_TEMP_FEED), end='')
        #print("Publishing: {0} to {1} ... ".format(humidity, keys.AIO_HUMID_FEED), end='')
        client.publish(topic=keys.AIO_TEMP_FEED, msg=str(temperature))
        #client.publish(topic=keys.AIO_HUMID_FEED, msg=str(humidity))
        #client.publish(topic=keys.AIO_LOG_FEED, msg=str(log_str))
        print("DONE")

    except Exception as e:
        print("FAILED")
        print(e)
    finally:
        last_temp_sent = time.ticks_ms()


reed_switch = machine.Pin(26, machine.Pin.IN)
REED_INTERVAL = 20000
last_reed_sent = 0  # milliseconds

def send_reed():
    global last_reed_sent
    global REED_INTERVAL

    if ((time.ticks_ms() - last_reed_sent) < REED_INTERVAL):
        return; # Too soon since last one sent.
    try:
        reed_value = reed_switch.value()
        print("Publishing: {0} to {1} ... ".format(reed_value, keys.AIO_REED_FEED), end='')
        client.publish(topic=keys.AIO_REED_FEED, msg=str(reed_value))
        print("DONE")
    except Exception as e:
        print("FAILED")
    finally:
        last_reed_sent = time.ticks_ms()
    


# Try WiFi Connection
try:
    ip = wifiConnection.connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(keys.AIO_CLIENT_ID, keys.AIO_SERVER, keys.AIO_PORT, keys.AIO_USER, keys.AIO_KEY)

# Subscribed messages will be delivered to this callback
#client.set_callback(sub_cb)
client.connect()
#client.subscribe(keys.AIO_LIGHTS_FEED)
#print("Connected to %s, subscribed to %s topic" % (keys.AIO_SERVER, keys.AIO_LIGHTS_FEED))



try:                      # Code between try: and finally: may cause an error
                          # so ensure the client disconnects the server if
                          # that happens.
    while 1:              # Repeat this loop forever
        #client.check_msg()# Action a message if one is received. Non-blocking.
        send_temp_humid()     # Send a random number to Adafruit IO if it's time.
        send_reed()
        time.sleep(2)
finally:                  # If an exception is thrown ...
    client.disconnect()   # ... disconnect the client and clean up.
    client = None
    wifiConnection.disconnect()
    print("Disconnected from Adafruit IO.")