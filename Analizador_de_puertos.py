import socket

ip = input("Ingrese la dirección IP que quiera escanear: ")

for puerto in range(1, 65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    result = sock.connect_ex((ip, puerto))  

    if result == 0:
        print("Puerto abierto: " + str(puerto))
    else:
        print("Puerto cerrado: " + str(puerto))

    sock.close()  



