#include <File.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIFiles.au3>
#include <WinAPISys.au3>


ControlFocus("���ݰ�ȫ","","Button7")
WinWait("[CLASS:#32770]","",10)
Sleep(3000)
ControlClick("���ݰ�ȫ","","Button7")