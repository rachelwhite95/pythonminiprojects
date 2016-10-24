from mosquitto import *
from serial import *
from random import *

board = Serial("/dev/cu.usbmodemfd111",9600,timeout=2)

client = Mosquitto("RACHEL210")
client.connect("10.212.61.136")

client.subscribe("/lights")

def messageReceived(broker, obj, msg):
    payload = msg.payload.decode()
    print("Message " + msg.topic + " containing: " + payload)
    
    if (payload == "ON"):
        message = "1"
    if (payload == "OFF"):
        message = "0"
    board.write(message.encode())    

client.on_message = messageReceived

while (client != None): client.loop()
