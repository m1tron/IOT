import ubinascii              # Conversions between binary data and various encodings
import machine                # To Generate a unique id from processor

# Wireless network
WIFI_SSID =  "Altibox870235"
WIFI_PASS = "YmQs84c3"

# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "m1tron"
AIO_KEY = "aio_fuzY38kOugRc2aJ9Uy9izilKcGyG"
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
AIO_REED_FEED = "m1tron/feeds/reed"
AIO_HUMID_FEED = "m1tron/feeds/humid"
AIO_TEMP_FEED = "m1tron/feeds/temp"
AIO_LOG_FEED = "m1tron/feeds/log"