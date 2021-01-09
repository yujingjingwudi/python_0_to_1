import socket
import gevent
from gevent import monkey
import re

monkey.patch_all()


def deal_request(socket, data):
    request = data.splitlines()
    # GET / HTTP1.1
    ret = re.match(r"[^/]+(/[^ ]*)",request[0])
    file_name = ''
    if ret:
        file_name = ret.group(1)
        if file_name == '/':
            file_name = '/index.html'
    print(file_name)
    print('.html' + file_name)
    try:
        f = open('./html' + file_name, "rb")
        content = f.read()
        f.close()
    except Exception as e:
        content = "HTTP/1.1 404 NOT FOUND\r\n"
        content += "Content-Length:5\r\n"
        content += "\r\n"
        content += "error"
        print("没有这个网页")
        socket.send(content.encode("utf-8"))
    else:
        print("有这个网页")
        send_content_body = content
        send_content = "HTTP/1.1 200 OK\r\n"
        # COnteent-Length的目的是告诉浏览器数据传输完毕
        send_content += "Content-Length:%d\r\n" % len(send_content_body)
        print(len(send_content_body))
        send_content += "\r\n"
        socket.send(send_content.encode("utf-8"))
        socket.send(content)


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server_socket.bind(('', 7890))
    server_socket.listen(128)
    server_socket.setblocking(False)
    socket_list = list()

    while True:
        try:
            new_socket, client_addr = server_socket.accept()
        except:
            pass
        else:
            new_socket.setblocking(False)
            socket_list.append(new_socket)

        for i in socket_list:
            try:
                recv_data = i.recv(1280).decode("utf-8")
            except:
                pass
            else:
                if recv_data:
                    deal_request(i, recv_data)
                else:
                    i.close()
                    socket_list.remove(i)


if __name__ == '__main__':
    main()