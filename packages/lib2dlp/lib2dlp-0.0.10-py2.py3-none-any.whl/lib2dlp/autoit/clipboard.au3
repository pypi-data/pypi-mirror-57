#include <Clipboard.au3>
#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>

Global $g_idMemo

clipboard()

Func clipboard()

    $g_idMemo = GUICtrlCreateEdit("", 2, 2, 596, 396, $WS_VSCROLL)
	_ClipBoard_Empty()
    _ClipBoard_SetData("王宝强|wangbaoqiang------------------------王宝强|wangbaoqiang------------------------王宝强|wangbaoqiang------------------------")
    MemoWrite(_ClipBoard_GetData())


EndFunc

Func MemoWrite($sMessage = "")
    GUICtrlSetData($g_idMemo, $sMessage & @CRLF, 1)
EndFunc