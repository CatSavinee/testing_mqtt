import paho.mqtt.client as mqtt
import pymongo
host = "broker.mqttdashboard.com"
port = 8000

def on_connect(self, client, userdata, rc):
    print("MQTT Connected.")
    self.subscribe("TEST/MQTT/CCC")

def on_message(client, userdata,msg):
    print(msg.payload.decode("utf-8", "strict"))
    #b = a.upper()
    #print(b)
    #client.publish("TEST/MQTT/CCC", b)
    
def on_database(client, userdata,msg):
    myclient = pymongo.MongoClient("mongodb+srv://micedb:dbdbdbdb@micetestcluster.hawt0.mongodb.net/test")
    mydb = myclient["test_db"]
    mycol = mydb["testtetstete"]

    mydict = msg.payload.decode("utf-8", "strict")

    mycol.insert_one(mydict)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host)
client.loop_forever()
