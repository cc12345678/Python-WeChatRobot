import itchat
from itchat.content import *
import threading
import re
import myvars
import mywxfuncs


@itchat.msg_register(TEXT, isFriendChat=True)
def reply_text(msg):
    # 获取发件人信息
    _user_sender = mywxfuncs.wx_getuserinfo(msg["FromUserName"])
    # 获取转发人信息
    _user_mm = mywxfuncs.wx_getuserinfo("王小白")
    # 获取主人信息
    _user_yy = mywxfuncs.wx_getuserinfo("NERO-You")

    # 记录最近发信人
    myvars.LatestMsgUserInfo = _user_sender

    # 本地打印
    print("收到信息：%s 【发信人：%s】" % (msg["Text"], _user_sender["NickName"]))

    # 转发消息
    if myvars.IsTransfer:
        if (_user_sender["UserName"] != _user_mm["UserName"]) and (_user_sender["UserName"] != _user_yy["UserName"]):
            # 信息内容
            _send_msg_content = msg["Text"]
            _send_msg_name = _user_sender["NickName"]
            _send_msg_sex = _user_sender["Sex"] == 1 and "男" or "女"
            _send_msg = "注意！大由由收到一条信息：\n%s。\n发信人：%s。性别：%s" % (_send_msg_content, _send_msg_name, _send_msg_sex)
            _send_username = _user_mm["UserName"]
            # 消息转发
            itchat.send_msg(_send_msg, toUserName=_send_username)

    # 回复消息
    if myvars.IsAutoReply:
        # 自动回复
        return _user_sender["NickName"] + "您好，我是WeChatRobot！主人现在不在，稍后与您联系。"


def run_itchat():
    """
    运行微信
    :return:
    """
    itchat.run()


def handle_cmd(cmd):
    """
    处理指令
    :param cmd: 输入的指令
    :return:
    """
    # 单目指令
    # 退出功能
    if cmd in ("quit", "q"):
        myvars.IsStop = True
    # 设置自动回复
    elif cmd in ("sr", "sr true"):
        myvars.IsAutoReply = True
        myvars.save_vars()
        myvars.print_vars()
    # 取消自动回复
    elif cmd in ("cr", "sr false"):
        myvars.IsAutoReply = False
        myvars.save_vars()
        myvars.print_vars()
    # 设置转发
    elif cmd in ("st", "st true"):
        myvars.IsTransfer = True
        myvars.save_vars()
        myvars.print_vars()
    # 取消转发
    elif cmd in ("cr", "st false"):
        myvars.IsTransfer = False
        myvars.save_vars()
        myvars.print_vars()
    # 显示设置数据
    elif cmd in ("showsetdata", "ssd"):
        myvars.print_vars()
    # 显示好友统计信息
    elif cmd in ("showfriendstata", "sfs"):
        print(mywxfuncs.wx_statafriends())

    # 多目指令
    _cmds = re.split("\s+", cmd)

    # 双目
    if len(_cmds) == 2:
        # 搜索并显示用户信息
        if _cmds[0] in ("user", "searchuser"):
            _user = mywxfuncs.wx_getuserinfo(_cmds[1])
            if _user:
                print(_user)
        # 向最近一次来信用户发送消息
        elif _cmds[0] in ("m", "msg", "sendmsg"):
            if myvars.LatestMsgUserInfo:
                print("正在发送信息至%s……" % myvars.LatestMsgUserInfo["NickName"])
                mywxfuncs.wx_sendmsg(msg=_cmds[1], userdata=myvars.LatestMsgUserInfo)

    # 三目
    if len(_cmds) == 3:
        # 根据用户名发送消息
        if _cmds[0] in ("m", "msg", "sendmsg"):
            print("正在发送信息至指定用户……")
            mywxfuncs.wx_sendmsg(msg=_cmds[2], usermark=_cmds[1])


if __name__ == "__main__":
    # 加载全局变量
    myvars.load_vars()

    # 登录微信
    itchat.auto_login(hotReload=True)

    # 后台运行微信
    trd = threading.Thread(target=run_itchat, args=())
    trd.setDaemon(True)
    trd.start()

    # 运行指令输入及解析
    while not myvars.IsStop:
        handle_cmd(cmd=input("输入指令："))

    # 提示结束
    print("程序运行结束。")




