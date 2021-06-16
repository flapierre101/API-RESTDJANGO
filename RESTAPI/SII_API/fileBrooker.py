import paho.mqtt.client as mqtt
import os, urllib.parse, os.path
import json
import base64
from datetime import date

class connectionMQTT():

    def __init__(self, url, topic):
        self.mqttc = mqtt.Client()
        self.url = urllib.parse.urlparse(url)
        self.topic = topic

        self.connection()

    def on_message(self, client, obj, msg):

        from .models import Sii_Api
        from rest_framework.parsers import JSONParser

        udata = json.loads(msg.payload.decode("utf-8"))

        print(type(udata), udata)

        self.updateDB(udata)

    def updateDB(self, msg):

        from SII_API.serializers import ApiSerializer
        from rest_framework.parsers import JSONParser
        from django.http.response import JsonResponse
        from rest_framework import status

        serial = ApiSerializer(data=msg)
        data = None

        if serial.is_valid():
            if(data == None):
                serial.save()
            print('post du message venant du brooker dans la db avec succès!')
        else:
            print('erreur au niveau du post du message du brooker dans la db')
            print(serial.errors)

    def connection(self):
        # Connect
        print('je me connecte au brooker')
        self.mqttc.username_pw_set(self.url.username, self.url.password)
        self.mqttc.connect(self.url.hostname, self.url.port)

        # Start subscribe, with QoS level 0
        self.mqttc.subscribe(self.topic, 0)
        self.mqttc.on_message = self.on_message

    def transformJSON(message):
        with open('brooker/data.json', 'w') as outfile:
            json.dump(message, outfile)