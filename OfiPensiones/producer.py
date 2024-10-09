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

while True:
    valor = round(uniform(1000000, 1000000000), 1)
    payload = "{'valor':%r,'tipo':'Cobro','estado':'Generado'}" % (valor)
    channel.basic_publish(exchange=exchange, routing_key=topic, body=payload)
    print("Recibo con valor de: %r" % (valor))
    time.sleep(1)

connection.close()