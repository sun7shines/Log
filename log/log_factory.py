#coding:utf-8

log_msgs = {'log_package':[]}
from unknown_log import UNknown_Log
from err_log import Err_Log
from alert_log import Alert_Log
loglist = {}

class LogFactory():
        
    @staticmethod
    def create_log(logpara):
        '''
        分类策略：
        设备 iscsid python Java kernel FronVMM
        优先级 err warning  notice info
        err 立即发送
        kernel and iscsid err 发警报
        其他低级的级别 如info 满十个发送
        致命级(KERN_EMESG), 
        警戒级(KERN_ALERT), 
        临界级(KERN_CRIT),
        错误级(KERN_ERR),
        '''

        priority = logpara["priority"]##优先级
        isunknown = logpara["isunknown"]
        syslogtag = logpara["syslogtag"]
        
            ##未知的日志（优先级、tag 未知） 目前之是单纯的作为基本的日志日志类型进行操作。
            ##后期需要处理的话就重写UNknown_Log 类
        if isunknown:
            if not loglist.get("unknown_log"):
                loglist["unknown_log"] = UNknown_Log("unknown")
                return loglist["unknown_log"]
            else:
                return loglist["unknown_log"] 
        elif syslogtag in ("iscsid","kernel","FronVMM","python") and priority == "err":
            
            if not loglist.get("alert_log"):
                loglist["alert_log"] = Alert_Log("alert_log")
                return loglist["alert_log"]
            else:
                return loglist["alert_log"]
        elif priority in ("alert","crit","alert"):
            '''
            严重的日志级别进行告警 ？是否需要
            '''
            if not loglist.get("alert_log"):
                loglist["alert_log"] = Alert_Log("alert_log")
                return loglist["alert_log"]
            else:
                return loglist["alert_log"]
        
        elif priority == "err":
            
            if not loglist.get("err_log"):
                loglist["err_log"] = Err_Log("err_log")
                return loglist["err_log"]
            else:
                return loglist["err_log"]               
        else:
            if not loglist.get("norm_log"):
                loglist["norm_log"] = UNknown_Log("norm")
                return loglist["norm_log"]
            else:
                return loglist["norm_log"]


