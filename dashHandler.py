from scapy.all import *
from phue import Bridge, Group

MAC_ADDRESS_DICT = {'fc:a6:67:bd:22:a2':"Jacob's Room",

					} # enter Dash Button's MAC Address here.

def detect_button(pkt):
	print "Packet Found"
	if pkt.haslayer(DHCP):
		b = Bridge('192.168.1.103')
		b.connect()
		if pkt[Ether].src in MAC_ADDRESS_DICT.keys(): #Toggle Jacobs Room Lights
			print "Button Press Detected", pkt[Ether].src, MAC_ADDRESS_DICT[pkt[Ether].src] 
			roomGroup = Group(b,MAC_ADDRESS_DICT[pkt[Ether].src])
			roomGroup.on = not roomGroup.on

if __name__ == '__main__':
	print "Starting Sniffs"
	print sniff(prn=detect_button, filter="(udp and (port 67 or 68))", store=0)