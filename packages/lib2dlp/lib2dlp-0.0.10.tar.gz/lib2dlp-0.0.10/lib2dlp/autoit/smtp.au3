#include <Inet.au3>
#include <MsgBoxConstants.au3>

Local $s_SmtpServer = "10.95.41.18"
Local $s_FromName = "My Name"
Local $s_FromAddress = "dlptest1@dlp.cn"
Local $s_ToAddress = "dlptest2@dlp.cn"
Local $s_Subject = "My Test UDF"
;Local $as_Body[2]
;$as_Body[0] = "Testing the new email udf"
;$as_Body[1] = "Second Line"
Local $iResponse = _INetSmtpMail($s_SmtpServer, $s_FromName, $s_FromAddress, $s_ToAddress, $s_Subject, $as_Body)
Local $iErr = @error
If $iResponse = 1 Then
    MsgBox($MB_SYSTEMMODAL, "Success!", "Mail sent")
Else
    MsgBox($MB_SYSTEMMODAL, "Error!", "Mail failed with error code " & $iErr)
EndIf
