#!/usr/bin/env python
import time
import pika
from random import uniform

rabbit_host = 'host'
rabbit_user = 'monitoring_user'
rabbit_password = 'isis2503'
exchange = 'ofipensiones_recibos'
topic = 'InstitucionA.Recibo'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

print('> Sending recibos. To exit press CTRL+C')

cant = 0
while cant < 300:
    valor = round(uniform(1000000, 1000000000), 1)
    payload = "{'valor':%r,'tipo':'Cobro','estado':'Generado'}" % (valor)
    channel.basic_publish(exchange=exchange, routing_key=topic, body=payload)
    print("Recibo de %s con valor de: %r" % (topic.split('.')[0], valor))
    cant+=1
    time.sleep(1)

connection.close()