#!/usr/bin/env pytho      # -*- coding: utf-8 -*-
# 登录用户名密码,密码判断三次,密码是否为数字

import time

def name_panduan():
    user_name = input('请输入用户名:')
    if user_name == true_name:
        pass_panduan()
    else:
        print('用户名错误！')
        name_panduan()

def pass_panduan():
    global i,j
    while True:
        user_pass = int(input('请输入密码(只能为数字):'))
        if user_pass != true_pass:
            print('密码输入错误！')
            i += 1
            if i == 3:
                print('三次密码错误，三秒内不可再次输入！')
                i = 0
                for _ in range(3):
                    print(j)
                    j -= 1
                    time.sleep(1)
                j = 3
            pass_panduan()
        else:
            print('登录成功！')
            exit()

i = 0
j = 3
true_name = 'admin'
true_pass = 123456
name_panduan()
pass_panduan()