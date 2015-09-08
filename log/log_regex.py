#coding:utf-8
import re
import patterns
    
class Log_Regex():
    def __init__(self):
        
        self.patterns = []

    def get_regex_patterns(self):
     
        for elm in patterns.patterns:
            func = elm[0]
            iswrite = elm[1]
            isalert = elm[2]
            xpattern = elm[3]
            self.patterns.append((re.compile(xpattern),func,iswrite,isalert))
    
    def regex_match(self,logpara):
        
        priority = logpara['priority']
        msg = logpara['msg']
        
        resolved = 'False'
        priority = priority
        iswrite = False
        func = None
        
        for x in self.patterns:
            pt = x[0]
            func = x[1]
            iswrite = x[2]
            is_alert = x[3]
            match = pt.match(msg)
            if match:
                if func:
                    func(match,logpara)
                resolved = 'True'
                if is_alert == True:
                    priority = 'alert'
                break
            
        
        logpara['priority'] = priority
        if iswrite and func:
            logpara['priority'] = 'alert'
        logpara['resolved'] = resolved
        logpara['iswrite'] = iswrite
        logpara['func'] = func
    
