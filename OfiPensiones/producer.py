# #!/usr/bin/env python
# import time
# import pika
# from random import uniform

# rabbit_host = 'host'
# rabbit_user = 'monitoring_user'
# rabbit_password = 'isis2503'
# exchange = 'ofipensiones_recibos'
# topic = 'InstitucionA.Recibo'

# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
# channel = connection.channel()

# channel.exchange_declare(exchange=exchange, exchange_type='topic')

# print('> Sending recibos. To exit press CTRL+C')

# cant = 0
# while cant < 300:
#     valor = round(uniform(1000000, 1000000000), 1)
#     payload = "{'valor':%r,'tipo':'Cobro','estado':'Generado'}" % (valor)
#     channel.basic_publish(exchange=exchange, routing_key=topic, body=payload)
#     print("Recibo de %s con valor de: %r" % (topic.split('.')[0], valor))
#     cant+=1
#     time.sleep(1)

# connection.close()

#!/usr/bin/env python
import time
import pika
from random import uniform

rabbit_host = '10.128.0.13'
rabbit_user = 'ofipensiones_user'
rabbit_password = 'ofipensiones'
exchange = 'ofipensiones_recibos'
topic = ['InstitucionA.Recibo','InstitucionB.Recibo','InstitucionC.Recibo','InstitucionD.Recibo','InstitucionE.Recibo']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

print('> Sending recibos. To exit press CTRL+C')

cant = 0
while cant < 300:
    for i in range(len(topic)):
        valor = round(uniform(1000000, 1000000000), 1)
        payload = "{'valor':%r,'tipo':'Cobro','estado':'Generado'}" % (valor)
        channel.basic_publish(exchange=exchange,
                            routing_key=topic[i], body=payload)
        print("Recibo de %s con valor de: %r" % (topic[i].split('.')[0], valor))
        time.sleep(0.2)
    cant+=1

connection.close()