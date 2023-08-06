#include <FileConstants.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIFiles.au3>
#include <File.au3>
#include <WinAPIFiles.au3>
#include <WinAPIHObj.au3>
#include <Process.au3>

Local Const $sFile = @DesktopDir & '\wa.txt'
Local Const $AllAuth = "AllAuth.txt"
Local Const $AllDisAuth = "AllDisAuth.txt"
Local Const $DisPrint = "DisPrint.txt"
Local Const $DisReAuth = "DisReAuth.txt"
Local Const $DisPrintScn = "DisPrintScn.txt"
Local Const $DisCopy = "DisCopy.txt"
Local Const $DisOfflineUse = "DisOfflineUse.txt"
Local Const $X64 = 'X64'
Local Const $X86 = 'X86'
Local const $winxp = 'WIN_XP'
Local const $win7 = 'WIN_7'
Local const $win8 = 'WIN_8'
Local const $win81 = 'WIN_81'
Local const $win10 = 'WIN_10'
Local const $wuhq = '3PFTVS4-WUHQ'
Local const $dlp_pc_test_dlp = 'DLP-PC-TEST-DLP'
Local const $DESKTOP_CHQS1KQ = 'DESKTOP-CHQS1KQ'
Local $sUserName, $sPassword, $flag, $sText, $hFile, $nBytes, $tBuffer, $fJson

If $CmdLine[0] <> 1 Then
   MsgBox("","error","缺少参数")
   Exit
Else
   Switch @OSVersion
	  Case $winxp

	  Case $win7

	  Case $win8

	  Case $win81
		 If @ComputerName == $dlp_pc_test_dlp Then
			$sText = '{'
			$sUserName = "administrator"
			$sPassword = "www.360.cn"
			CreateJsonFile($sFile)
			GrantAdmin($sUserName,$sPassword,$CmdLine[1])
		 Else
			Exit
		 EndIf
	  Case $win10
		 If @ComputerName == $wuhq Then
			$sText = '{'
			$sUserName = "wuhq"
			$sPassword = "1221"
			CreateJsonFile($sFile)
			Grant($sUserName,$sPassword,$CmdLine[1])
		 ElseIf @ComputerName == $DESKTOP_CHQS1KQ Then
			$sText = '{'
			$sUserName = "administrator"
			$sPassword = "www.360.cn"
			CreateJsonFile($sFile)
			GrantAdmin($sUserName,$sPassword,$CmdLine[1])
		 Else
			Exit
		 EndIf
   EndSwitch
EndIf

Func Grant($sUserName,$sPassword,$flag)
   If @OSArch == $X64 Then
	  Switch $flag
		 Case 1;所有权限都允许
			AllAuth64()
			Sleep(10000)
			MoveFile($AllAuth)
		 Case 2;所有权限都禁止
			AllDisAuth64()
			Sleep(10000)
			MoveFile($AllDisAuth)
		 Case 3;禁止打印
			DisPrint64()
			Sleep(10000)
			MoveFile($DisPrint)
		 Case 4;禁止再授权
			DisReAuth64()
			Sleep(10000)
			MoveFile($DisReAuth)
		 Case 5;禁止截屏
			DisPrintScn64()
			Sleep(10000)
			MoveFile($DisPrintScn)
		 Case 6;禁止拷贝
			DisCopy64()
			Sleep(10000)
			MoveFile($DisCopy)
		 Case 7;禁止离线使用
			DisOfflineUse64()
			Sleep(10000)
			MoveFile($DisOfflineUse)
	  EndSwitch
   ElseIf @OSArch == $X86 Then
	  Switch $flag
		 Case 1;所有权限都允许
			AllAuth32()
			Sleep(10000)
			MoveFile($AllAuth)
		 Case 2;所有权限都禁止
			AllDisAuth32()
			Sleep(10000)
			MoveFile($AllDisAuth)
		 Case 3;禁止打印
			DisPrint32()
			Sleep(10000)
			MoveFile($DisPrint)
		 Case 4;禁止再授权
			DisReAuth32()
			Sleep(10000)
			MoveFile($DisReAuth)
		 Case 5;禁止截屏
			DisPrintScn32()
			Sleep(10000)
			MoveFile($DisPrintScn)
		 Case 6;禁止拷贝
			DisCopy32()
			Sleep(10000)
			MoveFile($DisCopy)
		 Case 7;禁止离线使用
			DisOfflineUse32()
			Sleep(10000)
			MoveFile($DisOfflineUse)
	  EndSwitch
   Else
	  Exit
   EndIf
EndFunc

Func GrantAdmin($sUserName,$sPassword,$flag)
   If @OSArch == $X64 Then
	  Switch $flag
		 Case 1;所有权限都允许
			AllAuth64admin()
			Sleep(10000)
			MoveFile($AllAuth)
		 Case 2;所有权限都禁止
			AllDisAuth64admin()
			Sleep(10000)
			MoveFile($AllDisAuth)
		 Case 3;禁止打印
			DisPrint64admin()
			Sleep(10000)
			MoveFile($DisPrint)
		 Case 4;禁止再授权
			DisReAuth64admin()
			Sleep(10000)
			MoveFile($DisReAuth)
		 Case 5;禁止截屏
			DisPrintScn64admin()
			Sleep(10000)
			MoveFile($DisPrintScn)
		 Case 6;禁止拷贝
			DisCopy64admin()
			Sleep(10000)
			MoveFile($DisCopy)
		 Case 7;禁止离线使用
			DisOfflineUse64admin()
			Sleep(10000)
			MoveFile($DisOfflineUse)
	  EndSwitch
   ElseIf @OSArch == $X86 Then
	  Switch $flag
		 Case 1;所有权限都允许
			AllAuth32admin()
			Sleep(10000)
			MoveFile($AllAuth)
		 Case 2;所有权限都禁止
			AllDisAuth32admin()
			Sleep(10000)
			MoveFile($AllDisAuth)
		 Case 3;禁止打印
			DisPrint32admin()
			Sleep(10000)
			MoveFile($DisPrint)
		 Case 4;禁止再授权
			DisReAuth32admin()
			Sleep(10000)
			MoveFile($DisReAuth)
		 Case 5;禁止截屏
			DisPrintScn32admin()
			Sleep(10000)
			MoveFile($DisPrintScn)
		 Case 6;禁止拷贝
			DisCopy32admin()
			Sleep(10000)
			MoveFile($DisCopy)
		 Case 7;禁止离线使用
			DisOfflineUse32admin()
			Sleep(10000)
			MoveFile($DisOfflineUse)
	  EndSwitch
   Else
	  Exit
   EndIf
EndFunc

Func AllAuth64()
   ;ProcessClose("DLPGrant_64.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configAllAuth.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_64.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 10)
   Sleep(3000)
EndFunc

Func AllDisAuth64()
   ;ProcessClose("DLPGrant_64.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configAllDisAuth.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_64.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 10)
   Sleep(3000)
EndFunc

Func DisPrint64()
   ;ProcessClose("DLPGrant_64.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisPrint.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_64.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 10)
   Sleep(3000)
EndFunc

Func DisReAuth64()
   ;ProcessClose("DLPGrant_64.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisReAuth.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_64.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 10)
   Sleep(3000)
EndFunc

Func DisPrintScn64()
   ;ProcessClose("DLPGrant_64.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisPrintScn.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_64.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 10)
   Sleep(3000)
EndFunc

Func DisCopy64()
   ;ProcessClose("DLPGrant_64.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisCopy.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_64.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 10)
   Sleep(3000)
EndFunc

Func DisOfflineUse64()
   ;ProcessClose("DLPGrant_64.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisOfflineUse.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_64.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 10)
   Sleep(3000)
EndFunc

Func AllAuth32()
   ;ProcessClose("DLPGrant_32.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configAllAuth.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_32.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 10)
   Sleep(3000)
EndFunc

Func AllDisAuth32()
   ;ProcessClose("DLPGrant_32.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configAllDisAuth.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_32.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 10)
   Sleep(3000)
EndFunc

Func DisPrint32()
   ;ProcessClose("DLPGrant_32.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisPrint.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_32.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 10)
   Sleep(3000)
EndFunc

Func DisReAuth32()
   ;ProcessClose("DLPGrant_32.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisReAuth.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_32.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 10)
   Sleep(3000)
EndFunc

Func DisPrintScn32()
   ;ProcessClose("DLPGrant_32.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisPrintScn.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_32.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 10)
   Sleep(3000)
EndFunc

Func DisCopy32()
   ;ProcessClose("DLPGrant_32.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisCopy.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_32.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 10)
   Sleep(3000)
EndFunc

Func DisOfflineUse32()
   ;ProcessClose("DLPGrant_32.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisOffilneUse.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_32.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 10)
   Sleep(3000)
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

	  FileWrite($hFileOpen, "{" & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"autoSub"' & ":true," & @CRLF)

	  FileWrite($hFileOpen, @TAB & '"autoSel"' & ":true," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"canPrint"' & ":true," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"canReAuth"' & ":true," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"canPrintScn"' & ":true," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"canCopy"' & ":true," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"canOfflineUse"' & ":true," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"canEndTime"' & ":true," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"file_list"' & ":[" & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "{" & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & @TAB & '"file"' & ":" & '"C:\\Users\\Wuhq\\Desktop\\wwwwwwwwww.txt"' & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "}" & @CRLF)
	  FileWrite($hFileOpen, @TAB & "]," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"group_list"' & ":[" & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "{" & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & @TAB & '"groupId"' & ":" & '"3"' & "," & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & @TAB & '"groupName"' & ":" & '"luo"' & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "}," & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "{" & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & @TAB & '"groupId"' & ":" & '"12"' & "," & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & @TAB & '"groupName"' & ":" & '"luo1"' & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "}," & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "{" & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & @TAB & '"groupId"' & ":" & '"13"' & "," & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & @TAB & '"groupName"' & ":" & '"luo2"' & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "}" & @CRLF)
	  FileWrite($hFileOpen, @TAB & "]" & @CRLF)
	  FileWrite($hFileOpen, "}" & @CRLF)

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

Func CreateJsonFile($fJson)
   Local $iFileExists = FileExists($fJson)
   Local $sRandomText = ""
   If $iFileExists Then
	  FileDelete($fJson)
   Else
	  $tBuffer = DllStructCreate("byte[" & StringLen($sText) & "]")
	  DllStructSetData($tBuffer, 1, $sText)
	  $hFile = _WinAPI_CreateFile($fJson, 1)
	  _WinAPI_WriteFile($hFile, $tBuffer, StringLen($sText), $nBytes)
	  _WinAPI_CloseHandle($hFile)

	  Local $hFileOpen = FileOpen($fJson, $FO_OVERWRITE)
	  If $hFileOpen = -1 Then
		 ;MsgBox($MB_SYSTEMMODAL, "", "An error occurred whilst writing the temporary file.")
		 Return False
	  EndIf

	  For $i = 1 To Random(5, 20, 1)
		 $sRandomText &= Chr(Random(65, 122, 1))
	  Next


	  FileWrite($hFileOpen, "{" & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"autoSub"' & ":true," & @CRLF)

	  FileWrite($hFileOpen, @TAB & '"autoSel"' & ":true," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"canPrint"' & ":true," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"canReAuth"' & ":true," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"canPrintScn"' & ":true," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"canCopy"' & ":true," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"canOfflineUse"' & ":true," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"canEndTime"' & ":true," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"file_list"' & ":[" & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "{" & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & @TAB & '"file"' & ":" & '"C:\\Users\\Wuhq\\Desktop\\wwwwwwwwww.txt"' & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "}" & @CRLF)
	  FileWrite($hFileOpen, @TAB & "]," & @CRLF)
	  FileWrite($hFileOpen, @TAB & '"group_list"' & ":[" & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "{" & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & @TAB & '"groupId"' & ":" & '"3"' & "," & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & @TAB & '"groupName"' & ":" & '"luo"' & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "}," & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "{" & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & @TAB & '"groupId"' & ":" & '"12"' & "," & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & @TAB & '"groupName"' & ":" & '"luo1"' & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "}," & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "{" & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & @TAB & '"groupId"' & ":" & '"13"' & "," & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & @TAB & '"groupName"' & ":" & '"luo2"' & @CRLF)
	  FileWrite($hFileOpen, @TAB & @TAB & "}" & @CRLF)
	  FileWrite($hFileOpen, @TAB & "]" & @CRLF)
	  FileWrite($hFileOpen, "}" & @CRLF)
	  FileWrite($hFileOpen, "THE RANDOM TEXT IS :" & @CRLF)
	  FileWrite($hFileOpen, $sRandomText & @CRLF)

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


Func MoveFile($dst)
   Local $dFile = _PathFull(@WorkingDir & "\..\DLP\Result\Auth\" & $dst)
   FileMove($sFile, $dFile, $FC_OVERWRITE + $FC_CREATEPATH)
EndFunc


;适配administrator用户，重新写一遍
Func AllAuth64admin()
   ;ProcessClose("DLPGrant_64.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configAllAuthAdmin.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_64.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 20)
   Sleep(3000)
EndFunc

Func AllDisAuth64admin()
   ;ProcessClose("DLPGrant_64.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configAllDisAuthAdmin.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_64.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 20)
   Sleep(3000)
EndFunc

Func DisPrint64admin()
   ;ProcessClose("DLPGrant_64.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisPrintAdmin.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_64.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 20)
   Sleep(3000)
EndFunc

Func DisReAuth64admin()
   ;ProcessClose("DLPGrant_64.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisReAuthAdmin.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_64.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 20)
   Sleep(3000)
EndFunc

Func DisPrintScn64admin()
   ;ProcessClose("DLPGrant_64.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisPrintScnAdmin.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_64.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 20)
   Sleep(3000)
EndFunc

Func DisCopy64admin()
   ;ProcessClose("DLPGrant_64.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisCopyAdmin.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_64.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 20)
   Sleep(3000)
EndFunc

Func DisOfflineUse64admin()
   ;ProcessClose("DLPGrant_64.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisOfflineUseAdmin.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_64.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 20)
   Sleep(3000)
EndFunc

Func AllAuth32admin()
   ;ProcessClose("DLPGrant_32.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configAllAuthAdmin.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_32.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 20)
   Sleep(3000)
EndFunc

Func AllDisAuth32admin()
   ;ProcessClose("DLPGrant_32.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configAllDisAuth10.95.27.76.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_32.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 20)
   Sleep(3000)
EndFunc

Func DisPrint32admin()
   ;ProcessClose("DLPGrant_32.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisPrintAdmin.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_32.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 20)
   Sleep(3000)
EndFunc

Func DisReAuth32admin()
   ;ProcessClose("DLPGrant_32.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisReAuthAdmin.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_32.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 20)
   Sleep(3000)
EndFunc

Func DisPrintScn32admin()
   ;ProcessClose("DLPGrant_32.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisPrintScnAdmin.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_32.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 20)
   Sleep(3000)
EndFunc

Func DisCopy32admin()
   ;ProcessClose("DLPGrant_32.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisCopyAdmin.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_32.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 20)
   Sleep(3000)
EndFunc

Func DisOfflineUse32admin()
   ;ProcessClose("DLPGrant_32.exe")
   Local $iFile = _PathFull(@WorkingDir & "\..\DLP\AutoTest\configDisOffilneUseAdmin.json")
   Sleep(3000)
   Local $iPID = RunAs($sUserName, @ComputerName, $sPassword, $RUN_LOGON_INHERIT, "C:\Program Files (x86)\360\360Safe\DLp\DLPGrant_32.exe " & $iFile, "", @SW_SHOW)
   WinWait("数据安全", "", 20)
   Sleep(3000)
EndFunc
#cs
Func _StringToUnicodeEncode($str, $sPrefix = '&amp;#x', $sSuffix = ';')
   Local $EncodedString, $i, $s2d, $sS = StringSplit($str, '')
   For $i = 1 To $sS[0]
	  If StringRegExp($sS[$i], '[^\x00-\xff]') Then
		 $EncodedString &amp
	  Else
		 $EncodedString &amp
	  EndIf
   Next
   Return $EncodedString
EndFunc
#ce