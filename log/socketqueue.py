# -*- coding: utf-8 -*-

import socket
import syslog

import socket_util

BUFSIZE = 10240


class SocketServer(object):

    def __init__(self,ip,port):

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_util.close_socket_inheritance(self.socket)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((ip,port))
        self.socket.listen(5)
 
    def close(self):

        self.socket.close()
 
    def get(self, block = True, timeout = None):

        self.connection,self.address = self.socket.accept()
        try:
            if timeout != None:
                self.connection.settimeout(timeout)
            buf = self.connection.recv(BUFSIZE).strip()
        except socket.timeout:
            syslog.syslog(syslog.LOG_ERR,"SocketQueue get buf error!")
            self.connection.close()
            return False,''

        self.connection.close()
        return True,buf
 
    def put(self, item, block=True, timeout=None):
        
        pass

