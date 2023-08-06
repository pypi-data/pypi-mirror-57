#include <GUITreeView.au3>
#include <GUIListBox.au3>
#include <WinAPI.au3>
#include <GuiButton.au3>

Local const $winxp = 'WIN_XP'
Local const $win7 = 'WIN_7'
Local const $win8 = 'WIN_8'
Local const $win81 = 'WIN_81'
Local const $win10 = 'WIN_10'
Local const $kdp_win7_PC = 'KDP-WIN7-PC'
;��������
Global $hWnd,$goalfile,$result,$htzqchtz,$count,$isgo
Global $title='����(FeiQ)---��������ʱͨѶ'
Global $title1='Administrator(KDP-WIN7-PC)'
Global $text = '����ǿ������ǿ'
Local $str,$location,$j,$hItem,$start,$end
$search=1002 ;����
$friend_tip=1293 ;���ѱ�ǩ
$group_tip=1294 ;Ⱥ��ǩ
$recent_tip=1295 ;���ͨ����ǩ
$bbs_tip=1296 ;��̳��ǩ

;�м䴰����ؿؼ�
$friend_view=1193 ;����
$group_view=1190 ;Ⱥ
$recent_view=1298 ;���ͨ��
;~$bbs_view= ;��̳

Switch @OSVersion
   Case $winxp

   Case $win7
	  If @ComputerName == $kdp_win7_PC Then
		 SendMsg()
	  Else
		 Exit
	  EndIf
   Case $win8

   Case $win81

   Case $win10

EndSwitch

Func SendMsg()
   ;����ͻ��˴���
   WinActivate($title)
   Sleep(1000)

   $hWnd=ControlGetHandle($title,"","SysTreeView321")
   _GUICtrlTreeView_Expand($hWnd)
   ControlTreeView($title,"",$hWnd,"Expand","#1")
   Sleep(1000)
   ;$textcontent = ControlTreeView($title,"",$hWnd,"GetText","#2")
   ;MsgBox(0,'',$textcontent)
   ControlTreeView($title,"",$hWnd,"Select","#2")
   $hItem =_GUICtrlTreeView_GetSelection($hWnd)
   sleep(1000)
   _GUICtrlTreeView_ClickItem($hWnd,$hItem,"left", False,2);�����Ŀ
   sleep(1000)
   ControlFocus($title1,"","RichEdit20W2")
   ControlClick($title1,"","RichEdit20W2")
   Sleep(2000)
   ControlSetText($title1,"", "RichEdit20W2", $text)
   Sleep(2000)
   ;ģ��ctrl+enter
   send("{CTRLDOWN}{ENTER}")
   Sleep(100)
   Send("{CTRLUP}")

   Sleep(3000)
   WinClose("[CLASS:#32770]", "")
   Sleep(1000)
   WinSetState($title, "", @SW_MINIMIZE)
EndFunc

#comments-start
ConsoleWrite('TreeView�ܽڵ������'&_GUICtrlTreeView_GetCount($hWnd)&@CR)
sleep(10)
$str='#0'
$start=TimerInit()    ;��ʱ��ʼ
SearchTree($str)
$end=TimerDiff($start);��ʱ����
ConsoleWrite('����ʱ�䣺'&$end&@CR)
ConsoleWrite('���������'&$result&@CR)
ConsoleWrite('�����ڵ������'&$count&@CR)
#comments-end
;��Ŀ����ڵ�·�����
;$location=StringSplit($result,'|')
;��ȡ�ϼ�Ŀ��ڵ�·��
;for $j=2 to $location[0]-2
   ;ConsoleWrite('Ŀ�����·�����ǣ�'&$location[$j]&@CR)
;   $str=$str&'|'&$location[$j]
;Next
;ConsoleWrite('Ŀ�����·������'&$str&@CR)
;Sleep(10)

;��ȡ�ϼ�Ŀ��ڵ�,�Ҽ���������˵�����
;ControlTreeView ($title,"",$hWnd,"Select",$str)
;Sleep(10)
;$hItem =_GUICtrlTreeView_GetSelection($hWnd)
;_GUICtrlTreeView_ClickItem($hWnd,$hItem,"left", False,2);�����Ŀ
;sleep(10)
;#cs

;���Ͱ�����ʵ��
;for $i = 1 to 16
   ;sleep(10)
;   send("{DOWN}")
;next
;sleep(10)
;send("{LEFT}")
;sleep(1000)
;send("{ENTER}")
;#ce

;�����ڵ�ȫ���۵�
;_GUICtrlTreeView_Expand($hWnd,'',False)

;��ȡ��������
;$frdNum=getOnFrdCount()
;MsgBox(0,'��������',$frdNum)
;��ȡȺ����
;$groupNum=getOnGroupCount()
;MsgBox(0,'Ⱥ����',$groupNum)
;��ȡ���ͨ������
;$recentNum=getOnRecentCount()
;MsgBox(0,'���ͨ������',$recentNum)
;~ �����̳��ǩ
;ControlClick($title,"",$bbs_tip)
;MsgBox(0,'�����̳��ǩ','��̳...')
;�Ŵ���С����
#comments-start
For $i = 3 to 1 Step -1
   WinSetState($title, "", @SW_HIDE)
   WinSetState($title, "", @SW_SHOW)
   WinSetState($title, "", @SW_MINIMIZE)
   WinSetState($title, "", @SW_MAXIMIZE)
   WinSetState($title, "", @SW_RESTORE)
#comments-end
#comments-start
@SW_HIDE = ���ش���
@SW_SHOW = ��ʾ��ǰ���صĴ���
@SW_MINIMIZE = ��С������
@SW_MAXIMIZE = ��󻯴���
@SW_RESTORE = �������ڵ���С�������״̬
@SW_DISABLE = ���ô���
@SW_ENABLE = ʹ���ڿ���
#comments-end

;����
;��õ�ǰ��������
Func getOnFrdCount()
   ControlClick($title,"",$friend_tip)
   $h=getCtrlHandle($friend_view)
   Return  _GUICtrlTreeView_GetCount($h)
EndFunc

;���Ⱥ����
Func getOnGroupCount()
   ControlClick($title,"",$group_tip)
   $h=getCtrlHandle($group_view)
   Return  _GUICtrlTreeView_GetCount($h)
EndFunc

;������ͨ������
Func getOnRecentCount()
   ControlClick($title,"",$recent_tip)
   $h=getCtrlHandle($recent_view)
   Return  _GUICtrlListBox_GetCount($h)
   _GUICtrlTreeView_GetCount
EndFunc

;��ȡ�ؼ����
Func getCtrlHandle($control)
   Return ControlGetHandle($title,'',$control)
EndFunc

;TreeView�ĸ�����������
Func SearchTree($str)
   Local $i,$temp,$str1,$num
   $str1=$str
   $num=ControlTreeView($title,"",$hWnd,"GetItemCount",$str1)
   $count+=$num
   ;#csֻҪ��ƥ���������������ݹ�
   If $isgo=False Then
          Return $str1
   EndIf
   ;#ce
   If $num=0 Then

          $temp=ControlTreeView($title,"",$hWnd, "GetText", $str1)
          If StringInStr($temp,$goalfile) Then
                 $isgo=False
                 ConsoleWrite('ƥ��ڵ����ƣ�'&$temp&@CR)
                 $result=$str1
          EndIf
   Else
          For $i=0 to $num-1
                 SearchTree($str1&StringFormat('|#%d',$i))
          Next
   EndIf

#cs
   If $isgo=False Then
          Return $str1
   EndIf
#ce
EndFunc