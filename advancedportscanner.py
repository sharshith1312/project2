from socket import *
import optparse
from threading import *
from termcolor import colored
def connScan(tgtHost,tgtPort):
    try:
        sock=socket(AF_INET,SOCK_STREAM)
        sock.connect((tgtHost,int(tgtPort)))
        print(colored(f"[+] Port {tgtPort} is open",'green'))
    except:
        print(colored(f"[-] Port {tgtPort} is closed",'red'))
    finally:
        sock.close()

def portscanner(tgtHost,tgtPorts):
    try:
        tgtIP=gethostbyname(tgtHost)
        # if tgtHost is link it will give ip adress or ip adress it will give ip address
    except:
        print(f"Unknown host {tgtHost}")

    try:
        # if input was given as link
        tgtName=gethostbyaddr(tgtIP)
        # here tagName is a tuple containing address of the ip xample below
        '''
        >>> socket.gethostbyname('www.google.com')
        '172.217.31.196'
        >>> socket.gethostbyaddr('172.217.31.196')
        ('maa03s28-in-f4.1e100.net', [], ['172.217.31.196'])
        '''
        print("[+] scan results for :"+tgtName[-1])
    except:
        # if input was ip
        print("[+] scan results for: "+tgtIP)

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        # usage of Thread takes target as argument which the functun to run and "args" as second
        # argument which takes arguments for the target function
        t=Thread(target=connScan,args=(tgtHost,int(tgtPort)))
        t.start()





def main():
    # usage of optparse
    parser=optparse.OptionParser('Usage of program: '+'-H <target host> -p <target port seperated by commas>')
    parser.add_option('-H',dest='tgtHost',type='string',help="specify target host")
    parser.add_option('-p',dest='tgtPort',type='string',help="specify target port")
    (options,ags)=parser.parse_args()
    tgtHost=options.tgtHost
    
    tgtPorts=str(options.tgtPort).split(',')
    # tgtPorts=list(range(1,1000))
    if (tgtHost==None) or (tgtPorts[0]==None):
        print(parser.usage)
        exit(0)

    portscanner(tgtHost,tgtPorts)


main()



'''
this code is not working properly in python3 for giving ip adress but working fine for when giving website link
try python 2 it will work said by the instructur
'''


# preinstalled kalinux command for find ip "nslookup <website>"