#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

def publick():

        sock = socket.socket()
        sock.connect(('localhost', 9090))
        sock.send(b'publick')
        data = sock.recv(4096)
        sock.close()
        return data.decode('utf-8')


def private():
 
        sock = socket.socket()
        sock.connect(('localhost', 9090))
        sock.send(b'private')
        data = sock.recv(4096)
        sock.close()
        return data.decode('utf-8')
