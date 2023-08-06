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
;Local $iFile = _PathFull(@WorkingDir & "\data\dlp.doc");��python���õ�ʱ����Ҫ��DLP·��
Local $dFile = _PathFull(@DesktopDir & "\print.xps")
Local $pFile = _PathFull(@WorkingDir & "\log\print.txt")
Local $iIsPrinted


If $CmdLine[0] <> 1 Then
   MsgBox("","error","ȱ�ٲ���")
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
   ControlFocus("�ļ����Ϊ","","Edit1")
   WinWait("[CLASS:#32770]","",10)
   Sleep(10000)
   ControlSetText("�ļ����Ϊ","", "Edit1", @DesktopDir & "\print.xps")
   Sleep(2000)
   ControlClick("�ļ����Ϊ","","Button1")
   Sleep(3000)
   refreshicon()
   Local $t = ControlFocus("ȷ�����Ϊ","","Button1")
   If $t = 1 Then
	  ControlFocus("ȷ�����Ϊ","","Button1")
	  Sleep(2000)
	  ControlClick("ȷ�����Ϊ","","Button1")
	  Sleep(3000)
	  refreshicon()
   Else
	  Sleep(2000)
	  ControlClick("�ļ����Ϊ","","Button1")
	  ControlFocus("����ӡ������Ϊ","","Button3")
	  Sleep(2000)
	  ControlClick("����ӡ������Ϊ","","Button3")
	  ControlFocus("���±�","","Button1")
	  Sleep(2000)
	  ControlClick("���±�","","Button1")
	  Sleep(3000)
	  refreshicon()
   EndIf
EndFunc
Func PrintWin10()
   ;$begin = TimerInit()
   Sleep(3000)
   ControlFocus("����ӡ������Ϊ","","Edit1")
   WinWait("[CLASS:#32770]","",10)
   Sleep(5000)
   ControlSetText("����ӡ������Ϊ","", "Edit1", @DesktopDir & "\print.xps")
   Sleep(2000)
   ControlClick("����ӡ������Ϊ","","Button2")
   Sleep(3000)
   refreshicon()
   Local $t = ControlFocus("ȷ�����Ϊ","","Button1")
   If $t = 1 Then
	  ControlFocus("ȷ�����Ϊ","","Button1")
	  Sleep(2000)
	  ControlClick("ȷ�����Ϊ","","Button1")
	  Sleep(3000)
	  refreshicon()
   Else
	  Sleep(2000)
	  ControlClick("�ļ����Ϊ","","Button1")
	  ControlFocus("����ӡ������Ϊ","","Button3")
	  Sleep(2000)
	  ControlClick("����ӡ������Ϊ","","Button3")
	  ControlFocus("���±�","","Button1")
	  Sleep(2000)
	  ControlClick("���±�","","Button1")
	  Sleep(3000)
	  refreshicon()
   EndIf
EndFunc

Func PrintWin81()
   ControlFocus("����ӡ������Ϊ","","Edit1")
   WinWait("[CLASS:#32770]","",10)
   Sleep(15000)
   ControlSetText("����ӡ������Ϊ","", "Edit1", @DesktopDir & "\print.xps")
   Sleep(2000)
   ControlClick("����ӡ������Ϊ","","Button1")
   Sleep(3000)
   refreshicon()
   Local $t = ControlFocus("ȷ�����Ϊ","","Button1")
   If $t = 1 Then
	  ControlFocus("ȷ�����Ϊ","","Button1")
	  Sleep(2000)
	  ControlClick("ȷ�����Ϊ","","Button1")
	  Sleep(3000)
	  refreshicon()
   Else
	  Sleep(2000)
	  ControlClick("�ļ����Ϊ","","Button1")
	  ControlFocus("����ӡ������Ϊ","","Button3")
	  Sleep(2000)
	  ControlClick("����ӡ������Ϊ","","Button3")
	  ControlFocus("���±�","","Button1")
	  Sleep(2000)
	  ControlClick("���±�","","Button1")
	  Sleep(3000)
	  refreshicon()
   EndIf
EndFunc
;ˢ������
Func refreshicon()
   DllCall("shell32.dll", "none", "SHChangeNotify", "long", 134217728, "uint", BitOR(0, 4096), "ptr", 0, "ptr", 0)
   Return 1
EndFunc
#comments-start
If $iIsPrinted Then
   Sleep(5000)
   ControlFocus("����ӡ������Ϊ","","Edit1")
   WinWait("[CLASS:#32770]","",10)
   ControlSetText("����ӡ������Ϊ","", "Edit1", @DesktopDir & "\print.xps")
   Sleep(2000)
   ControlClick("����ӡ������Ϊ","","Button2")
   Sleep(2000)
   Local $t = ControlFocus("ȷ�����Ϊ","","Button1")
   If $t = 1 Then
	  ControlFocus("ȷ�����Ϊ","","Button1")
	  Sleep(2000)
	  ControlClick("ȷ�����Ϊ","","Button1")
   Else
	  Sleep(2000)
	  ControlClick("�ļ����Ϊ","","Button1")
	  ControlFocus("����ӡ������Ϊ","","Button3")
	  Sleep(2000)
	  ControlClick("����ӡ������Ϊ","","Button3")
	  ControlFocus("���±�","","Button1")
	  Sleep(2000)
	  ControlClick("���±�","","Button1")
   EndIf
Else
   Exit
EndIf
#comments-end


#cs
Sleep(5000)
	  ControlFocus("�ļ����Ϊ","","Edit1")
	  WinWait("[CLASS:#32770]","",10)
	  ControlSetText("�ļ����Ϊ","", "Edit1", @DesktopDir & "\print.xps")
	  Sleep(2000)
	  ControlClick("�ļ����Ϊ","","Button1")
	  Sleep(3000)
	  refreshicon()
	  Local $t = ControlFocus("ȷ�����Ϊ","","Button1")
	  If $t = 1 Then
		 ControlFocus("ȷ�����Ϊ","","Button1")
		 Sleep(2000)
		 ControlClick("ȷ�����Ϊ","","Button1")
		 Sleep(3000)
		 refreshicon()
	  Else
		 Sleep(2000)
		 ControlClick("�ļ����Ϊ","","Button1")
		 ControlFocus("����ӡ������Ϊ","","Button3")
		 Sleep(2000)
		 ControlClick("����ӡ������Ϊ","","Button3")
		 ControlFocus("���±�","","Button1")
		 Sleep(2000)
		 ControlClick("���±�","","Button1")
		 Sleep(3000)
		 refreshicon()
	  EndIf
#ce