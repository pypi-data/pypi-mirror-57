#coding:gbk
"""
�Զ������ò���
"""
import hashlib
from PIL import ImageGrab
import logging
#import MySQLdb
import pywintypes
import random
import sys
import os
import threading, time
import win32con, win32file, wmi
import pythoncom
import ctypes

overlapped = None 

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN

BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED  = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

def _print(_str, color=FOREGROUND_WHITE):
    set_color(color)
    sys.stdout.write(_str+'\n')
    sys.stdout.flush()
    set_color(FOREGROUND_WHITE)
    
#��д��
class RWLock():
    def __init__(self):
        self.readers = 0
        self.wLock = threading.Lock()
        self.rLock = threading.Lock()
        
    def writeAcquire(self):
        self.wLock.acquire()
        
    def writeRelease(self):
        self.wLock.release()
        
    def readAcquire(self):
        self.rLock.acquire()
        self.readers += 1
        if self.readers == 1:
            self.wLock.acquire()
        self.rLock.release()
        
    def readRelease(self):
        self.rLock.acquire()
        self.readers -= 1
        if self.readers == 0:
            self.wLock.release()
        self.rLock.release()

#���ݶ���
class Data:
    def __init__(self, data = None):
        self.data = data

    def get(self):
        return self.data

    def set(self, data):
        self.data = data

#��������
class Condition:
    def __init__(self, func, *params, **paramMap):
        self.func = func
        self.params = params
        self.paramMap = paramMap

    def do(self):
        return self.func(*self.params, **self.paramMap)

#���ݿ����Ӷ���
class DBAccessor:
    def __init__(self, host, user, pswd, schm):
        self.host = host
        self.user = user
        self.pswd = pswd
        self.schm = schm
        self.conn = None

    def do(self, sql, *params):
        if self.conn and isExcept(tryExcept(self.conn.stat)):
            self.close()
        if not self.conn:
            conn = tryExcept(MySQLdb.connect, host = self.host, user = self.user, passwd = self.pswd, db = self.schm)
            if isExcept(conn):
                return conn
            self.conn = conn
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, params)
            try:
                if sql.startswith('select'):
                    return cursor.fetchall()
                elif sql.startswith('insert'):
                    return cursor.lastrowid
            finally:
                cursor.close()
                self.conn.commit()
        except Exception, e:
            tryExcept(self.conn.rollback)
            return e

    def close(self):
        if self.conn:
            tryExcept(self.conn.close)
            self.conn = None

#�����߳�
class FuncThread(threading.Thread):
    def __init__(self, func, *params, **paramMap):
        threading.Thread.__init__(self)
        self.func = func
        self.params = params
        self.paramMap = paramMap
        self.rst = None
        self.finished = False
        self.isDaemon = True

    def run(self):
        pythoncom.CoInitialize()
        self.rst = self.func(*self.params, **self.paramMap)
        self.finished = True
        pythoncom.CoUninitialize()

    def getResult(self):
        return self.rst

    def isFinished(self):
        return self.finished

#��־����
class Logger:
    def __init__(self, path):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        self.logger.addHandler(sh)
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        self.logger.addHandler(fh)
        self.case_result = True

    def debug(self, *data):
        data = len(data) == 1 and data[0] or ' '.join(map(str, data))
        self.info(data, logging.DEBUG, FOREGROUND_WHITE|FOREGROUND_INTENSITY)

    def error(self, data, color=FOREGROUND_RED):
        self.info(data, logging.ERROR, color|FOREGROUND_INTENSITY)
        self.case_result = False

    def fatal(self, data, color = FOREGROUND_GREEN):
        self.info(data, logging.FATAL)

    def info(self, data, level = logging.INFO, color = FOREGROUND_GREEN):
        set_color(color|FOREGROUND_INTENSITY)
        try:
            self.logger.log(level, data)
        except:
            pass
        set_color(FOREGROUND_WHITE)

    def warn(self, data, color=FOREGROUND_YELLOW):
        self.info(data, logging.WARN, color|FOREGROUND_INTENSITY)

#��ȡĳ����ָ�����ص�����
#rgb:(r,g,b)
def countPixels(rect, rgb):
    img = grabImage(rect)
    w, h = rect[2] - rect[0], rect[3] - rect[1]
    num = 0
    for i in range(w):
        for j in range(h):
            if img.getpixel((i, j)) == rgb:
                num += 1
    return num

#���߳���ִ��
def doInThread(func, *params, **paramMap):
    ft = FuncThread(func, *params, **paramMap)
    ft.setDaemon(ft.isDaemon)
    ft.start()
    return ft

#��ȡָ������Ľ�ͼ
def grab(rect, path = None):
    img = ImageGrab.grab(rect)
    if path:
        img.save(path)
    return img

#��ȡ��Ļ��ͼ
def grabScreen(path = None):
    return grab(None, path)

#��ȡĳ����Ľ�ͼ
def grabImage(rect, filename = None):
    img = ImageGrab.grab(rect)
    if filename:
        img.save(filename)
    return img

#��ȡָ��λ�õ�����
def getPixel(x, y):
    img = grab((x, y, x + 1, y + 1))
    return img.getpixel((0, 0))

#��ȡ������ָ�����ص�����
#rgb:(r,g,b)
def countPixel(rect, rgb):
    img = grab(rect)
    num = 0
    for i in range(rect[2] - rect[0]):
        for j in range(rect[3] - rect[1]):
            if img.getpixel((i, j)) == rgb:
                num += 1
    return num

#�ж�ָ��λ���Ƿ�������ƥ��
#rgb:(r,g,b)
def matchPixel(x, y, rgb):
    return getPixel(x, y) == rgb

#��һ��������ִ��
def doInTimes(func, times, *params, **paramMap):
    while times > 0:
        rst = func(*params, **paramMap)
        if rst and not isExcept(rst):
            break
        times = times - 1
    return rst

def getTimeFunc():
    import platform
    pf = platform.platform()
    if pf.lower().startswith(r'linux'):
        return time.time
    return time.clock

time_func = getTimeFunc()

#�ڳ�ʱ��Χ��ִ��
#timeoutΪ��ֵ��Ԫ�飨��ʱʱ��,���ʱ�䣩
def handleTimeout(func, timeout, *params, **paramMap):
    global time_func
    interval = 0.6
    if type(timeout) == tuple:
        timeout, interval = timeout
    rst = None
    while timeout > 0:
        t = time_func()
        rst = func(*params, **paramMap)
        if rst and not isExcept(rst):
            break
        time.sleep(interval)
        timeout -= time_func() - t
    return rst

#�ж��Ƿ�Ϊ�쳣
def isExcept(e, eType = Exception):
    return isinstance(e, eType)

#�ж��Ƿ�Ϊ64λϵͳ
def isSystem64():
    return 'PROGRAMFILES(X86)' in os.environ

#����md5
def md5(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()

#�����ļ�md5
def md5File(path, size = 32768):
    m = hashlib.md5()
    f = open(path, 'rb')
    while True:
        d = f.read(size)
        if not d:
            break
        m.update(d)
    f.close()
    return m.hexdigest()

#����sha1
def sha1(data):
    m = hashlib.sha1()
    m.update(data)
    return m.hexdigest()

#�����ļ�sha1
def sha1File(path, size = 32768):
    m = hashlib.sha1()
    f = open(path, 'rb')
    while True:
        d = f.read(size)
        if not d:
            break
        m.update(d)
    f.close()
    return m.hexdigest()

#�����ͼ��md5
def md5Image(rect):
    img = grabImage(rect)
    return md5(img.tostring())

#�����ͼmd5
def md5Grab(rect):
    img = grab(rect)
    return md5(img.tostring())

#ȡ��ִ��
def negative(func, *params, **paramMap):
    return not func(*params, **paramMap)

#��ѯWMI����
def queryWmi(sql):
    rst = wmi.WMI().ExecQuery(sql)
    count = tryExcept(len, rst)
    if isExcept(count):
        return queryWmi(sql)
    return rst, count

#��ȡ������ִ�
def randomIntStr():
    return str(random.random())[2:]

#��ȡʱ���
def timestamp(style = '%Y-%m-%d %H:%M:%S'):
    return time.strftime(style, time.localtime())

#��ȡ�ļ�����ʱ��
def getFileCreateTime(file_path, style='%Y-%m-%d %H:%M:%S'):
    return time.strftime(style, time.localtime(os.stat(file_path).st_ctime))

#��ȡ�ļ�����ʱ��
def getFileModifyTime(file_path, style='%Y-%m-%d %H:%M:%S'):
    return time.strftime(style, time.localtime(os.stat(file_path).st_mtime))

#��try��ִ��
def tryExcept(func, *params, **paramMap):
    try:
        return func(*params, **paramMap)
    except Exception, e:
        return e

#���ļ�
def lockFile(file):
    global overlapped
    if not overlapped:
        overlapped = pywintypes.OVERLAPPED()
    hfile = win32file._get_osfhandle(file.fileno())
    win32file.LockFileEx(hfile, win32con.LOCKFILE_EXCLUSIVE_LOCK, 0, 0xffff, overlapped)

#�����ļ�
def unlockFile(file):
    hfile = win32file._get_osfhandle(file.fileno())
    win32file.UnlockFileEx(hfile, 0, 0xffff, overlapped)
