import socket
import select
import random

buff = 1024

PORT = random.randint(1250, 8509)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.1.5", 8509))
s.listen(5)
print("Server is online !")
print("The port is {0}".format(PORT))

delay = 0.04
connected_clients = []

while True:
	request, wlist, xlist = select.select([s], [], [], delay)
	for connection in request:
		clientsocket, address = connection.accept()
		connected_clients.append(clientsocket)

	read_client = []
	try:
		read_client, wlist, xlist = select.select(connected_clients,[], [], delay)
	except select.error:
		pass
	else:
		for client in read_client:
			msg = client.recv(buff)
			print(msg)
			if msg == "quit'":
				client.close()
				break
			else:
				lenght = len(connected_clients)
				print(msg)

				for count in range(0, lenght):
					connected_clients[count].send(msg)
					print(connected_clients[count])


for client in connected_clients:
	print("Bye {0}".format(client))
	client.close()

	#clientsocket.send(b"Bienvenue !")
	#print("Somebody joined the server !")
	
	



		
			
			







	



