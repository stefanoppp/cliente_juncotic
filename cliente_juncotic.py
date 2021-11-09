import socket
import argparse

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

argumentos = argparse.ArgumentParser(description="Cliente")
argumentos.add_argument('-h', "--host", required = True, default="127.0.0.1", help='Host')
argumentos.add_argument('-p', '--puerto', required=True, default=47980,help='Puerto')

parse = argumentos.parse_args()
HOST = parse.host
PORT = parse.port

cliente.connect((HOST, PORT))

while True:
    datos=[]
    
    name = "start|{}".format(input(f"Ingrese su nombre: "))

    datos.append(name)
    
    email = "email|{}".format(input(f"Ingrese su email: "))
    
    datos.append(email)
    
    key = "key|{}".format(input(f"Ingrese su clave: "))
    
    datos.append(key)
    
    exit_input=input("Ingrese 'quit' para cerrar el cliente: ")

    datos.append(exit_input)
    
    def envio(datos):
        for i in datos:
            cliente.send(i.encode())
            status = cliente.recv(1024)
            print(status.decode())
    cliente.close()
    envio(datos)
    break