# -*- coding: utf-8 -*-
"""
# Filename: vmd_log_op.py
# Note: This module support these option, 
# create a socket server to get msg from rsyslog,
# using factory design mode to create special log classess
# make email alert
#
# Author: zhangwenhui
# Create time: 2014-07-08
"""
import sys
import traceback
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/usr/vmd")
import syslog
import time

import global_params
global_params.django = True
sys.path.append("/usr/")
from django.conf import settings
sys.path.append("/usr/django_object")
try:
    import django_object.settings
    settings.configure(default_settings=django_object.settings)
except:
    pass

import new_subthread
import create_daemon
import support.uuid_op
import log_conf
from log_msg_queue import Msg_Queue
import support.message.vmd_message_queue
import support.message.global_object
import dbmodule.db_module_interface

def __init_log_server():
    """Init mission event server, recv optevent result."""
    
    try:
        support.message.global_object.MSG_LOG_OBJECT = support.message.vmd_message_queue.LOGQueue()
    except:
        strs = str(traceback.format_exc())
        syslog.syslog(syslog.LOG_ERR, "Start log server for vmdlog failed: " + strs)
        return False
    return True

def get_log_db_message():
    """Get log db  result message."""
    
    try:
        (flag, log_db_message) = \
         support.message.global_object.MSG_LOG_OBJECT.server.get()
    except support.message.message_queue.QueueGetError:
        return (False, "")
    try:
        support.message.global_object.MSG_LOG_OBJECT.server.put \
               ("recv successed")
    except support.message.message_queue.QueuePutError:
        return (False, "")
    return (flag, log_db_message)


def log_server():
    """log server to get log db result."""
    
    while True:
        
        # e.g block here
        (flag, log_db_message) = get_log_db_message()
        if not flag:
            continue
        flag = dbmodule.db_module_interface.put_re_message_in_queue(log_db_message)

def running_log_server():
    """Running log server,
    Get log db  result message."""
    
    # e.g runing sub thread for dispatch
    desc = "start_log_server"
    new_subthread.addtosubthread(desc, log_server)
    return

if __name__ == '__main__':
    
    no_fork = False
    global_params.DB_PORT = support.message.global_object.MSG_LOG_SERVER_PORT
    if len(sys.argv) > 1:
        if sys.argv[1] == "-d":
            no_fork = True
    if not no_fork:
        create_daemon.daemonize()

    if global_params.vcflag:
        sys.exit(0)

    # sleep 8 seconds wait until /etc/init_business.py running finished
    time.sleep(8)
    log_conf.init()
    global_params.init_threadlock()
    
    _,hostuuid = support.uuid_op.get_vs_uuid()
    serverport = 9170
    serverhost = 'localhost'
    log_queue = Msg_Queue(serverhost,serverport,hostuuid)
    if not __init_log_server():
        sys.exit(1)
    running_log_server()

    new_subthread.addtosubthread("logloop_get_logmsg", \
                                 log_queue.get_logmsg)
    new_subthread.addtosubthread("logloop_dispatch_logmsg",\
                                 log_queue.dispatch_logmsg)
    
    while True:
        time.sleep(5)
    
