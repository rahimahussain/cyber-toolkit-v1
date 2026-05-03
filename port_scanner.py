import socket

target = input("Target IP or domain: ")

ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

print("\n" + "="*40)
print(f" SCANNING: {target}")
print("="*40 + "\n")

open_ports = []

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    if sock.connect_ex((target, port)) == 0:
        print(f"[OPEN] Port {port}")
        open_ports.append(port)

    sock.close()

print("\n" + "-"*40)
print(" SCAN COMPLETE")
print(f" Open ports: {open_ports}")
print("-"*40)