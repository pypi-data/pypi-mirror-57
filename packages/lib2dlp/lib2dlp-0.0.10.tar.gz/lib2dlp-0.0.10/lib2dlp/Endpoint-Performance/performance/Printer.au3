#include <File.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIFiles.au3>
#include <WinAPISys.au3>
#include <Timers.au3>

Local const $winxp = 'WIN_XP'
Local const $win7 = 'WIN_7'
Local const $win8 = 'WIN_8'
Local const $win81 = 'WIN_81'
Local const $win10 = 'WIN_10'

Local $isPrinter = _WinAPI_SetDefaultPrinter("Microsoft XPS Document Writer")
If @error Then Exit
;Local $iFile = _PathFull(@WorkingDir & "\data\dlp.doc");给python调用的时候需要加DLP路径
Local $dFile = _PathFull(@DesktopDir & "\print.xps")
Local $pFile = _PathFull(@WorkingDir & "\log\print.txt")
Local $iIsPrinted


If $CmdLine[0] <> 1 Then
   MsgBox("","error","缺少参数")
   Exit
Else
   Switch @OSVersion
	  Case $winxp
		 FilePrint($CmdLine[1])
		 Sleep(5000)
		 PrintWin7()
	  Case $win7
		 Local $s = 0
		 $begin = TimerInit()
		 FilePrint($CmdLine[1])
		 Sleep(3000)
		 PrintWin7()
		 Sleep(5000)
		 WinWait("[CLASS:OpusApp]", "", 30)
		 If WinExists("[CLASS:OpusApp]") Then
			WinClose("[CLASS:OpusApp]", "")
		 EndIf
		 $dif = TimerDiff($begin)
		 $totaltime = $dif - 58000
		 WriteTime($totaltime)
		 $s = $s + 1
		 Sleep(3000)
	  Case $win8
		 FilePrint($CmdLine[1])
		 Sleep(5000)
		 PrintWin81()
	  Case $win81
		 FilePrint($CmdLine[1])
		 Sleep(5000)
		 PrintWin81()
	  Case $win10
		 Local $s = 0
		 While $s < 2
			FilePrint($CmdLine[1])
			Sleep(1000)
			PrintWin10()
			$s = $s + 1
		 WEnd
   EndSwitch
EndIf

Func FilePrint($iFile)
   ;$begin = TimerInit()
   $iIsPrinted = _FilePrint($iFile,@SW_SHOW)
   ;$dif = TimerDiff($begin)
   If $iIsPrinted Then
	  ;WriteTime($dif)
	  FileDelete($dFile)
	  Return True
   Else
	  ;MsgBox($MB_SYSTEMMODAL, "", "Error: " & @error & @CRLF & "The file was not printed.")
	  Return False
   EndIf
EndFunc


Func WriteTime($str)
    Local $hFileOpen = FileOpen($pFile, $FO_APPEND)
    If $hFileOpen = -1 Then
        ;MsgBox($MB_SYSTEMMODAL, "", "An error occurred whilst writing the temporary file.")
        Return False
    EndIf

    ; Write data to the file using the handle returned by FileOpen.
    FileWriteLine($hFileOpen, $str)

    ; Close the handle returned by FileOpen.
    FileClose($hFileOpen)
EndFunc

Func PrintWin7()
   ControlFocus("文件另存为","","Edit1")
   WinWait("[CLASS:#32770]","",10)
   Sleep(10000)
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
EndFunc
Func PrintWin10()
   ;$begin = TimerInit()
   Sleep(3000)
   ControlFocus("将打印输出另存为","","Edit1")
   WinWait("[CLASS:#32770]","",10)
   Sleep(5000)
   ControlSetText("将打印输出另存为","", "Edit1", @DesktopDir & "\print.xps")
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
   ControlSetText("将打印输出另存为","", "Edit1", @DesktopDir & "\print.xps")
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