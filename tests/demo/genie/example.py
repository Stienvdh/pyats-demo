from genie.conf import Genie
from genie.utils import Dq
from genie.testbed import load
import json

tb = load('testbed/sandbox-device.yaml')       # Load our testbed file from a file.
dev = tb.devices['internet-rtr01']       # Define an object called dev from the device named csr1000v

dev.connect()      # Connect to the object dev we defined earlier -  this must be done before parsing to the device

routingTable = dev.parse('show ip route')        # Run the command "show ip route" on the device and parse the output to JSON

routes = routingTable['vrf']['default']['address_family']['ipv4']['routes']

if "0.0.0.0/0" in routes:
   print("Default gateway is: " + routes["0.0.0.0/0"]['next_hop']['next_hop_list'][1]['next_hop'])
else:
   print("No default gateway is set")