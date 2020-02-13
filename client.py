import socket
import time

buff = 1024

Ident = input("Ident : ")
username = input("Enter your name : ")
args = Ident.split(":")
HOTE = args[0]
PORT = args[1]
print(HOTE, PORT)
print("Connection....")
time.sleep(1)




# Création du socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP Protocol
try:

    # Connexion au server
    connection = (str(HOTE), int(PORT))
    s.connect(connection)
    print("Sucessfully connected ! [DEV] : {0}".format(connection))
    # Récéption des packets
    while True:

        # Envoie de packets
        message = input(">>>> ")
        s.send(username.encode('utf-8') + b" >>> " + message.encode('utf-8'))
        msg = s.recv(buff)
        msg = msg.decode()
        print(msg)

# Si la connexion est refusée :
except ConnectionRefusedError:
    print("The connection to the server failed ! {0}".format(connection))
    quit = input()

# Si le serveur ne répond pas :
except TimeoutError:
    print("Connection failed ! The server doesn't reply to the request ! IPv4 : {0[0]}".format(connection))
    quit = input()










