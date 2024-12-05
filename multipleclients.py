import threading
import socket

def handle_client(client_socket):
	while True:
		msg = client_socket.recv(1024).decode("utf-8")
		if not msg:
			break
		print(f"Recieved: {msg}")
		client_socket.send(f"Echo: {msg}".encode("utf-8"))
	     	client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))
serverr.listen(5)

print("Server is listening on port 9999...")
wlile True:
	client_socket, addr = server.accept()
	print(f"Connection from {addr}")
	client_thread =threading.Thread(target=handle_client, args=(client_socket,))
	client_thread.start()
