# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time
import os
import commands
import subprocess

import pika


GPIO.setmode(GPIO.BCM)

#GPIO.setup(24, GPIO.IN, pull_up_dwon=GPIO.PUD_DOWN)
GPIO.setup(4, GPIO.IN)
R=13
G=19
B=26
GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

pwmR = GPIO.PWM(R, 70)
pwmG = GPIO.PWM(G, 70)
pwmB = GPIO.PWM(B, 70)

pwmR.start(0)
pwmG.start(0)
pwmB.start(0)

ledStatus = 0

def my_callback(channel):
    print("button pressed!")
    os.chdir('/home/pi/electron-quick-start')
    #os.system('electron .')
    #print commands.getstatusoutput('electron .')
    global ledStatus 
    ledStatus = ledStatus + 1
    parameters = pika.URLParameters('amqp://hardchain:pswHd@localhost:5672/%2F')
    
    connection = pika.BlockingConnection(parameters)
    channelr = connection.channel()
    #声明queue
    channelr.queue_declare(queue='electron', durable=True)  # 若声明过，则换一个名字
    #n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
    channelr.basic_publish(exchange='',
                          routing_key='electron',
                          body='Hello World!',
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                              )
                          )
    
    print(" [x] Sent 'Hello World!'")
    connection.close()
    pass
    #subprocess.call(['electron','.'],shell=True)

GPIO.add_event_detect(4, GPIO.RISING, callback=my_callback)

while True:
    try:
        if ledStatus % 2 == 1:
            pwmR.ChangeDutyCycle(0)
            pwmG.ChangeDutyCycle(100)
            pwmB.ChangeDutyCycle(100)
        else:
            pwmR.ChangeDutyCycle(0)
            pwmG.ChangeDutyCycle(0)
            pwmB.ChangeDutyCycle(100)

        #print("I'm working...")
        time.sleep(1)
        pass
    except KeyboardInterrupt:
        break
        pass
    pass


pwmR.stop()
pwmG.stop()
pwmB.stop()
GPIO.cleanup()
