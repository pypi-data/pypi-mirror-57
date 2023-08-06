#coding:gbk
"""
�������Զ�������
"""
import time
import win32api, win32con

CLICK_MOUSE = 0
CLICK_MOUSE_DOUBLE = 1
CLICK_MOUSE_RIGHT = 2
MOVE_MOUSE = 3
CLICK_MOUSE_MIDDLE = 4

#������
def clickMouse(x, y, byDrv = False, mode = CLICK_MOUSE,move_wait_time=0):
    moveMouse(x, y, byDrv)
    if move_wait_time:
        time.sleep(move_wait_time)
    if mode == MOVE_MOUSE:
        return
    downMsg, upMsg = win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP
    if mode == CLICK_MOUSE_RIGHT:
        downMsg, upMsg = win32con.MOUSEEVENTF_RIGHTDOWN, win32con.MOUSEEVENTF_RIGHTUP
    elif mode == CLICK_MOUSE_MIDDLE:
        downMsg, upMsg = win32con.MOUSEEVENTF_MIDDLEDOWN, win32con.MOUSEEVENTF_MIDDLEUP
    win32api.mouse_event(downMsg, 0, 0, 0, 0)
    win32api.mouse_event(upMsg, 0, 0, 0, 0)
    if mode == CLICK_MOUSE_DOUBLE:
        win32api.mouse_event(downMsg, 0, 0, 0, 0)
        win32api.mouse_event(upMsg, 0, 0, 0, 0)

#�����꣨���˫����
def clickMouseDouble(x, y, byDrv = False):
    clickMouse(x, y, byDrv, CLICK_MOUSE_DOUBLE)

#�����꣨�Ҽ���
def clickMouseRight(x, y, byDrv = False):
    clickMouse(x, y, byDrv, CLICK_MOUSE_RIGHT)

#�ƶ����
def moveMouse(x, y, byDrv = False):
    w, h = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
    x, y = int(float(x) / w * 65535), int(float(y) / h * 65535)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)

#��껬�ֹ���
def wheelMouse(dwData = 0):
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, dwData, win32con.WHEEL_DELTA)
    
#��ȡ��ǰ����
def getCursorPos():
    return win32api.GetCursorPos()


