import re
import socket
import select


def support_service(socket,recvdata):
    # print("连接成功")
    # recvdata = socket.recv(1280).decode("utf-8")
    # print(recvdata)
    #   recvdata = recvdata.decode("utf-8")
    request = recvdata.splitlines()
    ret = re.match(r"[^/]+(/[^ ]*)",request[0])

    fileName = ''

    if ret:
        fileName = ret.group(1)
        if fileName == '/':
            fileName = '/index.html'

    print(fileName)

    try:
        f = open("./html" + fileName,"rb")
    except:
        print("打开文件失败")
        content = "HTTP/1.1 404 NOT FOUND\r\n"
        content += "\r\n"
        content += "niaho"
        socket.send(content.encode("utf-8"))
    else:
        print("打开文件成功")
        content = "HTTP/1.1 200 ok\r\n"
        content += "\r\n"
        socket.send(content.encode("utf-8"))
        socket.send(f.read())
        f.close()
    socket.close()

if __name__ == "__main__":
    service_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # service_socket.setblocking(False)
    service_socket.bind(("",7898))
    service_socket.listen(128)
    # 创建一个epoll对象
    epl = select.epoll()
    # 注册客服套接字
    epl.register(service_socket.fileno(),select.EPOLLIN)
    # 新建一个字典存储文件描述符和套接字的对应关系
    socket_dic = dict()
    # socket_dic[service_socket.fileno()] = service_socket

    while True:
        # epl.poll返回的是一个消息队列，里面存储的是元祖
        fd_list = epl.poll()
        for fd, event in fd_list:
            # 如果文件描述符是客服套接字的文件描述符
            if fd == service_socket.fileno():
                new_socket,client_socket = service_socket.accept()
                # 注册新的套接字
                epl.register(new_socket.fileno(),select.EPOLLIN)
                socket_dic[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                recvdata = socket_dic[fd].recv(1024).decode("utf-8")
                if recvdata:
                    support_service(socket_dic[fd],recvdata)
                else:
                    socket_dic[fd].close()
                    epl.unregister(socket_dic[fd])
                    del socket_dic[fd]