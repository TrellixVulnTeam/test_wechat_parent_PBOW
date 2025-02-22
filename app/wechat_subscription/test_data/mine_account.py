#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI


# 11位手机号  线上
phone_data = [
    {'username': '18011111115', 'password': '123456789', 'assert': '账号或密码错误'},  # 错误密码  数字  9位
    {'username': '18011111115', 'password': '121212', 'assert': '账号或密码错误'},  # 手机号为空
    {'username': '18011111897', 'password': '123456', 'assert': '该手机号尚未注册，请先至学生端注册'},  # 未注册手机号
    {'username': '19781111111', 'password': '123123', 'assert': '该手机号尚未注册或未注册学生身份'},  # 已注册老师账号
    {'username': '1801111111', 'password': '1111', 'assert': '请输入正确手机号'},
    {'username': '132345', 'password': '123456', 'assert': '请输入正确手机号'},  # 少于11个数字  是否报错
    {'username': '           ', 'password': '123456', 'assert': '请输入正确手机号'},  # 11个空格
    {'username': '18011111115', 'password': '123456', 'assert' : ''},  # 已注册学生账号
    {'username': '180q2.w@S勿x', 'password': '123456', 'assert': '请输入正确手机号'},  # 中文、数字、英文、大写字母、空格、@、'.'字符组合
    {'username': '13502095382', 'password': '123456', 'assert':'该手机号尚未注册或未注册学生身份'},  # 已注册有老师，学生，校长三重身份   # 基础版学生
    # {'username': '18711111134', 'password': '123456'},  # 已注册有老师身份又有学生身份
    # {'username': '18711111237', 'password': '123456'},  # 已注册有老师，学生，校长三重身份   # 基础版学生
    # {'username': '13502095382', 'password': '123456'},  # 已注册有老师身份又有学生身份
    ]

# 6-20位非空字符；只允许设置数字、英文字母（英文字母区分大小写）
pwd_data = [
    {'username': '18011111115', 'password': '123456789', 'assert': '账号或密码错误'},  # 错误密码  数字  9位
    {'username': '18011111115', 'password': '', 'assert': '密码错误'},   # 为空
    {'username': '18011111115', 'password': '     ', 'assert': '密码错误'},   # 5个空格
    # {'username': '18711111235', 'password': 'qweewrdhqasdfg', 'assert': '账号或密码错误'},  # 错误密码 字母  14位
    # {'username': '18711111236', 'password': '123ewr78', 'assert': '账号或密码错误'},  # 数字 字母组合 区分大小写 正确密码为：123eWr78
    {'username': '18011111115', 'password': '3$#3r@#7r', 'assert': '密码错误'},  # 输入特殊字符
    {'username': '18011111115', 'password': '1234', 'assert': '密码错误'},   # 少于6位 数字
    {'username': '18011111115', 'password': 'asd', 'assert': '密码错误'},   # 少于6位 字母
    {'username': '18011111115', 'password': '12as', 'assert': '密码错误'},   # 少于6位 数字、字母组合
    {'username': '18011111115', 'password': '123456342423443213423123', 'assert': '密码错误'},   # 多于20位  数字
    {'username': '18011111115', 'password': 'asrcxsdfsadluipydsyesa', 'assert': '密码错误'},   # 多于20位  字母
    {'username': '18011111115', 'password': '123456sfsfwrzxcsad123sa', 'assert': '密码错误'},   # 多于20位 数、字字母组合
    {'username': '18011111115', 'password': '1115','assert':''},  # 已注册学生账号
    {'username': '', 'password': '', 'assert': '请输入正确手机号', 'assertpwd': '密码错误'},  # 手机号和密码均不输入
    # {'username': '18711111235', 'password': 'qwertyuiopasdfghjklz'},  # 正确密码 字母  20位
    # {'username': '18711111236', 'password': '123eWr78'},  # 正确密码 字母、数字组合 8位
    # {'username': '18711111237', 'password': '123456'},  # 正确密码 数字 6位

    ]

# # 11位手机号  dev
# phone_data = [
#     {'username': '18011111111', 'password': '1111'},  # 未注册手机号
#     {'username': '18011110123', 'password': '123456', 'assert': ''},  #正常登录
#     {'username': '132345', 'password': '123456', 'assert': '请输入正确手机号'},  # 少于11个数字  是否报错
#     {'username': '', 'password': '123456', 'assert': '请输入手机号'},  # 手机号为空
#     {'username': '           ', 'password': '123456', 'assert': '请输入正确手机号'},  # 11个空格
#     {'username': '130你好8world', 'password': '123456', 'assert': '请输入正确手机号'},  # 中文、数字、英文字符组合 -11位
#     {'username': '180q2.w@S勿x', 'password': '123456', 'assert': '请输入正确手机号'},  # 中文、数字、英文、大写字母、空格、@、'.'字符组合

#     # {'username': '187111112345678', 'password': '123456'},  # 15位数字  是否限制大于11位输入
#     {'username': '19781111111', 'password': '123123', 'assert': '该手机号尚未注册或未注册学生身份'},  # 已注册老师账号
#     {'username': '18711111234', 'password': '123456','assert': '该手机号尚未注册，请先至学生端注册'},  # 已注册学生账号
#     {'username': '18011111134', 'password': '123456','assert':''},  # 已注册有老师身份又有学生身份
#     {'username': '18711111237', 'password': '123456','assert':''},  # 已注册有老师，学生，校长三重身份   # 基础版学生
#     ]
#
# # 6-20位非空字符；只允许设置数字、英文字母（英文字母区分大小写）
# pwd_data = [


#     {'username': '18711111234', 'password': '123456789', 'assert': '账号或密码错误'},  # 错误密码  数字  9位
#     {'username': '18011111234', 'password': '', 'assert': '密码错误'},   # 为空
#     {'username': '18011111234', 'password': '     ', 'assert': '密码错误'},   # 5个空格
#     {'username': '18711111235', 'password': 'qweewrdhqasdfg', 'assert': '账号或密码错误'},  # 错误密码 字母  14位
#     {'username': '18711111236', 'password': '123ewr78', 'assert': '账号或密码错误'},  # 数字 字母组合 区分大小写 正确密码为：123eWr78
#     {'username': '18011111234', 'password': '3$#3r@#7r', 'assert': '密码错误'},  # 输入特殊字符
#     {'username': '18011111234', 'password': '1234', 'assert': '密码错误'},   # 少于6位 数字
#     {'username': '18011111234', 'password': 'asd', 'assert': '密码错误'},   # 少于6位 字母
#     {'username': '18011111234', 'password': '12as', 'assert': '密码错误'},   # 少于6位 数字、字母组合
#     {'username': '18711111234', 'password': '123456342423443213423123', 'assert': '密码错误'},   # 多于20位  数字
#     {'username': '18711111234', 'password': 'asrcxsdfsadluipydsyesa', 'assert': '密码错误'},   # 多于20位  字母
#     {'username': '18711111234', 'password': '123456sfsfwrzxcsad123sa', 'assert': '密码错误'},   # 多于20位 数字、字母组合
#     {'username': '', 'password': '', 'assert': '请输入正确手机号', 'assertpwd': '密码错误'},  # 手机号和密码均不输入
#     {'username': '18711111235', 'password': 'qwertyuiopasdfghjklz','assert':''},  # 正确密码 字母  20位
#     {'username': '18711111236', 'password': '123eWr78','assert':''},  # 正确密码 字母、数字组合 8位
#     {'username': '18711111237', 'password': '123456','assert':''},  # 正确密码 数字 6位
#     ]
