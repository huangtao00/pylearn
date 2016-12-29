import IN,socket,sys
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

MAX=65535

PORT =1060

s.connect(("192.168.1.1",PORT))

s.setsockopt(socket.IPPROTO_IP,IN.IP_MTU_DISCOVER,IN.IP_PMTUDISC_DO)
try:
        s.send("#"*1400)
except socket.error:
    print "message did not make it"
    option=getattr(IN,"IP_MTU",14)
    print "MTU:",s.getsockopt(socket.IPPROTO_IP,option)
else:
    print "the big message was sent! Your network supports really big packet"