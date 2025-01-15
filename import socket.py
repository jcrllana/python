import socket
import nmap

# Escanear puertos abiertos en una dirección IP
# para instalar el modulo nmap, ejecutar desde PS: pip install python-nmap
def scan_ports(ip_address):
    nm = nmap.PortScanner()
    nm.scan(ip_address, arguments="-p-")
    open_ports = []
    for port in nm[ip_address].all_tcp():
        if nm[ip_address].tcp(port)['state'] == 'open':
            open_ports.append(port)
    return open_ports


# Obtener la dirección IP local
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        local_ip = s.getsockname()[0]
    except:
        local_ip = 'No se pudo obtener la dirección IP local'
    finally:
        s.close()
    return local_ip

# Mostrar la dirección IP local
print("La dirección IP local es:", get_local_ip())

# Pedir una dirección IP de destino
dest_ip = input("Introduce la dirección IP de destino:")

# Escanear puertos abiertos en la dirección IP de destino
open_ports = scan_ports(dest_ip)

# Mostrar los puertos abiertos
if len(open_ports) > 0:
    print("Los puertos abiertos en la dirección IP", dest_ip, "son:")
    for port in open_ports:
        print("-", port)
else:
    print("No se han encontrado puertos abiertos en la dirección IP", dest_ip)