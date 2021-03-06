"""
全局变量及其管理函数
"""
import pickle
import os


# 全局变量 - 是否自动回复
IsAutoReply = False

# 全局变量 - 是否转发
IsTransfer = False

# 全局变量 - 标记是否停止
IsStop = False

# 最近一次发信息的好友信息
LatestMsgUserInfo = None

# 保存文件路径
__File_Path = "config/set.dat"


def load_vars():
    """
    从本地加载变量
    :return:
    """
    # 声明全局变量
    global IsAutoReply
    global IsTransfer
    global __File_Path

    # 读取数据
    if os.path.exists(__File_Path):
        _file = open(__File_Path, "rb")
        _savedict = pickle.load(_file)
    else:
        _savedict = dict(IsAutoReply=False, IsTransfer=False)

    # 变量赋值
    try:
        IsAutoReply = _savedict["IsAutoReply"]
    except KeyError:
        IsAutoReply = False

    try:
        IsTransfer = _savedict["IsTransfer"]
    except KeyError:
        IsTransfer = False


def save_vars():
    """
    变量保存到本地
    :return:
    """
    # 声明全局变量
    global IsAutoReply
    global IsTransfer
    global __File_Path

    # 形成保存字典
    _savedict = dict(IsAutoReply=IsAutoReply, IsTransfer=IsTransfer)

    # 保存数据
    _file = open(__File_Path, "wb")
    pickle.dump(_savedict, _file)


def print_vars():
    """
    打印变量状态
    :return:
    """
    # 声明全局变量
    global IsStop
    global IsAutoReply
    global IsTransfer
    # 打印
    print("全局参数如下：\nIsStop=%s\nIsAutoReply=%s\nIsTransfer=%s" % (IsStop, IsAutoReply, IsTransfer))
