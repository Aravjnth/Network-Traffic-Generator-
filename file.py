import scapy.all as scapy

def network_traffic_generator(ip_src, ip_dst, port_src, port_dst):
    packet = scapy.IP(src=ip_src, dst=ip_dst) / scapy.TCP(sport=port_src, dport=port_dst)
    scapy.send(packet, iface=scapy.conf.iface)  # Use scapy.conf.iface to get the default interface

network_traffic_generator("192.168.1.1", "192.168.1.2", 1234, 80)