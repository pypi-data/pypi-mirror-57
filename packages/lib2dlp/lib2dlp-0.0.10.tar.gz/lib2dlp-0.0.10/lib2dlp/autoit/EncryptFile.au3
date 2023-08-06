#include <FileConstants.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIFiles.au3>
#include <File.au3>
#include <WinAPIFiles.au3>

Local $sFilePath = @DesktopDir & '\encfile.txt'
Local $sText
Local const $winxp = 'WIN_XP'
Local const $win7 = 'WIN_7'
Local const $win8 = 'WIN_8'
Local const $win81 = 'WIN_81'
Local const $win10 = 'WIN_10'
Local const $wuhq = '3PFTVS4-WUHQ'
Local const $dlp_pc_test_dlp = 'DLP-PC-TEST-DLP'
Local const $DESKTOP_CHQS1KQ = 'DESKTOP-CHQS1KQ'

Switch @OSVersion
   Case $winxp

   Case $win7

   Case $win8

   Case $win81
	  If @ComputerName == $dlp_pc_test_dlp Then
		 ;While 1
			$sText = '—Ó Ôπ‚'
			WriteFile($sText,$sFilePath)
			MoveFile()
			;Sleep(10)
		 ;WEnd
	  Else
		 Exit
	  EndIf
   Case $win10
	  If @ComputerName == $wuhq Then
		 ;While 1
			$sText = '—Ó Ôπ‚'
			WriteFile($sText,$sFilePath)
			MoveFile()
			;Sleep(10)
		 ;WEnd
	  ElseIf @ComputerName == $DESKTOP_CHQS1KQ Then
		 ;While 1
			$sText = '—Ó Ôπ‚'
			WriteFile($sText,$sFilePath)
			MoveFile()
			;Sleep(10)
		 ;WEnd
	  Else
		 Exit
	  EndIf
EndSwitch

Func WriteFile($sText,$sFilePath)

    ;Local Const $sFilePath = _WinAPI_GetTempFileName(@DesktopDir)

    If Not FileWrite($sFilePath, "Start of the FileWrite example, line 1. " & @CRLF) Then
        ;MsgBox($MB_SYSTEMMODAL, "", "An error occurred whilst writing the temporary file.")
        Return False
    EndIf

    #cs
    If Not _FileCreate(@DesktopDir & "ya.txt") Then
        ;MsgBox($MB_SYSTEMMODAL, "Error", " Error Creating/Resetting log.      error:" & @error)
		Return False
    EndIf
    #ce
    Local $hFileOpen = FileOpen($sFilePath, $FO_APPEND)
    If $hFileOpen = -1 Then
        ;MsgBox($MB_SYSTEMMODAL, "", "An error occurred whilst writing the temporary file.")
        Return False
    EndIf

    FileWrite($hFileOpen, $sText & @CRLF)
    FileWrite($hFileOpen, "This is still line 2 as a new line wasn't appended to the last FileWrite call." & @CRLF)
    FileWrite($hFileOpen, "Line 3" & @CRLF)
    FileWrite($hFileOpen, $sText)

    FileFlush($hFileOpen)
    FileClose($hFileOpen)

    $attr = FileGetAttrib($sFilePath)
    ;MsgBox("","",$attr)
    Sleep(100)

    ;FileDelete($sFilePath)
EndFunc

Func MoveFile()
   Local $dFile = _PathFull(@WorkingDir & "\..\DLP\Result\EncryptFile\")
   FileMove($sFilePath, $dFile, $FC_OVERWRITE + $FC_CREATEPATH)
EndFunc