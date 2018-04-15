import commands
import json

js = json.loads('{"ssid":"TP-LINK_yanyue_1", "password":"yy249670295"}')
print(js['ssid'])
print(js['password'])
print(commands.getstatusoutput('wpa_cli -iwlan0 add_network'))
network = commands.getstatusoutput("wpa_cli -iwlan0 add_network")
id = network[1]
commands.getstatusoutput("wpa_cli -iwlan0 set_network %s ssid '\"%s'\"" % (id, js['ssid']))
commands.getstatusoutput("wpa_cli -iwlan0 set_network %s key_mgmt WPA-PSK" % id)
commands.getstatusoutput("wpa_cli -iwlan0 set_network %s psk '\"%s\"'" % (id, js['password']))
commands.getstatusoutput("wpa_cli -iwlan0 enable_network %s" % id)
commands.getstatusoutput("wpa_cli -iwlan0 save")
