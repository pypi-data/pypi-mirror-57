#include <File.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIFiles.au3>
#include <WinAPISys.au3>
Local const $winxp = 'WIN_XP'
Local const $win7 = 'WIN_7'
Local const $win8 = 'WIN_8'
Local const $win81 = 'WIN_81'
Local const $win10 = 'WIN_10'

Local $isPrinter = _WinAPI_SetDefaultPrinter("Microsoft XPS Document Writer")
If @error Then Exit
Local $iFile = _PathFull(@WorkingDir & "\..\DLP\file\dlp.txt");给python调用的时候需要加DLP路径
Local $iFileC = "C:\DLP\file\dlp.txt"
Local $iFileD = "D:\DLP\file\dlp.txt"
Local $iIsPrinted

Local Const $sFilePath = "C:\printtest"
If FileExists($sFilePath) Then
   DirRemove($sFilePath, $DIR_REMOVE)
EndIf
Sleep(3000)
DirCreate($sFilePath)
Sleep(5000)

Switch @OSVersion
   Case $winxp
	  FilePrint($iFileD)
	  Sleep(5000)
	  PrintWin7()
   Case $win7
	  If @IPAddress1 == '10.95.41.17' And @IPAddress1 <> '0.0.0.0' Then
		 FilePrint($iFileD)
		 Sleep(5000)
		 PrintWin7()
	  ElseIf @IPAddress1 == '10.95.41.20' And @IPAddress1 <> '0.0.0.0' Then
		 FilePrint($iFileD)
		 Sleep(5000)
		 PrintWin7()
	  ElseIf @IPAddress1 == '10.95.27.75' And @IPAddress1 <> '0.0.0.0' Then
		 FilePrint($iFileC)
		 Sleep(5000)
		 PrintWin7()
	  ElseIf @IPAddress1 == '10.95.27.83' And @IPAddress1 <> '0.0.0.0' Then
		 FilePrint($iFileC)
		 Sleep(5000)
		 PrintWin7()
	  EndIf
   Case $win8
	  If @IPAddress1 == '10.95.27.79' And @IPAddress1 <> '0.0.0.0' Then
		 FilePrint($iFileC)
		 Sleep(5000)
		 PrintWin81()
	  ElseIf @IPAddress1 == '10.95.27.80' And @IPAddress1 <> '0.0.0.0' Then
		 FilePrint($iFileD)
		 Sleep(5000)
		 PrintWin81()
	  EndIf
   Case $win81
	  If @IPAddress1 == '10.95.27.76' And @IPAddress1 <> '0.0.0.0'  Then
		 FilePrint($iFileD)
		 Sleep(5000)
		 PrintWin81()
	  ElseIf @IPAddress1 == '10.95.27.77' And @IPAddress1 <> '0.0.0.0'  Then
		 FilePrint($iFileC)
		 Sleep(5000)
		 PrintWin81()
	  EndIf
   Case $win10
	  If @IPAddress1 == '10.95.27.116' And @IPAddress1 <> '0.0.0.0'  Then
		 FilePrint($iFileD)
		 Sleep(5000)
		 PrintWin10()
	  ElseIf @IPAddress1 == '10.95.27.74' And @IPAddress1 <> '0.0.0.0'  Then
		 FilePrint($iFileD)
		 Sleep(5000)
		 PrintWin10()
	  EndIf
EndSwitch

Func FilePrint($iFile)
   $iIsPrinted = _FilePrint($iFile,@SW_SHOW)
   If $iIsPrinted Then
	  Return True
   Else
	  MsgBox($MB_SYSTEMMODAL, "", "Error: " & @error & @CRLF & "The file was not printed.")
	  Return False
   EndIf
EndFunc

Func PrintWin7()
   ControlFocus("文件另存为","","Edit1")
   WinWait("[CLASS:#32770]","",10)
   Sleep(10000)
   ;ControlSetText("文件另存为","", "Edit1", @DesktopDir & "\print.xps")
   ControlSetText("文件另存为","", "Edit1", "C:\printtest\print.xps")
   Sleep(2000)
   ControlClick("文件另存为","","Button1")
   Sleep(3000)
   refreshicon()
   Local $t = ControlFocus("确认另存为","","Button1")
   If $t = 1 Then
	  ControlFocus("确认另存为","","Button1")
	  Sleep(2000)
	  ControlClick("确认另存为","","Button1")
	  Sleep(3000)
	  refreshicon()
   Else
	  Sleep(2000)
	  ControlClick("文件另存为","","Button1")
	  ControlFocus("将打印输出另存为","","Button3")
	  Sleep(2000)
	  ControlClick("将打印输出另存为","","Button3")
	  ControlFocus("记事本","","Button1")
	  Sleep(2000)
	  ControlClick("记事本","","Button1")
	  Sleep(3000)
	  refreshicon()
   EndIf
EndFunc
Func PrintWin10()
   ControlFocus("将打印输出另存为","","Edit1")
   WinWait("[CLASS:#32770]","",10)
   Sleep(5000)
   ;ControlSetText("将打印输出另存为","", "Edit1", @DesktopDir & "\print.xps")
   ControlSetText("将打印输出另存为","", "Edit1", "C:\printtest\print.xps")
   Sleep(2000)
   ControlClick("将打印输出另存为","","Button2")
   Sleep(3000)
   refreshicon()
   Local $t = ControlFocus("确认另存为","","Button1")
   If $t = 1 Then
	  ControlFocus("确认另存为","","Button1")
	  Sleep(2000)
	  ControlClick("确认另存为","","Button1")
	  Sleep(3000)
	  refreshicon()
   Else
	  Sleep(2000)
	  ControlClick("文件另存为","","Button1")
	  ControlFocus("将打印输出另存为","","Button3")
	  Sleep(2000)
	  ControlClick("将打印输出另存为","","Button3")
	  ControlFocus("记事本","","Button1")
	  Sleep(2000)
	  ControlClick("记事本","","Button1")
	  Sleep(3000)
	  refreshicon()
   EndIf
EndFunc

Func PrintWin81()
   ControlFocus("将打印输出另存为","","Edit1")
   WinWait("[CLASS:#32770]","",10)
   Sleep(15000)
   ;ControlSetText("将打印输出另存为","", "Edit1", @DesktopDir & "\print.xps")
   ControlSetText("将打印输出另存为","", "Edit1", "C:\printtest\print.xps")
   Sleep(2000)
   ControlClick("将打印输出另存为","","Button1")
   Sleep(3000)
   refreshicon()
   Local $t = ControlFocus("确认另存为","","Button1")
   If $t = 1 Then
	  ControlFocus("确认另存为","","Button1")
	  Sleep(2000)
	  ControlClick("确认另存为","","Button1")
	  Sleep(3000)
	  refreshicon()
   Else
	  Sleep(2000)
	  ControlClick("文件另存为","","Button1")
	  ControlFocus("将打印输出另存为","","Button3")
	  Sleep(2000)
	  ControlClick("将打印输出另存为","","Button3")
	  ControlFocus("记事本","","Button1")
	  Sleep(2000)
	  ControlClick("记事本","","Button1")
	  Sleep(3000)
	  refreshicon()
   EndIf
EndFunc
;刷新桌面
Func refreshicon()
   DllCall("shell32.dll", "none", "SHChangeNotify", "long", 134217728, "uint", BitOR(0, 4096), "ptr", 0, "ptr", 0)
   Return 1
EndFunc
#comments-start
If $iIsPrinted Then
   Sleep(5000)
   ControlFocus("将打印输出另存为","","Edit1")
   WinWait("[CLASS:#32770]","",10)
   ControlSetText("将打印输出另存为","", "Edit1", @DesktopDir & "\print.xps")
   Sleep(2000)
   ControlClick("将打印输出另存为","","Button2")
   Sleep(2000)
   Local $t = ControlFocus("确认另存为","","Button1")
   If $t = 1 Then
	  ControlFocus("确认另存为","","Button1")
	  Sleep(2000)
	  ControlClick("确认另存为","","Button1")
   Else
	  Sleep(2000)
	  ControlClick("文件另存为","","Button1")
	  ControlFocus("将打印输出另存为","","Button3")
	  Sleep(2000)
	  ControlClick("将打印输出另存为","","Button3")
	  ControlFocus("记事本","","Button1")
	  Sleep(2000)
	  ControlClick("记事本","","Button1")
   EndIf
Else
   Exit
EndIf
#comments-end


#cs
Sleep(5000)
	  ControlFocus("文件另存为","","Edit1")
	  WinWait("[CLASS:#32770]","",10)
	  ControlSetText("文件另存为","", "Edit1", @DesktopDir & "\print.xps")
	  Sleep(2000)
	  ControlClick("文件另存为","","Button1")
	  Sleep(3000)
	  refreshicon()
	  Local $t = ControlFocus("确认另存为","","Button1")
	  If $t = 1 Then
		 ControlFocus("确认另存为","","Button1")
		 Sleep(2000)
		 ControlClick("确认另存为","","Button1")
		 Sleep(3000)
		 refreshicon()
	  Else
		 Sleep(2000)
		 ControlClick("文件另存为","","Button1")
		 ControlFocus("将打印输出另存为","","Button3")
		 Sleep(2000)
		 ControlClick("将打印输出另存为","","Button3")
		 ControlFocus("记事本","","Button1")
		 Sleep(2000)
		 ControlClick("记事本","","Button1")
		 Sleep(3000)
		 refreshicon()
	  EndIf
#ce
