Local $xps
$xps = "C:\Users\Administrator\Desktop\print.xps"
print()

Func print()

   ;ControlFocus("title","text",controlID)Edit1=Edit instance 1

   ControlFocus("�ļ����Ϊ","","Edit1")

   ; Wait 10 seconds for the Upload window to appear

   WinWait("[CLASS:#32770]","",10)

   ; Set the File name text on the Edit field

   ;ControlSetText("�ļ����Ϊ","", "Edit1", "C:\Users\Administrator\Desktop\print.xps")
   ControlSetText("�ļ����Ϊ","", "Edit1", @DesktopDir & "\print.xps")

   Sleep(1000)

   ; Click on the Open button

   ControlClick("�ļ����Ϊ","","Button1")


   Local $t = ControlFocus("ȷ�����Ϊ","","Button1")

   If $t = 1 Then
	  ControlFocus("ȷ�����Ϊ","","Button1")
	  ControlClick("ȷ�����Ϊ","","Button1")
   Else
	  ControlClick("�ļ����Ϊ","","Button1")
	  ControlFocus("ȷ�����Ϊ","","Button1")
	  ControlClick("ȷ�����Ϊ","","Button1")
	  ControlFocus("���±�","","Button1")
	  ControlClick("���±�","","Button1")
   EndIf



EndFunc
