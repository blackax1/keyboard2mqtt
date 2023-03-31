import paho.mqtt.client as mqtt
import hid
import time

# Connect to the broker
client = mqtt.Client()

# Set a flag to indicate that the loop is running
running = True

# While the flag is True, run the loop
while running:

        # Get the keyboard's current scan codes
	#hid.Devoce(vendor_id,product_id)
        scan_codes = hid.Device(18498,1).read(8)

        #fix scancodes
        byte_str = ''.join(chr(n) for n in scan_codes[1:])
        result_str = byte_str.split('\x00')

        # Connect and Publish a message to the "keyboard" topic with the scan codes
        client.connect("mqtt.blackax.net") #Set your MQTT broker 
        client.publish("keyboard2mqtt", str(result_str))

        # Sleep for 1 second
        time.sleep(.2)
