"""
微信辅助函数
"""
import itchat


# 搜索用户
def wx_getuserinfo(userinfo):
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


# 根据用户信息发送消息
def wx_sendmsg(userinfo, msg):
    # 获取用户信息
    _user = wx_getuserinfo(userinfo)
    # 判断用户是否有效
    if _user:
        itchat.send_msg(msg, toUserName=_user["UserName"])
        print("消息发送完毕")


