import sqlite3
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(("localhost" , 9999))

server.listen()
print("✅ Server listening on port 9999...")
def handle_connection(c):
    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    c.send("Password: ".encode())
    password = c.recv(1024).decode()

    password = hashlib.sha256(password.encode()).hexdigest()

    connection = sqlite3.connect("userdata.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM userdata WHERE username = ? AND password = ?" , (username, password))

    if cursor.fetchall():
        c.send("Login Successful!".encode())
    else:
        c.send("Login Failed!".encode())

while True:
    client , address = server.accept()
    threading.Thread(target= handle_connection, args=(client,)).start()