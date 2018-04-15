# file: rfcomm-server.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: simple demonstration of a server application that uses RFCOMM sockets
#
# $Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $

from bluetooth import *
import json
import os
import commands

os.system('echo "discoverable on" | bluetoothctl')

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ]
#                   protocols = [ OBEX_UUID ] 
                    )
                   
print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)

try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        js = json.loads(data)
        print(js['ssid'])
        print(js['password'])
        network = commands.getstatusoutput("wpa_cli -iwlan0 add_network")
        id = network[1]
        commands.getstatusoutput("wpa_cli -iwlan0 set_network %s ssid '\"%s\"'" % (id, js['ssid']))
        commands.getstatusoutput("wpa_cli -iwlan0 set_network %s ssid '\"%s\"'" % (id, js['ssid']))
        commands.getstatusoutput("wpa_cli -iwlan0 set_network %s key_mgmt WPA-PSK" % id)
        commands.getstatusoutput("wpa_cli -iwlan0 set_network %s psk '\"%s\"'" % (id, js['password']))
        commands.getstatusoutput("wpa_cli -iwlan0 enable_network %s" % id)
        commands.getstatusoutput("wpa_cli -iwlan0 save")

        print("received [%s]" % data)
except IOError:
    pass

print("disconnected")

client_sock.close()
server_sock.close()
print("all done")
