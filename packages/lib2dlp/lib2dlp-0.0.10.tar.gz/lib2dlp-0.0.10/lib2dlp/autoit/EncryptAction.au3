#include <FileConstants.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIFiles.au3>
#include <File.au3>
#include <WinAPIFiles.au3>

$iFileTXT = _PathFull(@WorkingDir & "\..\Result\dlp.txt")
Local const $winxp = 'WIN_XP'
Local const $win7 = 'WIN_7'
Local const $win8 = 'WIN_8'
Local const $win81 = 'WIN_81'
Local const $win10 = 'WIN_10'
Local const $wuhq = '3PFTVS4-WUHQ'
Local const $dlp_pc_test_dlp = 'DLP-PC-TEST-DLP'
Local const $DESKTOP_CHQS1KQ = 'DESKTOP-CHQS1KQ'

If $CmdLine[0] <> 1 Then
   MsgBox("","error","缺少参数")
   Exit
Else
   Menu($CmdLine[1])
EndIf

Func Menu($flag)
   Switch $flag
	  Case 1;文件申请加白
		 Outaction()
	  Case 2;右键普通加密
		 Enaction()
	  Case 3;私有加密
		 EnPrivateaction()
	  Case 4;右键解密
		 DisENaction()
   EndSwitch
EndFunc
;刷新桌面
Func refreshicon()
   DllCall("shell32.dll", "none", "SHChangeNotify", "long", 134217728, "uint", BitOR(0, 4096), "ptr", 0, "ptr", 0)
   Return 1
EndFunc

;切换输入法到英语美式键盘
Func SwitchInput()
   $hWnd=WinGetHandle("[ACTIVE]");$hWnd 为目标窗口句柄，这里设置的是当前活动窗口
   $ret=DllCall("user32.dll","long","LoadKeyboardLayout","str","08040804","int",1+0)
   DllCall("user32.dll","ptr","SendMessage","hwnd",$hWnd,"int",0x50,"int",1,"int",$ret[0])
EndFunc

;激活Listary
Func OpenListary()
   Switch @OSVersion
	  Case $winxp
		 send("#s")
	  Case $win7
		 send("#s")
	  Case $win8
		 send("#g")
	  Case $win81
		 send("#g")
	  Case $win10
		 send("#f")
   EndSwitch
EndFunc

Func MoveToDLP()
   Switch @OSVersion
	  Case $winxp

	  Case $win7
		 If @IPAddress1 == '10.95.41.17' And @IPAddress1 <> '0.0.0.0' Then

		 ElseIf @IPAddress1 == '10.95.41.20' And @IPAddress1 <> '0.0.0.0' Then
			Sleep(3000)
			send("{UP 15}")
		 ElseIf @IPAddress1 == '10.95.27.75' And @IPAddress1 <> '0.0.0.0' Then

		 ElseIf @IPAddress1 == '10.95.27.83' And @IPAddress1 <> '0.0.0.0' Then

		 Else
			Exit
		 EndIf
	  Case $win8
		 If @IPAddress1 == '10.95.27.79' And @IPAddress1 <> '0.0.0.0' Then

		 ElseIf @IPAddress1 == '10.95.27.80' And @IPAddress1 <> '0.0.0.0' Then

		 Else
			Exit
		 EndIf
	  Case $win81
		 If @IPAddress1 == '10.95.27.76' And @IPAddress1 <> '0.0.0.0'  Then
			Sleep(3000)
			send("{UP 14}")
		 ElseIf @IPAddress1 == '10.95.27.77' And @IPAddress1 <> '0.0.0.0'  Then

		 Else
			Exit
		 EndIf
	  Case $win10
		 If @IPAddress1 == '10.95.27.116' And @IPAddress1 <> '0.0.0.0'  Then

		 ElseIf @IPAddress1 == '10.95.27.74' And @IPAddress1 <> '0.0.0.0'  Then

		 ElseIf @IPAddress1 == '172.24.83.62' And @IPAddress1 <> '0.0.0.0'  Then
			Sleep(3000)
			send("{UP 16}")
		 Else
			Exit
		 EndIf
   EndSwitch
EndFunc

;右键加密
Func Enaction()
   $iFileExists = FileExists($iFileTXT)
   If $iFileExists Then
	  FileCopy($iFileTXT, @DesktopDir & "\www.txt", $FC_OVERWRITE + $FC_CREATEPATH)
   Else
	  MsgBox($MB_SYSTEMMODAL, "", $iFileTXT & @CRLF & "The file doesn't exist.")
	  Return False
   EndIf
   Sleep(3000)
   refreshicon()
   ;切换输入法到英语美式键盘
   SwitchInput()
   ;激活Listary
   OpenListary()

   Sleep(3000)
   send("www.txt")

   Sleep(3000)
   send("^o")
   Sleep(3000)
   send("^p")
   ;移动到数据防泄漏
   MoveToDLP()
   Sleep(3000)
   send("{RIGHT}")
   Sleep(3000)
   send("{DOWN}")
   Sleep(3000)
   send("{ENTER}")
   Return True
EndFunc

;右键加密私有
Func EnPrivateaction()
   $iFileExists = FileExists($iFileTXT)
   If $iFileExists Then
	  FileCopy($iFileTXT, @DesktopDir & "\www.txt", $FC_OVERWRITE + $FC_CREATEPATH)
   Else
	  MsgBox($MB_SYSTEMMODAL, "", $iFileTXT & @CRLF & "The file doesn't exist.")
	  Return False
   EndIf
   Sleep(3000)
   refreshicon()
   ;切换输入法到英语美式键盘
   SwitchInput()
   ;激活Listary
   OpenListary()

   Sleep(3000)
   send("www.txt")

   Sleep(3000)
   send("^o")
   Sleep(3000)
   send("^p")
   ;移动到数据防泄漏
   MoveToDLP()
   Sleep(3000)
   send("{RIGHT}")
   Sleep(3000)
   send("{DOWN 2}")
   Sleep(3000)
   send("{ENTER}")
   Return True
EndFunc

;右键解密
Func DisENaction()
   Local Const $sFilePath = _PathFull(@DesktopDir & "\www.txt")
   Local $iFileExists = FileExists($sFilePath)
   If $iFileExists Then
	  refreshicon()
	  ;切换输入法到英语美式键盘
	  SwitchInput()
	  ;激活Listary
	  OpenListary()

	  Sleep(3000)
	  send("www.txt")

	  Sleep(3000)
	  send("^o")
	  Sleep(3000)
	  send("^p")
	  ;移动到数据防泄漏
	  MoveToDLP()
	  Sleep(3000)
	  send("{RIGHT}")
	  Sleep(3000)
	  send("{ENTER}")
	  Return True
   Else
	  MsgBox($MB_SYSTEMMODAL, "", $sFilePath & @CRLF & "The file doesn't exist.")
	  Return False
   EndIf

EndFunc

;外发申请
Func Outaction()
   $title = "数据安全"
   $text = "申请文件外发-我是自动的"
   $iFileExists = FileExists($iFileTXT)
   If $iFileExists Then
	  FileCopy($iFileTXT, @DesktopDir & "\www.txt", $FC_OVERWRITE + $FC_CREATEPATH)
   Else
	  MsgBox($MB_SYSTEMMODAL, "", $iFileTXT & @CRLF & "The file doesn't exist.")
	  Return False
   EndIf
   Sleep(3000)
   refreshicon()
   Sleep(3000)
   ;切换输入法到英语美式键盘
   SwitchInput()
   ;最小化活动窗口
   $hWnd=WinGetHandle("[CLASS:TkTopLevel]")
   WinSetState("$hWnd", "", @SW_MINIMIZE)
   Sleep(3000)
   ;激活Listary
   OpenListary()

   Sleep(3000)
   send("www.txt")

   Sleep(3000)
   send("^o")
   Sleep(3000)
   send("^p")
   ;移动到数据防泄漏
   MoveToDLP()
   Sleep(3000)
   send("{RIGHT}")
   Sleep(3000)
   send("{ENTER}")
   ControlFocus($title,"","Edit1")
   ControlClick($title,"","Edit1")
   Sleep(2000)
   ControlSetText($title,"", "Edit1", $text)
   Sleep(3000)
   ControlFocus($title,"","Button2")
   ControlClick($title,"","Button2")
   Return True
EndFunc
