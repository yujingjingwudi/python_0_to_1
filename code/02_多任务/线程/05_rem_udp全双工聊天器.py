import threading
import socket



class send_thread(threading.Thread):
    def __init__(self,socket,ip,port):
        # 必须要调用thread的初始化函数，如果要执行构造函数的话
        threading.Thread.__init__(self)
        self.sock = socket
        self.ip = ip
        self.port = port


    def run(self):
        while True:
            message = input("请输入要发送的消息：")
            self.sock.sendto(message.encode("gbk"),(self.ip,self.port))


class recv_thread(threading.Thread):
    def __init__(self,socket,ip,port):
        threading.Thread.__init__(self)
        self.sock = socket
        self.ip = ip
        self.port = port



    def run(self):
        while True:
            # data传回来的数据是一个元组，元组第一个元素时消息，第二个元素时发送方地址
            data = self.sock.recvfrom(1024)
            print("收到来自%s %s的消息：" % (str(data[1]),data[0].decode("gbk")))


def main():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    client_socket.bind(("",8080))
    t1 = send_thread(client_socket,"192.168.1.10",7890)
    t2 = recv_thread(client_socket, "192.168.1.10", 7890)
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()