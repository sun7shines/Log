# -*- coding: utf-8 -*-

import syslog
import traceback

import support.message.message as message
import support.message.vmd_message_queue as vmd_message_queue
import system.monit.stable_time
from log_base import Base_Log
import log_factory
import send_mail
class Err_Log(Base_Log):
    '''
    errlog is desing for a log level is err
    but does not trigger the alarm
    '''
    
    def __init__(self,log_type):
        
        self.logtype=log_type
    
    def dealwithlog(self,logpara):
        return self.regexp_resolve(logpara)
        

    def regexp_resolve(self,logpara):
        
        log_msg = {}
        log_msg['time'] = logpara['time']
        log_msg['facility'] = logpara["facility"]
        log_msg['host'] = logpara["host"]
        log_msg['syslogtag'] = logpara["syslogtag"]
        log_msg['msg'] = logpara["msg"]
        log_msg['priority'] = logpara["priority"]
        log_msg['hostuuid'] = logpara["hostuuid"]
        log_msg['absolute_time'] = str(int(logpara["absolute_time"]))
        log_msg['resolved'] = logpara['resolved']
        log_factory.log_msgs['log_package'].append(log_msg)
        mdict = {'message':'log','log_package':[]}
        mdict['log_package'].append(log_msg)
        msg = message.LogMessage(mdict)
        vmd_message_queue.put_msg_to_vsvc_web(msg, True)
        
        if (logpara['iswrite'] and logpara['func']):      
            self.trigger(logpara)
        
