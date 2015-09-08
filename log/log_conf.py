# -*- coding: utf-8 -*-

import os
import time


import system.monit.stable_time
import support.uuid_op
from support.fileutil.file_option import FileOption

LOG_CONF_PATH = '/etc/apache-tomcat-6.0.37/webapps/ROOT/WEB-INF/classes/logConf.properties'
level_tag = {}
level_value = {"debug":10,"info":20,"notice":30,"warning":40,"err":50,"crit":60,"alert":70,"emerg":80,"none":90}

HOSTUUID = ""
 
def rsyslog_restart():

    os.system('/etc/init.d/rsyslog restart')

   
def recovery_from_lstr(lstr):

    param = {}
    lx = lstr.strip().split()
    for item in lx:
        key = item.split(":")[0].strip()
        value = item.split(":")[1].strip()
        param[key] = value 
   
    return param 

def reset_level_tag(msg):
   
    param =  recovery_from_lstr(msg)
    if param.pop("host") != "localhost": 
        return 
   
    for key,value in param.items():
        level_tag[key] = value
    
def unknown_msg(log_para):
    
    if not level_tag.get(log_para.get('syslogtag')) or not level_value.get(log_para.get('priority')):
        log_para['isunknown'] = True
        return True
    return False
     
def check_priority(log_para):

    syslogtag = log_para.get('syslogtag')
    priority = log_para.get('priority')
    
    lv = level_tag[syslogtag]
    if level_value[priority] < level_value[lv]:
        return False
    
    return True
    
def get_log_conf():
    
    fn = LOG_CONF_PATH
    f = open(fn) 
    lines = f.readlines()
    f.close()
    
    for x in lines:
        lx = x[:-1].split('=')
        syslogtag = lx[0].strip()
        current_level = lx[1].strip().split(',')[0].strip()
        level_tag[syslogtag] = current_level
    
            
def reset_syslogtag(tag):

    for x in level_tag.keys():
        if tag.find(x) != -1:
            tag = x
            break

    if tag.find('[') != -1:
        tag = tag.split('[')[0].strip()

    return tag

def get_basehostname():

    file_name = '/etc/sysconfig/network'
    lines = FileOption(file_name).read_file()
    if not lines:
        return ""
    basehostname = ""
    for item in lines:
        if 'HOSTNAME=' == item[0:9]:
            basehostname = item.split("\n")[0].split("HOSTNAME=")[1]
    return basehostname
            
            
def base_resolve(lstr):
    lx = lstr.split()
    ltime = lx[0]
    priority = lx[1]
    facility = lx[2]
    host = lx[3]
    syslogtag = lx[4][:-1]
    absolutetime = system.monit.stable_time.do_web_get_stable_time()
 
    msg = " ".join(lx[5:])
    if facility == 'local1' and host == 'Java':

        vsuuid = support.uuid_op.get_vs_uuid()[1]
        basehostname = get_basehostname()
        if basehostname != "":
            host = basehostname
        else:
            host = vsuuid

        syslogtag = 'java'
        if lx[4] == 'DEBUG':
            priority = 'debug'
        if lx[4] == 'INFO':
            priority = 'info'
        if lx[4] == 'WARN':
            priority = 'warn'
        if lx[4] == 'ERROR':
            priority = 'err'
        msg = " ".join(lx[5:])

    ts = time.strptime(ltime[:-6], '%Y-%m-%dT%H:%M:%S.%f')
    ntime = time.mktime(ts) 
    
    return ntime,priority,facility,host,syslogtag,absolutetime,msg

def init_logpara(log_para,lstr):
    
    time,priority,facility,host,syslogtag,absolutetime,msg= base_resolve(lstr)
    
    syslogtag = reset_syslogtag(syslogtag)
    
    if syslogtag == "setlogleveltag":
        reset_level_tag(msg)
                
    log_para['time'] = time
    log_para['facility'] = facility
    log_para['host'] = host
    log_para['syslogtag'] = syslogtag
    log_para['msg'] = msg
    log_para['hostuuid'] = HOSTUUID
    log_para['absolute_time'] = absolutetime
    log_para['priority']= priority
    log_para['isunknown'] = False
    log_para['resolved'] = 'False'
    
    log_para['iswrite'] = False

    log_para['optobjuuid'] = ''
    log_para['optobjtype'] = ''
    log_para['reqtype'] = ''
    log_para['message'] = ''
    log_para['level'] = 'debug'
    
def init():
    
    rsyslog_restart()
    get_log_conf()


