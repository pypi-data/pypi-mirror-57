#include <File.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIFiles.au3>
#include <WinAPISys.au3>

ControlFocus("公告弹窗","","")
WinWait("[CLASS:popupWindowClass]","",10)
Sleep(3000)
WinClose("[CLASS:popupWindowClass]", "");Close the currently active window
;Sleep(3000)
;ControlFocus("1 个已中断的操作","","DirectUIHWND1")
;WinWait("[CLASS:OperationStatusWindow]","",10)
;ControlClick("1 个已中断的操作","","DirectUIHWND1")
;Sleep(3000)
;WinClose("[CLASS:OperationStatusWindow]", "");Close the currently active window