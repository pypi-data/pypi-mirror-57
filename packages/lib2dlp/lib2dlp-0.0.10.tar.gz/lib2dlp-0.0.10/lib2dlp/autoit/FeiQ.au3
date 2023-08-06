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
;声明变量
Global $hWnd,$goalfile,$result,$htzqchtz,$count,$isgo
Global $title='飞秋(FeiQ)---局域网即时通讯'
Global $title1='Administrator(KDP-WIN7-PC)'
Global $text = '王宝强，王宝强'
Local $str,$location,$j,$hItem,$start,$end
$search=1002 ;搜索
$friend_tip=1293 ;好友标签
$group_tip=1294 ;群标签
$recent_tip=1295 ;最近通话标签
$bbs_tip=1296 ;论坛标签

;中间窗口相关控件
$friend_view=1193 ;好友
$group_view=1190 ;群
$recent_view=1298 ;最近通话
;~$bbs_view= ;论坛

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
   ;激活客户端窗口
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
   _GUICtrlTreeView_ClickItem($hWnd,$hItem,"left", False,2);点击项目
   sleep(1000)
   ControlFocus($title1,"","RichEdit20W2")
   ControlClick($title1,"","RichEdit20W2")
   Sleep(2000)
   ControlSetText($title1,"", "RichEdit20W2", $text)
   Sleep(2000)
   ;模拟ctrl+enter
   send("{CTRLDOWN}{ENTER}")
   Sleep(100)
   Send("{CTRLUP}")

   Sleep(3000)
   WinClose("[CLASS:#32770]", "")
   Sleep(1000)
   WinSetState($title, "", @SW_MINIMIZE)
EndFunc

#comments-start
ConsoleWrite('TreeView总节点个数：'&_GUICtrlTreeView_GetCount($hWnd)&@CR)
sleep(10)
$str='#0'
$start=TimerInit()    ;计时开始
SearchTree($str)
$end=TimerDiff($start);计时结束
ConsoleWrite('检索时间：'&$end&@CR)
ConsoleWrite('检索结果：'&$result&@CR)
ConsoleWrite('检索节点个数：'&$count&@CR)
#comments-end
;将目标根节点路径拆分
;$location=StringSplit($result,'|')
;获取上级目标节点路径
;for $j=2 to $location[0]-2
   ;ConsoleWrite('目标操作路径数是：'&$location[$j]&@CR)
;   $str=$str&'|'&$location[$j]
;Next
;ConsoleWrite('目标操作路径数：'&$str&@CR)
;Sleep(10)

;获取上级目标节点,右键点击弹出菜单窗口
;ControlTreeView ($title,"",$hWnd,"Select",$str)
;Sleep(10)
;$hItem =_GUICtrlTreeView_GetSelection($hWnd)
;_GUICtrlTreeView_ClickItem($hWnd,$hItem,"left", False,2);点击项目
;sleep(10)
;#cs

;发送按键来实现
;for $i = 1 to 16
   ;sleep(10)
;   send("{DOWN}")
;next
;sleep(10)
;send("{LEFT}")
;sleep(1000)
;send("{ENTER}")
;#ce

;将树节点全部折叠
;_GUICtrlTreeView_Expand($hWnd,'',False)

;获取好友数量
;$frdNum=getOnFrdCount()
;MsgBox(0,'好友数量',$frdNum)
;获取群数量
;$groupNum=getOnGroupCount()
;MsgBox(0,'群数量',$groupNum)
;获取最近通话数量
;$recentNum=getOnRecentCount()
;MsgBox(0,'最近通话数量',$recentNum)
;~ 点击论坛标签
;ControlClick($title,"",$bbs_tip)
;MsgBox(0,'点击论坛标签','论坛...')
;放大缩小窗口
#comments-start
For $i = 3 to 1 Step -1
   WinSetState($title, "", @SW_HIDE)
   WinSetState($title, "", @SW_SHOW)
   WinSetState($title, "", @SW_MINIMIZE)
   WinSetState($title, "", @SW_MAXIMIZE)
   WinSetState($title, "", @SW_RESTORE)
#comments-end
#comments-start
@SW_HIDE = 隐藏窗口
@SW_SHOW = 显示以前隐藏的窗口
@SW_MINIMIZE = 最小化窗口
@SW_MAXIMIZE = 最大化窗口
@SW_RESTORE = 撤销窗口的最小化或最大化状态
@SW_DISABLE = 禁用窗口
@SW_ENABLE = 使窗口可用
#comments-end

;函数
;获得当前好友数量
Func getOnFrdCount()
   ControlClick($title,"",$friend_tip)
   $h=getCtrlHandle($friend_view)
   Return  _GUICtrlTreeView_GetCount($h)
EndFunc

;获得群数量
Func getOnGroupCount()
   ControlClick($title,"",$group_tip)
   $h=getCtrlHandle($group_view)
   Return  _GUICtrlTreeView_GetCount($h)
EndFunc

;获得最近通话数量
Func getOnRecentCount()
   ControlClick($title,"",$recent_tip)
   $h=getCtrlHandle($recent_view)
   Return  _GUICtrlListBox_GetCount($h)
   _GUICtrlTreeView_GetCount
EndFunc

;获取控件句柄
Func getCtrlHandle($control)
   Return ControlGetHandle($title,'',$control)
EndFunc

;TreeView的根结点遍历函数
Func SearchTree($str)
   Local $i,$temp,$str1,$num
   $str1=$str
   $num=ControlTreeView($title,"",$hWnd,"GetItemCount",$str1)
   $count+=$num
   ;#cs只要有匹配结果，立马跳出递归
   If $isgo=False Then
          Return $str1
   EndIf
   ;#ce
   If $num=0 Then

          $temp=ControlTreeView($title,"",$hWnd, "GetText", $str1)
          If StringInStr($temp,$goalfile) Then
                 $isgo=False
                 ConsoleWrite('匹配节点名称：'&$temp&@CR)
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