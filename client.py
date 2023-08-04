from socket import*
hostname=gethostname()
ip="127.0.0.1"
ClientSocket=socket(AF_INET,SOCK_DGRAM)
addr=(ip,1234)
c="Y"
while c.upper() == "Y":
 req=input("ENTER DOMAIN NAME FOR WHICH THE IP IS NEEDED:")
 send=ClientSocket.sendto(req.encode(),addr)
 message,serveraddress=ClientSocket.recvfrom(1024)
 reply=message.decode().strip()
 print(f"THE IP FOR THE DOMAINNAME{req}:{reply}")
 c=(input("CONTINUE?(Y/N)"))
ClientSocket.close()
