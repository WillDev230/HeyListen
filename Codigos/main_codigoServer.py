import socket
import network
from machine import Pin
import time
led = Pin(2,Pin.OUT)
# Configura la red Wi-Fi
WIFI_SSID = "PC"
WIFI_PASSWORD = "123456789"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configura la dirección IP y el puerto en el que el servidor escuchará conexiones
server_address = ('192.168.137.220', 12345)  # Puedes cambiar el puerto si es necesario

server_socket.bind(server_address)
server_socket.listen(1)

print("Servidor escuchando en {}:{}".format(server_address[0], server_address[1]))

# Conéctate a la red Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

while not wifi.isconnected():
    pass

print("Conexión Wi-Fi establecida")

# Espera la conexión del cliente
print("Esperando la conexión del cliente...")
client_socket, client_address = server_socket.accept()
print("Cliente conectado desde {}:{}".format(client_address[0], client_address[1]))

try:
    while True:
        # Recibe datos del cliente
        data = client_socket.recv(1024)
        if data.decode('utf-8')=="1":
            led.on()
            print("NOOO")
            time.sleep(1)
        else:
            led.off()
        if data:
            print("Mensaje recibido del cliente: {}".format(data.decode('utf-8')))
        else:
            break

finally:
    client_socket.close()
