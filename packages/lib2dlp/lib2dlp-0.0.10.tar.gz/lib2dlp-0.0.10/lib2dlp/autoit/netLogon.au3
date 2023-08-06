#include <AutoItConstants.au3>
#include <MsgBoxConstants.au3>
#include <FileConstants.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIFiles.au3>
#include <File.au3>
#include <WinAPISys.au3>
#include <Process.au3>

Local const $winxp = 'WIN_XP'
Local const $win7 = 'WIN_7'
Local const $win8 = 'WIN_8'
Local const $win81 = 'WIN_81'
Local const $win10 = 'WIN_10'
Local const $wuhq = '3PFTVS4-WUHQ'
Local const $kdp_win7_PC = 'KDP-WIN7-PC'
Local const $dlp_pc_test_dlp = 'DLP-PC-TEST-DLP'
Local const $DESKTOP_3QMBU5Q = 'DESKTOP-3QMBU5Q'
Local Const $EDLP_win832 = 'EDLP_WIN832'
Local Const $win864 = 'WIN864'
Local Const $win732 = 'DLP4-WIN732-PC'
Local Const $win1032 = 'DESKTOP-NQ06HQU'

Switch @OSVersion
   Case $winxp

   Case $win7
	  If @IPAddress1 == '10.95.41.17' And @IPAddress1 <> '0.0.0.0' Then
		 Logon81()
	  ElseIf @IPAddress1 == '10.95.41.20' And @IPAddress1 <> '0.0.0.0' Then
		 Logon81()
	  ElseIf @IPAddress1 == '10.95.27.75' And @IPAddress1 <> '0.0.0.0' Then
		 Logon81()
	  ElseIf @IPAddress1 == '10.95.27.83' And @IPAddress1 <> '0.0.0.0' Then
		 Logon81()
	  EndIf
   Case $win8
	  If @IPAddress1 == '10.95.27.79' And @IPAddress1 <> '0.0.0.0' Then
		 Logon81()
	  ElseIf @IPAddress1 == '10.95.27.80' And @IPAddress1 <> '0.0.0.0' Then
		 Logon81()
	  EndIf
   Case $win81
	  If @IPAddress1 == '10.95.27.76' And @IPAddress1 <> '0.0.0.0'  Then
		 Logon81()
	  ElseIf @IPAddress1 == '10.95.27.77' And @IPAddress1 <> '0.0.0.0'  Then
		 Logon81()
	  EndIf
   Case $win10
	  If @IPAddress1 == '10.95.27.116' And @IPAddress1 <> '0.0.0.0'  Then
		 Logon81()
	  ElseIf @IPAddress1 == '10.95.27.74' And @IPAddress1 <> '0.0.0.0'  Then
		 Logon81()
	  ElseIf @IPAddress1 == '172.24.83.62' And @IPAddress1 <> '0.0.0.0'  Then
		 Logon81()
	  EndIf
EndSwitch

Func Logon81()
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test")
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test", $DMA_DEFAULT, "administrator", "1")
EndFunc

Func Logon()
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test")
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test", $DMA_DEFAULT, ".\administrator", "1")
EndFunc