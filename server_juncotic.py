import socket 
import threading
import time

HEADER=512
KEY="12135"
HOST = socket.getHOSTname(socket.getHOSTname())
PORT= 5000
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
serversocket.bind((HOST, PORT))
serversocket.listen()
def handle_client(server):
    print("Servidor iniciado, esperando conexion...")
    socket,addr = server
    n = 0
    disconnect = False
    ip=str(addr)
    
    while True:
        fecha_actual=time.strftime("%c")
        msj = socket.recv(HEADER).decode()
        if msj[0:5]=="start": 
            if n==0:
                name=msj[6:]
                code="200"
                n+=1
            else:
                code="400"
                
                
        if msj[0:5]=="email":
            if n==1:
                email=msj[6:]
                code="200"
                n+=1
            else:
                code="400"
                
                
        if msj[0:3]=="key":
            if n==2:
                key=msj[4:]
                if key==KEY:
                    code="200"
                    n+=1
                else:
                    code="400"
                   
            else:
                code="400"
                
        if msj[0:4]=="quit":
            code="200"
            disconnect=True

        socket.send(code.encode("utf-8"))
        if disconnect:
            data = "%s|%s|%s|%s|%s" % (name,email,fecha_actual,ip,key)
            print(data)
            socket.close()

def start():
    while True:
        clientsocket = serversocket.accept()
        print("Nueva conexion")
        thread = threading.Thread(target=handle_client, args=(clientsocket))
        thread.start()