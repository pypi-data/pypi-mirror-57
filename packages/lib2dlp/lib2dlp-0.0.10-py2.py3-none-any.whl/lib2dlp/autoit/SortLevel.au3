#include <FileConstants.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIFiles.au3>
#include <File.au3>
#include <WinAPIFiles.au3>
#include <WinAPIHObj.au3>

Local Const $sFile = @DesktopDir & '\sort.txt'
Local const $winxp = 'WIN_XP'
Local const $win7 = 'WIN_7'
Local const $win8 = 'WIN_8'
Local const $win81 = 'WIN_81'
Local const $win10 = 'WIN_10'
Local const $wuhq = '3PFTVS4-WUHQ'
Local const $dlp_pc_test_dlp = 'DLP-PC-TEST-DLP'
Local const $DESKTOP_CHQS1KQ = 'DESKTOP-CHQS1KQ'
Local $hFile, $sText, $nBytes, $tBuffer, $iSize, $sUserName, $sPassword, $sText


Switch @OSVersion
   Case $winxp

   Case $win7

   Case $win8

   Case $win81
	  If @ComputerName == $dlp_pc_test_dlp Then
		 ;While 1
			$sText = '—Ó Ôπ‚'
			$sUserName = "administrator"
			$sPassword = "www.360.cn"
			CreateFile($sText)
			RunNotepad($sUserName,$sPassword)
			Sleep(1000)
			MoveFile()
		 ;WEnd
	  Else
		 Exit
	  EndIf
   Case $win10
	  If @ComputerName == $wuhq Then
		 ;While 1
			$sText = '—Ó Ôπ‚'
			$sUserName = "wuhq"
			$sPassword = "1221"
			CreateFile($sText)
			RunNotepad($sUserName,$sPassword)
			Sleep(1000)
			MoveFile()
		 ;WEnd
	  ElseIf @ComputerName == $DESKTOP_CHQS1KQ Then
		 ;While 1
			$sText = '—Ó Ôπ‚'
			$sUserName = "administrator"
			$sPassword = "www.360.cn"
			CreateFile($sText)
			RunNotepad($sUserName,$sPassword)
			Sleep(1000)
			MoveFile()
		 ;WEnd
	  Else
		 Exit
	  EndIf
EndSwitch

Func RunNotepad($sUserName,$sPassword)
   Local $iFileExists = FileExists($sFile)
   If $iFileExists Then
	  Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_NOPROFILE, "notepad.exe " & $sFile, "", @SW_SHOWMAXIMIZED)
	  Sleep(3000)
	  WinWaitClose("[CLASS:Notepad]","",5)
	  ProcessClose($iPID)
	  Sleep(3000)
	  #cs
	  Local $iDelete = FileDelete($sFile)
	  If $iDelete Then
		 Return True
	  Else
		 MsgBox($MB_SYSTEMMODAL, "", "An error occurred whilst deleting the file.")
	  EndIf
	  #ce
	  Return True
   Else
	  Return False
	  Exit
   EndIf
   Return True
EndFunc

Func CreateFile($sText)
   Local $iFileExists = FileExists($sFile)
   If $iFileExists Then
	  FileDelete($sFile)
   Else
	  $tBuffer = DllStructCreate("byte[" & StringLen($sText) & "]")
	  DllStructSetData($tBuffer, 1, $sText)
	  $hFile = _WinAPI_CreateFile($sFile, 1)
	  _WinAPI_WriteFile($hFile, $tBuffer, StringLen($sText), $nBytes)
	  _WinAPI_CloseHandle($hFile)

	  Local $hFileOpen = FileOpen($sFile, $FO_OVERWRITE)
	  If $hFileOpen = -1 Then
		 ;MsgBox($MB_SYSTEMMODAL, "", "An error occurred whilst writing the temporary file.")
		 Return False
	  EndIf

	  FileWrite($hFileOpen, $sText & @CRLF)
	  FileWrite($hFileOpen, "This is still line 2 as a new line wasn't appended to the last FileWrite call." & @CRLF)
	  FileWrite($hFileOpen, "Line 3" & @CRLF)
	  FileWrite($hFileOpen, $sText)

	  FileFlush($hFileOpen)
	  Sleep(3000)
	  FileClose($hFileOpen)
	  ;$iSize = _WinAPI_GetFileSizeEx($hFile)
	  ;_WinAPI_CloseHandle($hFile)
	  ;ConsoleWrite('1):' & $iSize & ' ' & FileRead($sFile) & @CRLF)
	  ;FileDelete($sTempFile)
	  Return True
   EndIf
EndFunc

Func MoveFile()
   Local $dFile = _PathFull(@WorkingDir & "\..\DLP\Result\Sort\")
   FileMove($sFile, $dFile, $FC_OVERWRITE + $FC_CREATEPATH)
EndFunc

Func Example()
   Local $sUserName = "wuhq"
   Local $sPassword = "1221"
   ; Run Notepad with the window maximized.
   ;Local $iPID = Run("notepad.exe", "", @SW_SHOWMAXIMIZED)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_NOPROFILE, "notepad.exe", "", @SW_SHOWMAXIMIZED)

   ; Wait 10 seconds for the Notepad window to appear.
   WinWait("[CLASS:Notepad]", "", 10)

   $sHwd = WinGetHandle("[CLASS:Notepad]")

   ; Wait for 2 seconds.
   Sleep(2000)
   ControlFocus($sHwd,"","Edit1")
   send("—Ó Ôπ‚")
   ;ControlSetText($sHwd,"", "Edit1", "—Ó Ôπ‚")

   Sleep(2000)
   ;ƒ£ƒ‚ctrl+enter
   send("{CTRLDOWN}{s}")
   Sleep(100)
   Send("{CTRLUP}")

   ControlFocus("¡Ì¥ÊŒ™","","Edit1")
   Sleep(1000)
   ControlSetText("¡Ì¥ÊŒ™","", "Edit1", @DesktopDir & "\ya.txt")
   Sleep(1000)
   ControlFocus("¡Ì¥ÊŒ™","","Button2")
   ControlClick("¡Ì¥ÊŒ™","","Button2")
   ; Close the Notepad process using the PID returned by Run.
   ;ProcessClose($iPID)
EndFunc