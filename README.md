Network Packet Analyzer

Project Overview:
The Network Packet Analyzer is a Python application that captures and analyzes network packets using Scapy.

Objectives:
Capture network packets from an authorized network interface.
Identify source and destination IP addresses.
Detect common protocols such as TCP, UDP, and ICMP.
Display packet sizes.
Save packet summaries to a CSV file.

Technologies Used:
Python 3
Scapy
CSV
GitHub

Installation:
Install Python 3.
Install Scapy:
bash
python -m pip install scapy
Install Npcap on Windows if required for packet capture.

How to Run:
Run the following command in your terminal:
bash
python packet_analyzer.py
Use the required permissions for packet capture on your operating system.

Output:
The application displays packet timestamps, source IP addresses, destination IP addresses, protocols, and packet sizes. It also creates a CSV report named packets.csv.

Limitations:
Packet visibility depends on the network interface, operating system permissions, and capture configuration. Encrypted network traffic is not automatically decrypted.

Safety:
Use this tool only on your own device or networks you are authorized to analyze.# network-packet-analyzer
Python-based Network Packet Analyzer using Scapy
