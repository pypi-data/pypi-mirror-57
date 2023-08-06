#include <FileConstants.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIFiles.au3>
#include <File.au3>
#include <WinAPIFiles.au3>
#include <WinAPIHObj.au3>
#include <Process.au3>
#include <WinAPIShellEx.au3>


;Local $sUserName = "administrator"
;Local $sPassword = "www.360.cn"
install()
Sleep(1000*10)
Shutdown(6)

Func install()
   ;Local $iFile = _PathFull(@WorkingDir & "\..\file\install\skylarinst-winc(10.95.27.118_80).exe")
   ;MsgBox("","",$iFile)
   ;Local $iPID = RunAs($sUserName, @UserName, $sPassword, $RUN_LOGON_PROFILE, $iFile, "", @SW_SHOWMAXIMIZED)
   ;Local $iPID = Run($iFile, "", @SW_SHOWMAXIMIZED)
   ;Local $iPID = ShellExecute($iFile)
   ;Local $iPID = _WinAPI_ShellExecute($iFile, '', '', 'open')
   Sleep(1000*6)
   WinWait("360天擎安装程序", "", 10)
   Sleep(3000)
   ControlFocus("360天擎安装程序","","Button2")
   WinWait("[CLASS:#32770]","",10)
   Sleep(3000)
   ControlClick("360天擎安装程序","","Button2")
   Sleep(1000*60*5);此处延时5分钟
   ControlFocus("360天擎安装程序","","Button10")
   WinWait("[CLASS:#32770]","",10)
   Sleep(3000)
   ControlClick("360天擎安装程序","","Button10")
   Sleep(3000)
   refreshicon()
EndFunc

;刷新桌面
Func refreshicon()
   DllCall("shell32.dll", "none", "SHChangeNotify", "long", 134217728, "uint", BitOR(0, 4096), "ptr", 0, "ptr", 0)
   Return 1
EndFunc