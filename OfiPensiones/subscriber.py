import json
import pika
from sys import path
from os import environ
import django

rabbit_host = '10.128.0.13'
rabbit_user = 'ofipensiones_user'
rabbit_password = 'ofipensiones'
exchange = 'ofipensiones_recibos'
topics=['InstitucionA.#','InstitucionB.#','InstitucionC.#',
        'InstitucionD.#','InstitucionE.#','InstitucionF.#',
        'InstitucionG.#','InstitucionH.#','InstitucionI.#',
        'InstitucionJ.#','InstitucionK.#','InstitucionL.#',
        'InstitucionM.#','InstitucionN.#','InstitucionO.#']


path.append('OfiPensiones/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'OfiPensiones.settings')
django.setup()

from recibos.logic.logic_recibo import create_recibo_object
from recibos.services.services_recibos import check_alarm
from instituciones.services.services_instituciones import get_institucion

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

for topic in topics:
    channel.queue_bind(
        exchange=exchange, queue=queue_name, routing_key=topic)

print('> Waiting recibos. To exit press CTRL+C')

recibos = []
def callback(ch, method, properties, body):
    global id
    payload = json.loads(body.decode('utf8').replace("'", '"'))
    recibos.append(payload)
    topic = method.routing_key.split('.')
    institucion = get_institucion(topic[0])
    create_recibo_object(
        institucion, payload['valor'], payload['tipo'], payload['estado'])
    if institucion.name == 'Temperature':
        check_alarm(payload['valor'])
    print("Recibo :%r" % (str(payload)))
    print(len(recibos))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()