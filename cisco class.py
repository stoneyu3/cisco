#coding=utf-8
import os
import sys
import paramiko

class device(object):
    def __init__(self,host=None,username=None,password=None,enable_password=None):
        self.host = host
        self.username = username
        self.password = password
        self.enable_passwod = enable_password
        self.connected = False
    def connect(self,username=):

