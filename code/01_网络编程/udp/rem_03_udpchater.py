import socket


def sendmeg(socket):
    send_message = input("请输入要发送的消息")
    destination_ipaddr = input("请输入目的地址")
    destination_port = int(input("请输入目的端口"))
    destination = (destination_ipaddr,destination_port)
    socket.sendto(send_message.encode("gbk"),destination)


def recvmeg(socket):
    recvdate = socket.recvfrom(1024)
    print(recvdate)
    print("%s : %s" % (str(recvdate[1]),recvdate[0].decode("gbk")))


def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    loceladdr = ("",7890)
    udp_socket.bind(loceladdr)
    while True:
        print("*********upd聊天器*********")
        print("**********请选择***********")
        print("********1.发送数据*********")
        print("********2.接收数据*********")
        print("********3.退出程序*********")
        choose = input()
        if choose == '1':
            sendmeg(udp_socket)
        if choose == '2':
            recvmeg(udp_socket)
        if choose == '3':
            break
        else:
            print("error")
    udp_socket.close()



if __name__ == "__main__":
    main()