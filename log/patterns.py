# -*- coding: utf-8 -*-

from fns import *

patterns = [

#函数的编号应该是顺序的，和行号同为递增的。   
#尽量用已有的模式，去识别更多的消息。否则，一条不确定的消息会遍历所有的正则表达式。
#对于频率比较高的消息，则应放在队列的前列。
#部分万能正则应该放在细化功能正则表达式之后

#出现频率多，且确定不告警服务。

#zmqmsg

(None,False,False,"Get DB message result faile"),
(fn00001zmqmsg,True,False,'unavailable.*updateStorageMountState.*"uuid": "(.*)"'),
(None,False,False,"MessageListener get message"),

#fronvmm#
(fn00001fronvmm,True,False,'CPU feature .* not found\n", "fronvmm-name": "(.*)"'),

(None,False,False,".*stamp.*event.*RESET"),
(None,False,False,".*stamp.*event.*RESUME"),
(None,False,False,".*stamp.*event.*START_VM"),
(None,False,False,".*stamp.*event.*RTC_CHANGE"),
(None,False,False,".*stamp.*event.*POWERDOWN"),
(None,False,False,".*stamp.*event.*SHUTDOWN"),
(fn00002fronvmm,True,False,'.*stamp.*event.*"BLOCK_IO_ERROR", "fronvmm-name": "(.*)", .*data'),
(None,True,False,".*stamp.*event.*STOP"),
(None,False,False,".*stamp.*event.*VNC"),
(None,False,False,".*stamp.*event.*"),

#cluster#
(None,True,False,"clsuter vm.*service exists"),
(None,True,False,"cluster vm.*service not exists"),
(None,True,False,"VM status failed.*Process not exist"),
(None,True,False,"Migrate.*utime.*True"),
(None,True,False,"Migrate.*True.*suc"),
(None,True,False,"HDWP is not quorate and connect other hosts failed"),
(None,True,False,"CLUSTER_INIT.*"),
(None,True,False,"Fence_agent.*"),
(None,True,False,"VM start failed.*vmerr"),

#java#

(None,False,False,"MessageListener get message"),

#vm#

(None,False,False,"VM exe cmd.*system_powerdown.*True"),
(None,False,False,"VM exe cmd.*changeimg.*Get vnc failed"),
(None,False,False,"VM exe cmd.*changeimg.*Connect error"),

(None,False,False,"VM exe cmd.*cpu_set.*offline.*False"),
(None,False,False,"VM exe cmd.*cpu_set.*online.*False"),

(None,True,False,"start kill vmpid (.*)"),                                 #stop vm: start kill vmpid 5275:xAQdBuco-CuJf8W-76hp

(None,False,False,"VM exe cmd.*"),
#以下消息无需告警服务#
(None,False,False,"VM exe cmd.*changeimg.*replace old image*"),
(None,False,False,"VM exe cmd.*Success.*save stage finish"),
(None,False,False,"VM exe cmd.*change drive"),
(None,False,False,"VM exe cmd.*eject -f drive"),
(None,False,False,"VM exe cmd.*balloon"),
(None,False,False,"VM exe cmd.*info migrate.*True"),
(None,False,False,"VM exe cmd.*migrate_set_speed.*True"),
(None,False,False,"VM exe cmd.*info ft.*True"),
(None,False,False,"VM exe cmd.*migrate -d tcp.*True"),
(None,False,False,"VM exe cmd.*info cpus.*True"),
(None,False,False,"VM exe cmd.*cont.*True.*monitor"),
(None,False,False,"VM exe cmd.*quit.*True"),
(None,False,False,"VM exe cmd.*changeimg.*True"),
(None,False,False,"VM exe cmd.*stop.*True"),
(None,False,False,"VM exe cmd.*device_del.*True"),

#host#

(None,False,False,"sync loop thread start"),
(None,False,False,"sync loop pause"),
(None,False,False,"sync loop continue"),
(None,False,False,"LICENSE UUID MSG"),
(None,False,False,"sync loop error"),
(None,False,False,"exceptions.RuntimeError"),
(None,False,False,"thread_erro"),

#shell

(None,False,False,"WILL KILL PID .*"),

#storage#

(None,False,False,"Umount path.*True"),  #此消息事件可以检测出来。
(None,False,False,'Umount path.*False'), #此消息事件可以检测出来。

(None,False,False,"Try mount .* storage.*True"),
(fn00005storage,True,False,"Try mount .* storage:/mnt/(.*) False"), 
(None,False,True,".*storage.*used more than.*space"), #fn00001storage
(fn00006storage,True,False,'Buffer I/O error on device (.*), logical block'),
(fn00007storage,True,False,'iscsid: connect to (.*):3260 failed'),

#code#
(fn00011vm,True,False,"vm_listener except: (.*) Traceback"),   
(fn00012vm,False,False,"vm_listener except.*Connection reset by peer"),
(fn00013vm,False,False,"vm_listener except.*Connection refused"),
(fn00001code,True,False,"SelectAllDBError"),
(fn00003code,False,False,'Event Result Not In Mission.*"action": (.*), "progress"'),
(fn99999code,True,False,".*Traceback.*most recent call last"),

#fronvmm#

(None,False,False,".*stamp.*stage.*"),
#无需告警服务#
(None,False,False,".*stamp.*stage.*info cpus"),
(None,False,False,".*stamp.*stage.*system_powerdown"),
(None,False,False,".*stamp.*stage.*quit"),
(None,False,False,".*stamp.*stage.*eject -f drive"),
(None,False,False,".*stamp.*stage.*change drive"),
(None,False,False,".*stamp.*stage.*migrate -d tcp"),
(None,False,False,".*stamp.*stage.*info migrate"),
(None,False,False,".*stamp.*stage.*migrate_set_speed"),
(None,False,False,".*stamp.*stage.*stop"),
(None,False,False,".*stamp.*stage.*cont"),
(None,False,False,".*stamp.*stage.*changeimg"),
(None,False,False,".*stamp.*stage.*info ft"),
(None,False,False,".*stamp.*stage.*savestage"),


(None,False,False,".*stamp.*desc.*i8254"),
(None,False,False,".*stamp.*desc.*scancode"),
(fn01001fronvmm,True,False,'.*stamp.*desc.*could not open disk image.*"fronvmm-name": "(.*)"'),

(None,True,False,".*stamp.*desc.*cpu cpr.*system is not ready"),
(None,True,False,".*stamp.*desc.*driver option fail"),
(None,True,False,".*stamp.*desc.*len.*errno"),
(None,True,False,".*stamp.*desc.*Success.*restore finished"),
(None,True,False,".*stamp.*desc.*"),

(None,False,False,".*stamp.*VNC"),
(None,False,False,"zcp.*copy the file.*success"),


#network#
(None,False,False,".*ovs-vsctl add-port"),
(None,False,False,".*ovs-vsctl.*if-exists del-port"),
(None,False,False,".*ovs-vsctl.*comment ovs-brcompatd"),
(None,False,False,".*ovs-vsctl.*create QoS"),
(None,False,False,".*ovs-vsctl.*may-exist add-br"),
(None,False,False,".*ovs-vsctl.*"),

#java#
(fn00001java,True,False,"finished initialize Threads"),
(None,False,False,"send job message to vmd"), #
(None,False,False,"pool-.*-thread-.*"),

]
