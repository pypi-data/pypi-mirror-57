#include <File.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIFiles.au3>
#include <WinAPISys.au3>

ControlFocus("���浯��","","")
WinWait("[CLASS:popupWindowClass]","",10)
Sleep(3000)
WinClose("[CLASS:popupWindowClass]", "");Close the currently active window
;Sleep(3000)
;ControlFocus("1 �����жϵĲ���","","DirectUIHWND1")
;WinWait("[CLASS:OperationStatusWindow]","",10)
;ControlClick("1 �����жϵĲ���","","DirectUIHWND1")
;Sleep(3000)
;WinClose("[CLASS:OperationStatusWindow]", "");Close the currently active window