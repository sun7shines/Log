# -*- coding: utf-8 -*-

import time
import support.message.message as message
import support.message.vmd_message_queue as vmd_message_queue
import system.monit.stable_time
import support.message.global_object

import log_factory

import eventlog_db_op
import socket
import datetime
import global_params

import syslog


class Base_Log():
    '''
    base log is the superclass of all the logs 
    '''
    
    def __init__(self,log_type):
        
        self.logtype=log_type
        
    def dealwithlog(self,logpara):
        
        self.regexp_resolve(logpara)
    
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
        if len(log_factory.log_msgs['log_package']) >= 10:
            mdict = log_factory.log_msgs
            msg = message.LogMessage(mdict)
            vmd_message_queue.put_msg_to_vsvc_web(msg, True)
            log_factory.log_msgs['log_package'] = []
        

    def trigger(self,logpara):
        
        if not (logpara.get('optobjuuid') and logpara.get('optobjtype') and logpara.get('reqtype') and logpara.get('message')):
            return
        if logpara.get('optflag') in ['error','ERROR']:
            logpara['optflag'] = 'err'
            
        if logpara.get('optflag') in ['warn']:
            logpara['optflag'] = 'warning'
             
        eventlogparam = {"optobjuuid":logpara.get('optobjuuid'),
                         "optobjtype":logpara.get('optobjtype'),
                         "message": logpara.get('message'),
                         "reqtype":logpara.get('reqtype'),
                         "optflag":logpara.get('optflag'),
                         "debug_message": "log",
                         "mission_id":0,
                         "action":0,
                         "username":"system",
                         "eventtime":datetime.datetime.now(),
                         "option_obj":'log',
                         "opthost":socket.gethostname()}
        global_params.DB_PORT = support.message.global_object.MSG_LOG_SERVER_PORT
        flag, state = eventlog_db_op.insert_eventlog(eventlogparam)
        