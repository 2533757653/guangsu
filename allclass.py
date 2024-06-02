
class resource:
    def __init__(self) -> None:
        pass
    def initize(self,id,name,number,startdate,enddate,starttime,endtime,priority,time):
        self.id=id
        self.name=name
        self.number=number
        self.startdate=startdate
        self.enddate=enddate
        self.starttime=starttime
        self.endtime=endtime
        self.priority=priority
        self.time=time
    def initfromlist(self,data):
        self.id=data[0]
        self.name=data[1]
        self.number=data[2]
        self.startdate=data[3]
        self.enddate=data[4]
        self.starttime=data[5]
        self.endtime=data[6]
        self.priority=data[7]
        self.time=data[8]
    
    def output(self):
        print("资源名称是"+self.name)
        print("资源数量是"+self.number)
# 这里对应所有的资源,不过需要考虑一个问题，那就是异步处理属于是
# 每个资源在使用结束后都需要释放，如何做呢？
# 现实世界总要解决异步问题 
# 遗传，蚁群去解决异步算法

class gongyi:
    def __init__(self,name,pretime,worktime,aftertime) -> None:
        self.name=name
        #only pretime and worktime use resources
        self.pretime=pretime
        self.worktime=worktime
        self.aftertime=aftertime
        pass
    
    
class wuliao:
    def __init__(self,id,gongxu) -> None:
        self.id=id
        self.gongxu=gongxu
        
        
class need:
    def __init__(self) -> None:
        pass