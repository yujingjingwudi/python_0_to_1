import socket

def main():
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	service_addr = ("192.168.1.10",7890)
	#发送链接请求
	client_socket.connect(service_addr)
	print("连接成功")
	#发送请求
	filename = input("请输入所需要的文件名")
	client_socket.send(filename.encode("gbk"))
	recedata = client_socket.recv(1024)
	if recedata:
		with open("new"+filename,"wb") as f:
			f.write(recedata)
	print("over")

if __name__ == "__main__":
	main()

