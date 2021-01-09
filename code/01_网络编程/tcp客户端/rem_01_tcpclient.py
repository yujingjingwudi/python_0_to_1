import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    destination_addr = ("192.168.1.10",8080)
    tcp_socket.connect(destination_addr)
    tcp_socket.send("你今天吃了没".encode("gbk"))
    recvDate = tcp_socket.recv(1024)
    print("%s"%(recvDate.decode("gbk")))
    tcp_socket.close()



if __name__ == "__main__":
    main()