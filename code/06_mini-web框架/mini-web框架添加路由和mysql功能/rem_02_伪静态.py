# encoding: utf-8
import socket
import multiprocessing
import re
import sys


class MSGIservice():
    def __init__(self,port,app,static_path):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.socket.bind(("192.168.1.10",port))
        self.socket.listen(128)
        self.application = app
        self.static_path = static_path


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

        if not fileaddr.endswith('.html'):
            try:
                p = open(self.static_path + fileaddr,"rb")
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
            body = self.application(dict1,self.start_response)
            header = "HTTP/1.1 %s\r\n" % self.status
            for temp in self.memb:
                header += "%s:%s\r\n" % (temp[0],temp[1])
            header += "\r\n"
            print(header)
            content = header + body

            newsocket.send(content)

    def start_response(self,status,memb):
        self.status = status
        self.memb = [('server','mini_frame v8.8 by yujingjing')]
        self.memb += memb


def main():
    print(1)
    # 打开配置文件，里面存放着静态资源和动态资源的路径
    with open("web_server.conf","r") as f:
        # eval将字符串
        path = eval(f.read())
        print(path)


    if (len(sys.argv)==3):
        try:
            port = int(sys.argv[1])
            frame = sys.argv[2]
            print(port,frame)
        except Exception as ex:
            print(2)
            print(3)
        else:
            #mini_web:application
            ret = re.match(r"([^:]+):(.*)", frame)
            if ret:
                print(ret.group(1),ret.group(2))
                frameName = ret.group(1)
                funcName = ret.group(2)
                # path = {'static_path':'./static','dynamic_path':'./frameword'}
                sys.path.append(path['dynamic_path'])
                # frameName = mini_web
                # funcName = application
                ff = __import__(frameName)
                app = getattr(ff,funcName)
                msig = MSGIservice(port,app,path['static_path'])
                msig.runforever()
            else:
                print("error")

    else:
        print("您的输入不正确")


if __name__ == '__main__':
    main()