import psutil
import time
import os,datetime

def main():
        dt =  datetime.datetime.fromtimestamp(psutil.boot_time())
        print "���ԵĿ���ʱ��:%s" %dt.strftime("%Y-%m-%d,%H:%M:%S")
        timenow = timeget()
        print '����������ʱ��:%s' %timenow
        timecha = time.time() - psutil.boot_time()
        print '����ʱ��%s' %timecha
        time.sleep(3600)


def timeget():
        timeStamp = time.time()
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)    
        return otherStyleTime           
        

if __name__=="__main__":
        main()
