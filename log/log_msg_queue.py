# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/usr/vmd")

import syslog
import Queue
import traceback
import support.uuid_op
from socketqueue import SocketServer
import log_conf
from log_regex import Log_Regex
from log_factory import LogFactory

def write_noutf8_msg():
    
    syslog.syslog(syslog.LOG_ERR,str(traceback.format_exc()))

def checkutf8(line):

    try:
        line.encode('utf-8')
        return True
    except:
        write_noutf8_msg()
        return False
    
class Msg_Queue():
    
    def __init__(self,serverhost,serverport,hostuuid):
        self.logmsg_queue = Queue.Queue() 
        self.logserver = SocketServer(serverhost,serverport)
        self.hostuuid = hostuuid
        log_conf.HOSTUUID = hostuuid
        self.log_regex = Log_Regex()
        
    def append_logmsg_object(self,logmsg_object):
    
        try:
            self.logmsg_queue.put(logmsg_object)
        except:
            syslog.syslog(syslog.LOG_ERR,"append_losgmsg_object error: "+str(traceback.format_exc()))
        return
    
    def get_logmsg(self):
    
        while True:
            flag,logmsg = self.logserver.get()
            if flag:
                self.append_logmsg_object(logmsg)
    
    def dispatch_logmsg(self):
        
        self.log_regex.get_regex_patterns()
        
        while True:
            logmsg = self.logmsg_queue.get()
            log_para = {}
            
            try:   
                if not checkutf8(logmsg):
                    #对于非utf8编码实行严格过滤
                    continue
                    
                log_conf.init_logpara(log_para,logmsg)
                
                if  log_conf.unknown_msg(log_para):
                    log = LogFactory.create_log(log_para)
                    log.dealwithlog(log_para)
                    continue 
                
                if not log_conf.check_priority(log_para):
                    continue
                self.log_regex.regex_match(log_para)
                log = LogFactory.create_log(log_para)
                log.dealwithlog(log_para)
                    
            except:
                syslog.syslog(syslog.LOG_ERR,"log dispatch err:"+str(traceback.format_exc()))
                continue
        
                
                
                