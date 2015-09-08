# -*- coding: utf-8 -*-

import syslog
import traceback

import support.message.message as message
import support.message.vmd_message_queue as vmd_message_queue
import system.monit.stable_time
from log_base import Base_Log
import log_factory
import send_mail

class Alert_Log(Base_Log):
    
    def __init__(self,log_type):
        
        self.logtype=log_type
    
    def dealwithlog(self,logpara):
           
        self.regexp_resolve(logpara)
            
    def regexp_resolve(self,logpara):
        ##发送消息
        
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
        
        #不计算在log_msg中
        
        mdict = {'message':'log','log_package':[]}
        mdict['log_package'].append(log_msg)
        msg = message.LogMessage(mdict)
        vmd_message_queue.put_msg_to_vsvc_web(msg, True) 
        
        if (logpara['iswrite'] and logpara['func']):      
            maillevel = "CRITICAL"
            title = "CRITICAL LOG for :%s %s"%(log_msg['host'],log_msg['syslogtag'])
            #send_mail.send_alert_mail(maillevel, title,str(mdict))#
            self.trigger(logpara)
