#include <AutoItConstants.au3>
#include <MsgBoxConstants.au3>
#include <FileConstants.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIFiles.au3>

Local const $winxp = 'WIN_XP'
Local const $win7 = 'WIN_7'
Local const $win8 = 'WIN_8'
Local const $win81 = 'WIN_81'
Local const $win10 = 'WIN_10'
Local const $wuhq = '3PFTVS4-WUHQ'
Local const $tim = 'Tim-PC'
Local $iFile = _PathFull(@WorkingDir & "\..\Result")

Switch @OSVersion
   Case $winxp

   Case $win7
	  If @ComputerName == $tim Then
		 ;udriver("dlp.doc")
		 udriverall()
	  Else
		 Exit
	  EndIf
   Case $win8

   Case $win81

   Case $win10
	  If @ComputerName == $wuhq Then
		 udriver("dlp.doc")
	  Else
		 Exit
	  EndIf
EndSwitch

Func udriver($filename)
   Local $aArray = DriveGetDrive($DT_REMOVABLE)
   Sleep(3000)
   Local $iFileExists = FileExists(@WorkingDir & "\" & $filename)

   ;MsgBox($MB_SYSTEMMODAL, "", "Drive " & "/" & $aArray[1] & ":" & @CRLF & StringUpper($aArray[1]))

   If Not @error And $iFileExists = 1 Then
	  FileCopy(@WorkingDir & "\" & $filename, $aArray[1] & "\", $FC_OVERWRITE + $FC_CREATEPATH)
   Else
	  Exit
   EndIf
EndFunc

Func udriverall()
   Local $aArray = DriveGetDrive($DT_REMOVABLE)
   Sleep(3000)

   ;MsgBox($MB_SYSTEMMODAL, "", "Drive " & "/" & $aArray[1] & ":" & @CRLF & StringUpper($aArray[1]))

   If Not @error = 1 Then
	  FileCopy($iFile & "\*.*", $aArray[1] & "\", $FC_OVERWRITE + $FC_CREATEPATH)
   Else
	  Exit
   EndIf
EndFunc