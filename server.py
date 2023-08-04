from socket import*
dns_table={"www.google.com":"192.165.1.1","www.youtube.com":"192.165.1.2","www.python.org":"192.165.1.3"}
ServerSocket=socket(AF_INET,SOCK_DGRAM)
print("STARTING SERVER.")
ServerSocket.bind(("127.0.0.1",1234))
while True:
  message,clientaddress=ServerSocket.recvfrom(1024)
  print(f"{clientaddress}wants to fetch data!")
  modifiedMessage=message.decode()
  ip=dns_table.get(modifiedMessage,"NOT FOUND!").encode()
  send=ServerSocket.sendto(ip,clientaddress)
