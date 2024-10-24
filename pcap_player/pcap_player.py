from scapy.all import *
import time
import sys

# python3 pcap_player.py <path/to/pcap/file> <destination.v4.ip.address>

if __name__ == '__main__':

	pcap_file = rdpcap(sys.argv[1])
	
	print("PCAP File contents:")
	print(pcap_file)
	
	# set the start time to the time the first packet was send.
	start_time = pcap_file[0].time

	for packet in pcap_file:
	
		# Calculate delay time (will be 0 at first iteration)
		delay = float(packet.time) - start_time
		print("Waiting for delay time to pass... (" + str(delay) + " s)")
		# computers can't calculate, so lets just assume delay time is 0 when value is negative.
		if delay < 0:
			delay = 0
		# delay like it was delayed originally
		time.sleep(float(delay))
		# Update the start time
		start_time = float(packet.time)
	
		print(packet)
	
		# create a new packet with the payload of the old one.
		new_packet = packet.payload
		new_packet[IP].dst = sys.argv[2]
	
		# delete the packet checksum.
		# del new_packet[UDP].chksum
	
		# print and send the new packet
		print(new_packet)
		send(new_packet)

