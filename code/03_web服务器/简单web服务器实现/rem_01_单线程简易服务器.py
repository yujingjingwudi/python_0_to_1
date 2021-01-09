import socket
import re

def dowork(new_socket):
    #print('*'*50)

    request = new_socket.recv(1280).decode("utf-8")
    #print(request)
    request_list = request.splitlines()
    # GET / HTTP/1.1
    ret = re.match(r"[^/]+(/[^ ]*)",request_list[0])
    file_name = ''
    if ret:
        # print(ret.group(1))
        file_name = ret.group(1)
        if file_name == '/':
            file_name = '/index.html'

    print("filename==" + file_name)

    try:
        f = open('./html'+ file_name,"rb")
        content = f.read()
        f.close()
    except:
        # print("555555555555555555555")
        content = "HTTP/1.1 404 NOT FOUND\r\n"
        content += '\r\n'
        content += "NO"
        new_socket.send(content.encode("utf-8"))
    else:
        # header和body分两次发比较好，格式方便统一
        send_file = "HTTP/1.1 200 OK\r\n"
        send_file += "\r\n"
        new_socket.send(send_file.encode("utf-8"))
        new_socket.send(content)
    new_socket.close()


def main():
    service_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    local_Addr = ("",7890)
    service_socket.bind(local_Addr)
    service_socket.listen(128)
    while True:
        new_socket,client_socket = service_socket.accept()
        dowork(new_socket)


if __name__ == "__main__":
    main()