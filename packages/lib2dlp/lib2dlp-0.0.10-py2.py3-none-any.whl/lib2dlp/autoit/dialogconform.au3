Local $xps
$xps = "C:\Users\Administrator\Desktop\print.xps"
print()

Func print()

   ;ControlFocus("title","text",controlID)Edit1=Edit instance 1

   ControlFocus("文件另存为","","Edit1")

   ; Wait 10 seconds for the Upload window to appear

   WinWait("[CLASS:#32770]","",10)

   ; Set the File name text on the Edit field

   ;ControlSetText("文件另存为","", "Edit1", "C:\Users\Administrator\Desktop\print.xps")
   ControlSetText("文件另存为","", "Edit1", @DesktopDir & "\print.xps")

   Sleep(1000)

   ; Click on the Open button

   ControlClick("文件另存为","","Button1")


   Local $t = ControlFocus("确认另存为","","Button1")

   If $t = 1 Then
	  ControlFocus("确认另存为","","Button1")
	  ControlClick("确认另存为","","Button1")
   Else
	  ControlClick("文件另存为","","Button1")
	  ControlFocus("确认另存为","","Button1")
	  ControlClick("确认另存为","","Button1")
	  ControlFocus("记事本","","Button1")
	  ControlClick("记事本","","Button1")
   EndIf



EndFunc
