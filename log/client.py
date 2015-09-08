# -*- coding: utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/usr/vmd")
import datetime

import socket_util

serverhost = 'localhost'
serverport = 9170

num = -1

def set_log_pri(syslogtag):

    if syslogtag in ['python']:
        return 'err'

    if syslogtag in ['ccs_tool','fenced','gfs2_cnotrold','rgmanager']:
        return 'alert'

    if syslogtag in ['auditd','rpc.statd','rsyslogd','init','rpcbind','logrotate','sm-notify','yum']:
        return 'debug'

    return 'info'

def base_resolve(lstr,line):

    lx = lstr.split()
    time = lx[0]
    host = lx[1]
    syslogtag = lx[2][:-1]
    msg = " ".join(lx[3:])
    print str(len(msg)),msg
    facility = 'user'
    priority = set_log_pri(syslogtag)
    return time,facility,host,syslogtag,msg,priority

def get_log_conf():

    LOG_CONF_PATH = '/etc/apache-tomcat-6.0.37/webapps/ROOT/WEB-INF/classes/logConf.properties'
    fn = LOG_CONF_PATH
    f = open(fn)
    lines = f.readlines()
    level_tag = {}
    for x in lines:
        lx = x[:-1].split('=')
        syslogtag = lx[0].strip()
        current_level = lx[1].strip().split(',')[0].strip()
        current_level = 'debug'
        level_tag[syslogtag] = current_level
    f.close()

    return level_tag

def create_level_tag_str():

    TIME = datetime.datetime.now().isoformat('T')
    priority = "alert"
    facility = "user"
    host = "h54"
    syslogtag = "setlogleveltag:"

    param = {"host":"localhost"}
    level_tag = get_log_conf() 
    param.update(level_tag)
    msg = ""
    for key,value in param.items():
        msg = msg + key+":"+value+" "

    lstr = TIME+" "+priority+" "+facility+" "+host+" "+syslogtag+" "+msg
    print syslogtag,lstr
    return lstr

def send_message_lines(fn,num):

    f = open(fn)
    lines = f.readlines()
    f.close()

    import socket
    import time
    time.sleep(2)
    for line in lines:
        if not line.strip():
            continue
        time.sleep(0.5)
        lx = line[:-1]
        TIME,facility,host,syslogtag,msg,priority = base_resolve(lx,line)
        lstr = TIME+" "+priority+" "+facility+" "+host+" "+syslogtag+": "+msg+"\n"

        if True: 
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_util.close_socket_inheritance(sock)
            sock.connect((serverhost, serverport))
            sock.setblocking(1)
            print lstr
            sock.send(lstr)
            sock.close()
            num = num +1 
            print num

def send_level_tag_line():

    import socket
    import time
    time.sleep(2)
        
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_util.close_socket_inheritance(sock)
    sock.connect((serverhost, serverport))
    sock.setblocking(1)
    
    lstr = create_level_tag_str()
    
    sock.send(lstr)
    sock.close()

if __name__ == "__main__":

    num = 0
    #if len(sys.argv) != 3:
    #    print "argv number error!"
    #    sys.exit()  
    if sys.argv[1] == '-f':
        while True:
            send_message_lines(sys.argv[2],num)
    if sys.argv[1] == 'level':
        send_level_tag_line()
