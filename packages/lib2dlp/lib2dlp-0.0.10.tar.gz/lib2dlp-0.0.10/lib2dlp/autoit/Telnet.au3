AutoItSetOption("WinTitleMatchMode", 4)
Run("Cmd.exe")
Sleep(500)
; Rename window
$WinTitle="Telnet (NE Gateway)"
WinSetTitle("Telnet 10.95.41.15","",$WinTitle)
WinActivate($WinTitle,"")
$hWnd = WinGetHandle("classname=ConsoleWindowClass")

; Login and change to export directory
xSend($WinTitle," telnet  10.95.41.15",$hWnd)
xSend($WinTitle,"root",$hWnd)
xSend($WinTitle,"www.360.cn",$hWnd)
xSend($WinTitle,"Íõ±¦Ç¿",$hWnd)
xSend($WinTitle,"",$hWnd)
xSend($WinTitle,"logout",$hWnd)

; Extended send function
func xSend($aWinTitle,$aString,$hWnd)
  Sleep(200)
  WinActivate($aWinTitle,"")
  LoadKeyboardLayout("00000804",$hWnd)
  Send($aString & "{ENTER}")
endfunc

;Set current window input method
Func LoadKeyboardLayout($sLayoutID, $hWnd)
    Local $WM_INPUTLANGCHANGEREQUEST = 0x50
    Local $ret = DllCall("user32.dll", "long", "LoadKeyboardLayout", "str", $sLayoutID, "int", 1 + 0)
    DllCall("user32.dll", "ptr", "SendMessage", "hwnd", $hWnd, "int", $WM_INPUTLANGCHANGEREQUEST, "int", 1, "int", $ret[0])
EndFunc