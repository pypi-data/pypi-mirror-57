#include <AutoItConstants.au3>
#include <MsgBoxConstants.au3>
#include <File.au3>
#include <WinAPIFiles.au3>
#include <WinAPISys.au3>

Local const $winxp = 'WIN_XP'
Local const $win7 = 'WIN_7'
Local const $win8 = 'WIN_8'
Local const $win81 = 'WIN_81'
Local const $win10 = 'WIN_10'
Local const $wuhq = '3PFTVS4-WUHQ'

Global Const $r = 4 ;设置蓝牙循环传送文件几次，建议设置4
Opt("WinTitleMatchMode", 4)
$sTrayWindow = WinGetHandle("[CLASS:Shell_TrayWnd]")
WinSetState($sTrayWindow, "", @SW_SHOW)
$ToolbarWindow = ControlGetHandle($sTrayWindow,"","ToolbarWindow323")
WinSetState($sTrayWindow,"",@SW_SHOW)
$sTrayNotify = ControlGetHandle($sTrayWindow,"","TrayNotifyWnd1")
WinSetState($sTrayNotify,"",@SW_SHOW)
$Button = ControlGetHandle($sTrayWindow,"","Button1")

;Local $i = 0
;While $i <= $r
;   BlueTooth(1,$i)
;   $i = $i + 1
;WEnd
;$i = 0
;While $i <= $r
;   BlueTooth(2,$i)
;   $i = $i + 1
;WEnd

Switch @OSVersion
   Case $winxp

   Case $win7

   Case $win8

   Case $win81

   Case $win10
	  If @ComputerName == $wuhq Then
		 BlueTooth(1,0)
		 refuse()
		 BlueTooth(2,0)
		 refuse()
		 BlueTooth(1,1)
		 refuse()
		 BlueTooth(2,1)
		 refuse()
		 BlueTooth(1,2)
		 refuse()
		 BlueTooth(2,2)
		 refuse()
	  Else
		 Exit
	  EndIf
EndSwitch

Func BlueTooth($t,$p)
   ;--------------------------------------------------------
   ;运行蓝牙程序
   ProcessClose("fsquirt.exe")
   Local $sUserName = "wuhq"
   Local $sPassword = "1221"
   Sleep(3000)
   RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "fsquirt.exe", "", @SW_SHOWMAXIMIZED)
   Sleep(3000)
   ControlFocus("蓝牙文件传送","","Button4")
   ControlClick("蓝牙文件传送","","Button4")

   ;根据坐标运行蓝牙
   ;ControlClick($sTrayWindow,"","ToolbarWindow323","main")
   ;Sleep(1000)
   ;MouseClick($MOUSE_CLICK_MAIN,"1258","648")
   ;----------------------------------------------------------
   Opt("MouseCoordMode",0)
   Local $aPos = WinGetPos("[ACTIVE]")
   Sleep(3000)
   ;左边一列
   Local $m = $t*200
   Local $n = $p*57
   MouseClick($MOUSE_CLICK_MAIN,$aPos[0]+$m,$aPos[1]+160+$n,"2")
   ;右边一列
   ;MouseClick($MOUSE_CLICK_MAIN,$aPos[0]+400,$aPos[1]+160+$p*0,"2")

   Sleep(1000)
   ControlFocus("蓝牙文件传送","","Edit1")
   ControlClick("蓝牙文件传送","","Button7")   ;点击浏览,运行蓝牙程序是修改成Button7
   ControlFocus("浏览","","Edit1")
   WinWait("[CLASS:#32770]","",10)
   Sleep(2000)
   ControlSetText("浏览","", "Edit1", @DesktopDir & "\SN.txt")
   ;ControlSetText("浏览","", "Edit1", "C:\Users\Wuhq\Desktop\SN.txt")
   Sleep(2000)
   ControlClick("浏览","","Button1")

   Sleep(1000)
   ControlFocus("蓝牙文件传送","","Button1")
   ControlClick("蓝牙文件传送","","Button1")
   Sleep(1000*10)
   ControlClick("蓝牙文件传送","","Button3")
EndFunc

Func refuse()
   ControlFocus("公告弹窗","","")
   WinWait("[CLASS:popupWindowClass]","",10)
   Sleep(3000)
   WinClose("[CLASS:popupWindowClass]", "");Close the currently active window
EndFunc