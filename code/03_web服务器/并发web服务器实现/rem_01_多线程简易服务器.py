import socket
import multiprocessing
import re


def support_service(socket):
    # print("连接成功")
    recvdata = socket.recv(1280).decode("utf-8")
    print(recvdata)
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



def main():
    service_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    local_addr = ("",7890)
    service_socket.bind(local_addr)
    service_socket.listen(128)
    while True:
        new_socket,client_addr = service_socket.accept()
        m1 = multiprocessing.Process(target=support_service,args=(new_socket,))
        m1.start()
        new_socket.close()
        # support_service(socket)


if __name__ == "__main__":
    main()