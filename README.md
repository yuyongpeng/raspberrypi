# raspberrypi

$ sudo apt-get install rabbitmq-server
$ sudo systemctl enable rabbitmq-server.service
$ sudo systemctl start rabbitmq-server.service
$ pip install pika
$ sudo rabbitmqctl add_user hardchain pswHd
$ sudo rabbitmqctl set_user_tags hardchain administrator
$ sudo rabbitmqctl set_permissions -p / hardchain ".*" ".*" ".*"

