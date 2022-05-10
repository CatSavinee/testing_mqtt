import paho.mqtt.client as mqtt
host = "broker.mqttdashboard.com"
port = 8000

def calculation():
    sum = 1+6
    return sum

while True:
    client = mqtt.Client()
    client.connect(host)
    client.publish("TEST/MQTT/CCC", 'today is the beautiful day')
