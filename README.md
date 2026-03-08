# DDOS-Simulation
DDoS attack simulation and Wireshark analysis, HTTP Flood Simulation and TCP SYN Traffic Simulation.
# DDoS Attack Simulation and Analysis
# DDoS Attack Simulation and Network Traffic Analysis

## Overview

This project demonstrates simulated Distributed Denial of Service (DDoS) attack patterns using Python scripts and analyzes the generated network traffic using Wireshark.

The purpose of this experiment is to understand how abnormal traffic patterns appear in packet capture tools and how they can be identified for network security analysis.

---

## Attacks Simulated

### 1. HTTP Flood Simulation

Multiple threads continuously send HTTP requests to a local server to simulate high web traffic.

### 2. TCP SYN Traffic Simulation

Repeated TCP connection requests are generated to demonstrate SYN traffic patterns.

---

## Tools Used

* Python
* Wireshark
* GitHub
* VS Code

---

## Repository Structure

attack1_http_flood.py → Python script for HTTP flood simulation
attack2_tcp_syn_simulation.py → Python script for TCP SYN traffic generation
screenshots/ → Wireshark packet capture screenshots

---

## Learning Outcome

This experiment demonstrates how excessive network traffic can be detected and analyzed using packet capture tools. The captured packets reveal patterns similar to real-world DDoS attacks.

---

## Author

Name: Your Name
Course: Network Security
