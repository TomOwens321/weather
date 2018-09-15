#!/usr/bin/env python
import pyownet
import json
import time
import paho.mqtt.client as mqtt

hosts = ['greenhousepi.ourhouse']

def mqtt_connect(host='picloud.ourhouse', port=1883, keepalive=60):
  client = mqtt.Client('pytemps')
  client.connect(host,port)
  return client

def mqtt_publish(topic,payload):
  #client = mqtt_connect()
  client.publish(topic, payload=payload, qos=0, retain=False)
  #client.disconnect()

def log_message(message):
  topic = 'sun-chaser/logs/pytemps'
  message = "[{}] pytemps : {}".format(time.asctime(),message)
  print(message)
  mqtt_publish(topic, message)

def simple_temperature(owclient,host,path):
  topic = "sun-chaser/temperature/{}/{}".format(host,owclient.read(path + "alias"))
  payload = owclient.read(path + "temperature")
  mqtt_publish(topic,payload)

client = mqtt_connect()

def loop():
  for host in hosts:
    try:
        owp = pyownet.protocol.proxy(host)
        log_message("Checking for therms on: {}".format(host))
        dir = owp.dir('/')
        alarm = owp.dir('/alarm')

        for d in dir:
          spath = d + "temperature"
          if owp.present(spath):
            simple_temperature(owp,host,d)
            log_message("{} : {}".format(spath.ljust(32), owp.read(spath)))

        for a in alarm:
          log_message("{} : ALARM!".format(a.ljust(32)))
    except:
        print("owhost connection failure.")

while True:
  loop()
  time.sleep(60)
