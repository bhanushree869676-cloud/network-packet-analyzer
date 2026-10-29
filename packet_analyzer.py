
from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP
from datetime import datetime
import csv

FILE_NAME = "packets.csv"
PACKET_LIMIT = 50


def analyze_packet(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst
    elif IPv6 in packet:
        src = packet[IPv6].src
        dst = packet[IPv6].dst
    else:
        src = "N/A"
        dst = "N/A"

    if TCP in packet:
        protocol = "TCP"
    elif UDP in packet:
        protocol = "UDP"
    elif ICMP in packet:
        protocol = "ICMP"
    else:
        protocol = "Other"

    size = len(packet)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(
        f"{timestamp} | {src} -> {dst} | "
        f"{protocol} | {size} bytes"
    )

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, src, dst, protocol, size])


def main():
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Timestamp", "Source IP", "Destination IP",
            "Protocol", "Packet Size"
        ])

    print("Network Packet Analyzer started.")
    print(f"Capturing up to {PACKET_LIMIT} packets.")
    print("Press Ctrl+C to stop early.")

    try:
        sniff(prn=analyze_packet, count=PACKET_LIMIT, store=False)
    except KeyboardInterrupt:
        print("\nCapture stopped.")
    except Exception as error:
        print(f"Capture error: {error}")

    print(f"Packet report saved to {FILE_NAME}")


if __name__ == "__main__":
    main()
