# -*- coding:UTF-8 -*-
import time
import os
import commands
import subprocess

import pika

parameters = pika.URLParameters('amqp://hardchain:pswHd@localhost:5672/%2F')

connection = pika.BlockingConnection(parameters)
channelr = connection.channel()
#声明queue
channelr.queue_declare(queue='electron3', durable=False)  # 若声明过，则换一个名字
#n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channelr.basic_publish(exchange='xxx',
                      routing_key='electron3',
                      body='test',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                          )
                      )

print(" [x] Sent 'Hello World!'")
connection.close()

