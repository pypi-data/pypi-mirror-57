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
Local $sFile,$iFile
;Local $iFile = _PathFull(@WorkingDir & "\..\DLP\file\" & $sFile)
Local $iSpecialFile = _PathFull(@WorkingDir & "\..\DLP\file\special" & $sFile)
Local $iTamperFile = _PathFull(@WorkingDir & "\..\DLP\file\tamper" & $sFile)
Local $i = 0

If $CmdLine[0] <> 1 Then
   MsgBox("","error","缺少参数")
   Exit
Else
   Switch @OSVersion
	  Case $winxp

	  Case $win7
		 If @IPAddress1 == '10.95.41.17' And @IPAddress1 <> '0.0.0.0' Then
			Sleep(3000)
			UploadWin7($CmdLine[1])
		 ElseIf @IPAddress1 == '10.95.41.20' And @IPAddress1 <> '0.0.0.0' Then
			Sleep(3000)
			UploadWin7($CmdLine[1])
		 ElseIf @IPAddress1 == '10.95.27.75' And @IPAddress1 <> '0.0.0.0' Then
			Sleep(3000)
			UploadWin7($CmdLine[1])
		 ElseIf @IPAddress1 == '10.95.27.83' And @IPAddress1 <> '0.0.0.0' Then
			Sleep(3000)
			UploadWin7($CmdLine[1])
		 Else
			Exit
		 EndIf
	  Case $win8
		 If @IPAddress1 == '10.95.27.79' And @IPAddress1 <> '0.0.0.0' Then
			Sleep(3000)
			UploadWin81($CmdLine[1])
		 ElseIf @IPAddress1 == '10.95.27.80' And @IPAddress1 <> '0.0.0.0' Then
			Sleep(3000)
			UploadWin81($CmdLine[1])
		 Else
			Exit
		 EndIf
	  Case $win81
		 If @IPAddress1 == '10.95.27.76' And @IPAddress1 <> '0.0.0.0'  Then
			Sleep(3000)
			UploadWin81($CmdLine[1])
		 ElseIf @IPAddress1 == '10.95.27.77' And @IPAddress1 <> '0.0.0.0'  Then
			Sleep(3000)
			UploadWin81($CmdLine[1])
		 Else
			Exit
		 EndIf
	  Case $win10
		 If @IPAddress1 == '10.95.27.116' And @IPAddress1 <> '0.0.0.0'  Then
			Sleep(3000)
			Upload($CmdLine[1])
		 ElseIf @IPAddress1 == '10.95.27.74' And @IPAddress1 <> '0.0.0.0'  Then
			Sleep(3000)
			Upload($CmdLine[1])
		 ElseIf @IPAddress1 == '172.24.83.62' And @IPAddress1 <> '0.0.0.0'  Then
			Sleep(3000)
			Upload($CmdLine[1])
		 Else
			Exit
		 EndIf
   EndSwitch
EndIf

Func UploadWin81($flag)
   Switch $flag
	  Case 1;测试OCR识别
		 $sFile = '我是tupian.jpg'
		 NetShareWin81($iFile,$sFile)
	  Case 2;测试文件内容包含关键字
		 $sFile = 'dlp.doc'
		 NetShareWin81($iFile,$sFile)
	  Case 3;测试受限文件
		 $sFile = 'shouxian.docx'
		 NetShareWin81($iFile,$sFile)
	  Case 4;测试文件名+文件内容的PDF文件
		 $sFile = 'tupian.pdf'
		 NetShareWin81($iFile,$sFile)
	  Case 5;使用共享方式测试上传证据文件
		 $sFile = 'src.txt'
		 NetShareWin81($iFile,$sFile)
	  Case 6;使用共享方式测试嵌套文件
		 $sFile = '5层嵌套zip.zip'
		 NetShareWin81($iFile,$sFile)
	  Case 7;使用共享方式测试嵌套文件
		 $sFile = '10层嵌套.pptx'
		 NetShareWin81($iFile,$sFile)
	  Case 8;使用共享方式测试备注、脚注、批注、页眉、页脚、正文文件
		 ;$sFile = '10层嵌套.pptx'
		 NetShareDirWin81($iSpecialFile,$sFile)
	  Case 9;使用共享方式测试篡改后缀名的文件
		 ;$sFile = '10层嵌套.pptx'
		 NetShareDirWin81($iTamperFile,$sFile)
   EndSwitch
EndFunc

Func Upload($flag)
   Switch $flag
	  Case 1;测试OCR识别
		 $sFile = '我是tupian.jpg'
		 NetShare($iFile,$sFile)
	  Case 2;测试文件内容包含关键字
		 $sFile = 'dlp.doc'
		 NetShare($iFile,$sFile)
	  Case 3;测试受限文件
		 $sFile = '受限文件.docx'
		 NetShare($iFile,$sFile)
	  Case 4;测试文件名+文件内容的PDF文件
		 $sFile = '王宝强4页.pdf'
		 NetShare($iFile,$sFile)
	  Case 5;使用共享方式测试上传证据文件
		 $sFile = 'src.txt'
		 NetShare($iFile,$sFile)
	  Case 6;使用共享方式测试嵌套文件
		 $sFile = '5层嵌套zip.zip'
		 NetShare($iFile,$sFile)
	  Case 7;使用共享方式测试嵌套文件
		 $sFile = '10层嵌套.pptx'
		 NetShare($iFile,$sFile)
	  Case 8;使用共享方式测试备注、脚注、批注、页眉、页脚、正文文件
		 ;$sFile = '10层嵌套.pptx'
		 NetShareDir($iSpecialFile,$sFile)
	  Case 9;使用共享方式测试篡改后缀名的文件
		 ;$sFile = '10层嵌套.pptx'
		 NetShareDir($iTamperFile,$sFile)
   EndSwitch
EndFunc

Func UploadWin7($flag)
   Switch $flag
	  Case 1;测试OCR识别
		 $sFile = '我是tupian.jpg'
		 NetShareWin7($iFile,$sFile)
	  Case 2;测试文件内容包含关键字
		 $sFile = 'dlp.doc'
		 NetShareWin7($iFile,$sFile)
	  Case 3;测试受限文件
		 $sFile = '受限文件.docx'
		 NetShareWin7($iFile,$sFile)
	  Case 4;测试文件名+文件内容的PDF文件
		 $sFile = '王宝强4页.pdf'
		 NetShareWin7($iFile,$sFile)
	  Case 5;使用共享方式测试上传证据文件
		 $sFile = 'src.txt'
		 NetShareWin7($iFile,$sFile)
	  Case 6;使用共享方式测试嵌套文件
		 $sFile = '5层嵌套zip.zip'
		 NetShareWin7($iFile,$sFile)
	  Case 7;使用共享方式测试嵌套文件
		 $sFile = '10层嵌套.pptx'
		 NetShareWin7($iFile,$sFile)
	  Case 8;使用共享方式测试备注、脚注、批注、页眉、页脚、正文文件
		 ;$sFile = '10层嵌套.pptx'
		 NetShareDirWin7($iSpecialFile,$sFile)
	  Case 9;使用共享方式测试篡改后缀名的文件
		 ;$sFile = '10层嵌套.pptx'
		 NetShareDirWin7($iTamperFile,$sFile)
   EndSwitch
EndFunc

Func NetShareWin81($iFile,$sFile)
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test")
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test", $DMA_DEFAULT, "administrator", "1")

   $iFile = _PathFull(@WorkingDir & "\..\DLP\file\" & $sFile)
   ;Local $aArray = DriveGetDrive($DT_NETWORK)
   Local $iFileExists = FileExists($iFile)


   If Not @error And $iFileExists = 1 Then
	  FileCopy($iFile, "Z:\", $FC_OVERWRITE + $FC_CREATEPATH)
	  DriveMapDel("Z:")
	  Return True
   Else
	  DriveMapDel("Z:")
	  Exit
	  Return False
   EndIf

   ;DriveMapDel("Z:")
EndFunc

Func NetShare($iFile,$sFile)
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test")
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test", $DMA_DEFAULT, ".\administrator", "1")

   $iFile = _PathFull(@WorkingDir & "\..\DLP\file\" & $sFile)
   ;Local $aArray = DriveGetDrive($DT_NETWORK)
   Local $iFileExists = FileExists($iFile)


   If Not @error And $iFileExists = 1 Then
	  FileCopy($iFile, "Z:\", $FC_OVERWRITE + $FC_CREATEPATH)
	  DriveMapDel("Z:")
	  Return True
   Else
	  DriveMapDel("Z:")
	  Exit
	  Return False
   EndIf

   ;DriveMapDel("Z:")
EndFunc

Func NetShareDirWin81($iFile,$sFile)
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test")
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test", $DMA_DEFAULT, "administrator", "1")

   ;$iFile = _PathFull(@WorkingDir & "\..\DLP\file\" & $sFile)
   ;Local $aArray = DriveGetDrive($DT_NETWORK)
   Local $iFileExists = FileExists($iFile)


   If Not @error And $iFileExists = 1 Then
	  FileCopy($iFile, "Z:\", $FC_OVERWRITE + $FC_CREATEPATH)
	  DriveMapDel("Z:")
	  Return True
   Else
	  DriveMapDel("Z:")
	  Exit
	  Return False
   EndIf

   ;DriveMapDel("Z:")
EndFunc

Func NetShareDir($iFile,$sFile)
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test")
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test", $DMA_DEFAULT, ".\administrator", "1")

   ;$iFile = _PathFull(@WorkingDir & "\..\DLP\file\" & $sFile)
   ;Local $aArray = DriveGetDrive($DT_NETWORK)
   Local $iFileExists = FileExists($iFile)


   If Not @error And $iFileExists = 1 Then
	  FileCopy($iFile, "Z:\", $FC_OVERWRITE + $FC_CREATEPATH)
	  DriveMapDel("Z:")
	  Return True
   Else
	  DriveMapDel("Z:")
	  Exit
	  Return False
   EndIf

   ;DriveMapDel("Z:")
EndFunc

Func NetShareWin7($iFile,$sFile)
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test")
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test", $DMA_DEFAULT, ".\administrator", "1")

   $iFile = _PathFull(@WorkingDir & "\..\DLP\file\" & $sFile)
   ;Local $aArray = DriveGetDrive($DT_NETWORK)
   Local $iFileExists = FileExists($iFile)


   If Not @error And $iFileExists = 1 Then
	  FileCopy($iFile, "Z:\", $FC_OVERWRITE + $FC_CREATEPATH)
	  ;DriveMapDel("Z:")
	  Return True
   Else
	  ;DriveMapDel("Z:")
	  Exit
	  Return False
   EndIf

   ;DriveMapDel("Z:")
EndFunc

Func NetShareDirWin7($iFile,$sFile)
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test")
   DriveMapAdd("Z:", "\\10.95.27.99\wuhq\Test", $DMA_DEFAULT, ".\administrator", "1")

   ;$iFile = _PathFull(@WorkingDir & "\..\DLP\file\" & $sFile)
   ;Local $aArray = DriveGetDrive($DT_NETWORK)
   Local $iFileExists = FileExists($iFile)


   If Not @error And $iFileExists = 1 Then
	  FileCopy($iFile, "Z:\", $FC_OVERWRITE + $FC_CREATEPATH)
	  ;DriveMapDel("Z:")
	  Return True
   Else
	  ;DriveMapDel("Z:")
	  Exit
	  Return False
   EndIf

   ;DriveMapDel("Z:")
EndFunc