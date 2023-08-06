#include <MsgBoxConstants.au3>

Local $i = ProcessExists("python.exe")

If $i == 0 Then ; Check if the python process is running.
   ;MsgBox($MB_SYSTEMMODAL, "", "python is running")
Else
   ;MsgBox($MB_SYSTEMMODAL, "", "python is not running")
   ProcessClose("python.exe")
   While $i <> 0
	  ;ProcessClose("python.exe")
	  If $i == 0 Then ; Check if the python process is running.
		 ;MsgBox($MB_SYSTEMMODAL, "", "python is running")
		 $i = 0
	  Else
		 ;MsgBox($MB_SYSTEMMODAL, "", "python is not running")
		 ProcessClose("python.exe")
		 $i = 0
	  EndIf
   WEnd
EndIf

