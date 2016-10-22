#coding=utf-8

import sys
import urllib
import urllib2
import re
import os
import time
import random
import socket
import signal
import threading
import math
import time
import socket
import SocketServer
#from time import ctime,sleep



#reload(sys)
#sys.setdefaultencoding("utf-8")


def tcp_client():
    HOST = '127.0.0.1'
    PORT = 8000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while(True):
        msg = raw_input('input:')
        try:
            s.sendall(msg)
            print 'client send:%s' % (msg)
        except:
            print 'server exit'
            break

    s.close()

 

class TCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while(True):
            try:
                data = self.request.recv(1024)
                if(len(data) == 0):#client exit
                    #print 'client exit'
                    break
                else:
                    print 'Raspberry car: %s' % (data)
                    response = 'From Raspberry car: %s' % (data)
                    self.request.sendall(response)
                #time.sleep(1)
            except:
                #print 'client exit'
                break


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 8000
    server = SocketServer.ThreadingTCPServer((HOST, PORT), TCPHandler)
    print 'Tcp Server start listening...'
    server.serve_forever()

 
    


