import socket
import multiprocessing
import re
import rem_03_applications


class MSGIservice():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.socket.bind(("192.168.1.10",7890))
        self.socket.listen(128)


    def runforever(self):
        while True:
            new_socket, client_addr = self.socket.accept()
            request = new_socket.recv(1280).decode("utf-8")
            multi = multiprocessing.Process(target=self.dealrequest,args=(new_socket,request))
            multi.start()
            new_socket.close()


    def dealrequest(self,newsocket,request):
        recvdata = request.splitlines()
        #HTTP2.1 / 200
        ret = re.match(r"[^/]+(/[^ ]*)",recvdata[0])
        fileaddr = ''

        if ret.group(1):
            fileaddr = ret.group(1)
            if fileaddr == '/':
                fileaddr = '/index.html'
            print("fileName == {0}".format(fileaddr))

        if not fileaddr.endswith('.pyy'):
            try:
                p = open("../html" + fileaddr,"rb")
                content = p.read()
                p.close()
            except:
                content = "HTTP/1.1 404 NOT FOUND\r\n"
                content += '\r\n'
                content += 'nihaoya'
                newsocket.send(content.encode("utf-8"))
            else:
                res_head = "HTTP/1.1 200 OK\r\n"
                res_head += '\r\n'
                newsocket.send(res_head.encode("utf-8"))
                newsocket.send(content)
            newsocket.close()

        else:
            # content2 = "HTTP/1.1 200 OK\r\n"
            # content2 += "\r\n"
            dict1 = dict()
            dict1['file'] = fileaddr
            # body = rem_02_application.applictaion(fileaddr)
            body = rem_03_applications.application(dict1,self.start_response)
            header = "HTTP/1.1 %s\r\n" % self.status
            for temp in self.memb:
                header += "%s:%s\r\n" % (temp[0],temp[1])
            header += "\r\n"
            print(header)
            content = header + body
            # content2 += '你好'
            # print("************************")
            # print(content2)
            # print("************************")
            newsocket.send(content.encode("utf-8"))

    def start_response(self,status,memb):
        self.status = status
        self.memb = [('server','mini_frame v8.8 by yujingjing')]
        self.memb += memb


def main():
    MSGI = MSGIservice()
    MSGI.runforever()




if __name__ == '__main__':
    main()