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
uninstall()

Func uninstall()
   Local $iFile = _PathFull(@ProgramFilesDir & "\360\360Safe\uninst.exe")
   ;MsgBox("","",$iFile)
   Sleep(6000*10)
   ;Local $iPID = RunAs($sUserName, @UserName, $sPassword, $RUN_LOGON_PROFILE, $iFile, "", @SW_SHOWMAXIMIZED)
   ;Local $iPID = Run($iFile, "", @SW_SHOWMAXIMIZED)
   Local $iPID = ShellExecute($iFile)
   ;Local $iPID = _WinAPI_ShellExecute($iFile, '', '', 'open')
   Sleep(1000*6)
   WinWait("360����", "", 10)
   Sleep(3000)
   ControlFocus("360����","","Button1")
   WinWait("[CLASS:#32770]","",10)
   Sleep(3000)
   ControlClick("360����","","Button1")
   Sleep(3000)
   ;MsgBox("","",$iPID)
   ControlFocus("360��Ʒ","","Button2")
   WinWait("[CLASS:#32770]","",10)
   Sleep(3000)
   ControlClick("360��Ʒ","","Button2");���ж��
   Sleep(1000*60*5);�˴���ʱ5����
   ControlFocus("360����","","Button5")
   WinWait("[CLASS:#32770]","",10)
   Sleep(3000)
   ControlClick("360����","","Button5")
   Sleep(3000)
   ControlFocus("360����","","Button4")
   WinWait("[CLASS:#32770]","",10)
   Sleep(3000)
   ControlClick("360����","","Button4")
   Sleep(3000)
   refreshicon()
EndFunc

;ˢ������
Func refreshicon()
   DllCall("shell32.dll", "none", "SHChangeNotify", "long", 134217728, "uint", BitOR(0, 4096), "ptr", 0, "ptr", 0)
   Return 1
EndFunc