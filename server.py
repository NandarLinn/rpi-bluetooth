from bluetooth import *
import subprocess
import time

def client_connect():

    client_sock, address = server_sock.accept()
    print("Accepted connection from ", address)

    try:
        data = client_sock.recv(1024)
        print("recieve [%s]" %data.decode())
        
        if data:
            ## Make Another process ##
            print("## Make some process here ##")
            client_sock.send(bytes("Process done", encoding='utf-8'))
            client_sock.close()
    except IOError:
        pass

while True:
    subprocess.call(['sudo', 'hciconfig', 'hci0', 'piscan'])
    server_sock = BluetoothSocket(RFCOMM)
    server_sock.bind(("",1))
    server_sock.listen(2)

    print("Waiting for connection on RFCOMM channel")
    client_connect()
    print("disconnected")
    server_sock.close()