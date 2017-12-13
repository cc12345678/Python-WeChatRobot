"""
微信辅助函数
"""
import itchat


def wx_getuserinfo(userinfo):
    """
    搜索用户
    :param userinfo: 用户名、昵称或备注
    :return:
    """
    # 缩写替代
    if userinfo == "wxb":
        userinfo = "王小白"

    # 根据用户名搜索
    _users = itchat.search_friends(nickName=userinfo)
    if len(_users) > 0:
        return _users[0]
    else:
        # 根据用户备注搜索
        _users = itchat.search_friends(remarkName=userinfo)
        if len(_users) > 0:
            return _users[0]
        else:
            # 根据用户账号搜索
            _users = itchat.search_friends(wechatAccount=userinfo)
            if len(_users) > 0:
                return _users[0]
            else:
                # 根据用户ID搜索
                _user = itchat.search_friends(userName=userinfo)
                if _user:
                    return _user
                else:
                    print("没有找到用户")
                    return None


def wx_sendmsg(userinfo, msg):
    """
    根据用户信息发送消息
    :param userinfo:用户名、昵称或备注
    :param msg:发送信息
    :return:
    """
    # 获取用户信息
    _user = wx_getuserinfo(userinfo)
    # 判断用户是否有效
    if _user:
        itchat.send_msg(msg, toUserName=_user["UserName"])
        print("消息发送完毕")


def wx_statafriends():
    """
    统计好友信息
    :return:
    """
    # 获取好友信息
    _friends = itchat.get_friends()

    # 统计好友数
    _stata_num = len(_friends)

    # 返回统计结果
    return dict(num=_stata_num,
                example=_friends[0])
