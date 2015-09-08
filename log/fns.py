# -*- coding: utf-8 -*-


#要求返回optobjuuid,optobjtype,reqtype,message#

def fn00001vm(m,logpara):
    
    return None

def fn00002vm(m,logpara):
    
    return None

def fn00006vm(m,logpara):
    
    return None

def fn00007vm(m,logpara):
    
    return None

def fn00008vm(m,logpara):
    
    return None

def fn00009vm(m,logpara):
    
    return None

def fn00010vm(m,logpara):
    
    return None

def fn00011vm(m,logpara):
    
    ##vm_listener except: xAQdBuco-CuJf8W-76hp Traceback
    
    if len(m.groups()) <1:
        return
    uuid = m.group(1)
    logpara['optobjuuid'] = uuid
    logpara['optobjtype'] = 'vm'
    logpara['reqtype'] = 'running'
    logpara['message'] = 'False'
    logpara['optflag'] = 'alert'
    
    return None

def fn00012vm(m,logpara):
    
    return None

def fn00013vm(m,logpara):
    
    return None

def fn00002host(m,logpara):
    
    return None

def fn00003host(m,logpara):
    
    return None

def fn00001storage(m,logpara):
    #判断存储容量是否超过80%
    logpara['optobjuuid'] = ''
    logpara['optobjtype'] = 'storage'
    logpara['reqtype'] = ''
    logpara['message'] = 'True'
    logpara['optflag'] = 'alert'
    
    return None

def fn00002storage(m,logpara):
    return None

def fn00004storage(m,logpara):
    return None  

def fn00005storage(m,logpara):
    #Try mount single storage:/mnt/1cdc354fbfc09de7916e6fde315e7864 False
    #判断存储容量是否超过80%
    if len(m.groups()) <1:
        return
    storage_uuid = m.group(1)
    logpara['optobjuuid'] = storage_uuid
    logpara['optobjtype'] = 'storage'
    logpara['reqtype'] = 'capacity'
    logpara['message'] = 'False'
    logpara['optflag'] = 'alert'

def fn00001code(m,logpara):
    
    #gluster updated: Traceback (most recent call last):#012  File "vmd/operation/gluster/peer_db.py", line 509, in gluster_updated#012  File
    logpara['optobjuuid'] = 'python'
    logpara['optobjtype'] = 'program'
    logpara['reqtype'] = 'exception'
    logpara['message'] = 'True'
    logpara['optflag'] = 'alert'
    
def fn99999code(m,logpara):
    #SelectAllDBError:(<class 'django.db.utils.OperationalError'>, OperationalError((2003, "Can't connect to MySQL server on '127.0.0.1' (111)"),), <traceback object at 0x7fbb404f99e0>)
    
    logpara['optobjuuid'] = 'mysql'
    logpara['optobjtype'] = 'program'
    logpara['reqtype'] = 'exception'
    logpara['message'] = 'True'
    logpara['optflag'] = 'alert'
    
def fn00001java(m,logpara):
    # main - finished initialize Threads...
    logpara['optobjuuid'] = 'java'
    logpara['optobjtype'] = 'program'
    logpara['reqtype'] = 'restart'
    logpara['message'] = 'True'
    logpara['optflag'] = 'alert'
    
def fn00001fronvmm(m,logpara):
    #{"timestamp": {"seconds": 1407827583, "microseconds": 795610}, "desc": "CPU feature epb not found\n", "fronvmm-name": "xp-1"}
    if len(m.groups()) <1:
        return
    vmDesc = m.group(1)
    logpara['optobjuuid'] = vmDesc
    logpara['optobjtype'] = 'fronvmm'
    logpara['reqtype'] = 'cpuFeature'
    logpara['message'] = 'False'
    logpara['optflag'] = 'alert'
    
def fn00001zmqmsg(m,logpara):
    ##MessageListener get message :{"state": "unavailable", "message": "updateStorageMountState", "uuid": "cc1156427b3afe8f5e0f2e4086646c06"
    if len(m.groups()) <1:
        return
    uuid = m.group(1)
    logpara['optobjuuid'] = uuid
    logpara['optobjtype'] = 'storage'
    logpara['reqtype'] = 'available'
    logpara['message'] = 'False'
    logpara['optflag'] = 'alert'
    
def fn00003code(m,logpara):

    if len(m.groups()) <1:
        return
    action = m.group(1)
    logpara['optobjuuid'] = str(action)
    logpara['optobjtype'] = 'taskEvent'
    logpara['reqtype'] = 'send'
    logpara['message'] = 'False'
    logpara['optflag'] = 'alert'
    
def fn00006storage(m,logpara):

    if len(m.groups()) <1:
        return
    device = m.group(1)
    logpara['optobjuuid'] = device
    logpara['optobjtype'] = 'storage'
    logpara['reqtype'] = 'available'
    logpara['message'] = 'False'
    logpara['optflag'] = 'alert'
    
def fn00007storage(m,logpara):

    if len(m.groups()) <1:
        return
    iscsi_host = m.group(1)
    logpara['optobjuuid'] = iscsi_host
    logpara['optobjtype'] = 'storage'
    logpara['reqtype'] = 'connected'
    logpara['message'] = 'False'
    logpara['optflag'] = 'alert'
    
def fn01001fronvmm(m,logpara):
    
    if len(m.groups()) <1:
        return
    vmDesc = m.group(1)
    logpara['optobjuuid'] = vmDesc
    logpara['optobjtype'] = 'fronvmm'
    logpara['reqtype'] = 'imgState'
    logpara['message'] = 'False'
    logpara['optflag'] = 'alert'
    
def fn00002fronvmm(m,logpara):
    #{"timestamp": {"seconds": 1364878600, "microseconds": 345895}, "event": "BLOCK_IO_ERROR", "fronvmm-name": "xp1", "data": {"device": "a6a18f54206fb11a20037", "operation": "write", "action": "report"}}
    if len(m.groups()) <1:
        return
    vmDesc = m.group(1)
    logpara['optobjuuid'] = vmDesc
    logpara['optobjtype'] = 'fronvmm'
    logpara['reqtype'] = 'imgState'
    logpara['message'] = 'False'
    logpara['optflag'] = 'alert'
    
    