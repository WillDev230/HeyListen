from time import sleep
import socket
import network
import machine

# Configura la red Wi-Fi
WIFI_SSID = "PC"
WIFI_PASSWORD = "123456789"
pulsador_pin = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configura la dirección IP y el puerto del servidor al que te conectarás
server_address = ("192.168.137.220", 12345)  # Cambia la dirección IP al del servidor

# Conéctate a la red Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

while not wifi.isconnected():
    pass

print("Conexión Wi-Fi establecida")

# Conéctate al servidor
client_socket.connect(server_address)

try:
    while True:
        # Envía datos al servidor
        if pulsador_pin.value() == 0:  # 0 significa que se presionó el pulsador (debido al resistor pull-up)
            message = "1"
        else:
            message = "2"
        client_socket.send(message.encode('utf-8'))
        sleep(1)
        print(pulsador_pin.value())
except:
    print("esteban puto")
