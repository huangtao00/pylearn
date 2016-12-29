
import socket
data="8d890100000100000000000005626169647503636f6d0000010001"
rawdata=bytes.fromhex(data) # dns raw data to get baidu ip
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
DNSserver="202.114.0.242"
s.connect((DNSserver,53))
s.send(rawdata)
recvData=s.recv(266)
print(recvData)