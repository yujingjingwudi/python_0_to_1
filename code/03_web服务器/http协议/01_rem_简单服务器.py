import socket


def servier(new_socket):
    request = new_socket.recv(1280)
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    response += "<h1>nihao</h1>"
    new_socket.send(response.encode("utf-8 "))


def main():
    service_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    local_addr = ("",7890)
    service_socket.bind(local_addr)
    service_socket.listen(128)
    while True:
        new_socket,client_addr = service_socket.accept()
        servier(new_socket)
        new_socket.close()
    service_socket.close()


if __name__ == "__main__":
    main()