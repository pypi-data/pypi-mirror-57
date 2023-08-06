#include <File.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIFiles.au3>
#include <WinAPISys.au3>


ControlFocus("数据安全","","Button7")
WinWait("[CLASS:#32770]","",10)
Sleep(3000)
ControlClick("数据安全","","Button7")