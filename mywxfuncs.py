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


def wx_sendmsg(msg, userdata=None, usermark=None):
    """
    根据用户信息发送消息
    :param msg:发送信息
    :param userdata:用户数据类
    :param usermark:用户名、昵称或备注
    :return:
    """
    # 直接获取用户信息
    if userdata:
        _user = userdata
    # 读取用户信息
    elif usermark:
        _user = wx_getuserinfo(usermark)

    # 判断用户是否有效
    if _user:
        itchat.send_msg(msg, toUserName=_user["UserName"])
        print("消息发送完毕")
    else:
        print("用户不存在")


def wx_statafriends():
    """
    统计好友信息
    :return:
    """
    # 获取好友信息
    _friends = itchat.get_friends(update=True)

    # 统计好友数
    _stata_num = len(_friends)

    # 统计好友其他信息
    _stata_malenum = 0
    _stata_femalenum = 0
    _stata_provinces = dict()
    for _friend in _friends:
        # 性别统计
        if _friend["Sex"] == 1:
            _stata_malenum += 1
        else:
            _stata_femalenum += 1
        # 地区统计
        _province = _friend["Province"]
        if _province in _stata_provinces.keys():
            _stata_provinces[_province] += 1
        else:
            _stata_provinces[_province] = 1

    # print(_friends[1])
    # 返回统计结果
    return {"Num_All": _stata_num,
            "Num_Male": _stata_malenum,
            "Num_Female": _stata_femalenum,
            "Stata_Provincce": _stata_provinces}
