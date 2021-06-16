from .fileBrooker import connectionMQTT

print('salut')

mqtt = connectionMQTT('mqtt://ghhtzpps:MwVNHJbYYirC@driver-01.cloudmqtt.com:18760', '/C64/Projet/#')

mqtt.mqttc.loop_start()