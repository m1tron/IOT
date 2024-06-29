import dht
import machine

import time

reed_switch = machine.Pin(26, machine.Pin.IN)
tempSensor = dht.DHT11(machine.Pin(27))     # DHT11 Constructor 

while True:
    try:
        reed_value = reed_switch.value()
        if reed_value == 1:
            print("Magnet Detected...")
        else:
            print("No Magnetic Field...")

        tempSensor.measure()
        temperature = tempSensor.temperature()
        humidity = tempSensor.humidity()
        print("Temperature is {} degrees Celsius and Humidity is {}%".format(temperature, humidity))
        

    except Exception as error:
        print("Exception occurred", error)
    time.sleep(2)