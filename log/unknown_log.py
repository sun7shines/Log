#coding:utf-8

from log_base import Base_Log

class UNknown_Log(Base_Log):
    '''
    if a log is not in the list of current conditions
    make it  As unknown
    '''
    
    def __init__(self,log_type):
        
        self.logtype=log_type
    
    def dealwithlog(self,logpara):
        
        self.regexp_resolve(logpara)
        if (logpara['iswrite'] and logpara['func']):      
            self.trigger(logpara)