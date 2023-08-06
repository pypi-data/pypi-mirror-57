#include <File.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIFiles.au3>
#include <WinAPISys.au3>


ControlFocus("数据安全","","Button8")
WinWait("[CLASS:#32770]","",10)
Sleep(3000)
ControlClick("数据安全","","Button8")
Sleep(3000)
ControlFocus("1 个已中断的操作","","DirectUIHWND1")
WinWait("[CLASS:OperationStatusWindow]","",10)
$sWindow = WinGetHandle("[CLASS:OperationStatusWindow]")
$dWindow = ControlGetHandle($sWindow,"","DirectUIHWND1")
ControlFocus("1 个已中断的操作","","DirectUIHWND1")
WinWait("[CLASS:OperationStatusWindow]","",10)
Sleep(3000)
ControlClick("1 个已中断的操作","","DirectUIHWND1")
Sleep(3000)
WinClose("[CLASS:OperationStatusWindow]", "");Close the currently active window