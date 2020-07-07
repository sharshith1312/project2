import socket
import sys
from termcolor import colored
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# first arg for ipv4 connection and second arg for tcp connection
socket.setdefaulttimeout(2)
# set the default after  two seconds it will print port is closed

# host="192.168.56.1"
# host="100.78.220.50"#mobile ip

# port=445


def portscanner(port):

    
   
    if s.connect_ex((host,port)):
        # print(s.connect_ex((host,port)))
        # similar to s.connect() s.connect_ex() returns a error code if it didn't connect (i.e0 10060)
        # as it didnot connect it returns the error code 10060 it executes this line
        print(colored(f"port {port} is closed",'red'))
    else:
        # if it connects it doesnot output any thing
        print(colored(f"port {port} is open",'green'))


host=input("[+] Enter the ip address: ")









port=int(input("[+] Enter the port to scan :"))
# for port in range(1,200):

#     portscanner(port)
    
portscanner(port)

