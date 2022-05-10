import paho.mqtt.client as mqtt
host = "broker.mqttdashboard.com"
port = 8000

def on_connect(self, client, userdata, rc):
    print("MQTT Connected.")
    self.subscribe("TEST/MQTT/CCC")

def on_message(client, userdata,msg):
    a = msg.payload.decode("utf-8", "strict")
    b = a.upper()
    print(b)
    #client.publish("TEST/MQTT/CCC", b)
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host)
client.loop_forever()