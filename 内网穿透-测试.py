# -*- coding: UTF-8 -*-
# Version: v1.4
# Created by lstcml on 2022/10/18
# 建议定时10分钟：*/10 * * * *

'''
cron: */10 * * * *
new Env('Cpolar内网穿透');
'''

'''
使用说明：
1、打开https://i.cpolar.com/m/4nX8注册登录后获取authtoken；
2、新增变量qlnwct_authtoken，值为你账户的authtoken，运行脚本

更新记录：
v1.4
1、兼容新版的青龙面板；

v1.3
1、移动仓库目录；

v1.2
1、新增CPU架构识别，自动下载对应cpolar程序；
2、默认开启自动更新，qlnwctupdate值为false则关闭自动更新；

v1.1
1、开放推送，仅支持PushPlus推送，每次触发启动穿透会推送一次地址；
'''

import os
import re
import sys
import json
import requests
from time import sleep
path = os.path.split(os.path.realpath(__file__))[0]
log_path = os.path.join(path, "nwct_cpolar_log")
log_name = os.path.join(log_path, "cpolar")
log_file = os.path.join(log_path, "cpolar.master.log") 
app_path = os.path.join(path, "cpolar")
commond = "python3 " + os.path.join(path, "cpolar.py") + " &"

# 检查更新
def update():
    print("当前运行的脚本版本：" + str(version))
    try:
        r1 = requests.get("https://mirror.ghproxy.com/https://raw.githubusercontent.com/jiankujidu/cpolar/main/nwct_cpolar.py").text
        r2 = re.findall(re.compile("version = \d.\d"), r1)[0].split("=")[1].strip()
        if float(r2) > version:
            print("发现新版本：" + r2)
            print("正在自动更新脚本...")
            os.system("killall cpolar")
            os.system("ql raw https://mirror.ghproxy.com/https://raw.githubusercontent.com/jiankujidu/cpolar/main/nwct_cpolar.py &")
    except:
        pass

# 判断CPU架构
def check_os():
    r = os.popen('uname -m').read()
    if 'aarch64' in r or 'arm' in r:
        cpu = 'arm'
    elif 'x86_64' in r or 'x64' in r:
        cpu = 'amd64'
    else:
        print('穿透失败：不支持当前架构！')
        return
    print('获取CPU架构：' + r.replace('\n', ''))
    download_cpolar(cpu)

# 下载主程序
def download_cpolar(cpu):
    if not os.path.exists("cpolar.py"):
        res = requests.get("https://mirror.ghproxy.com/https://raw.githubusercontent.com/jiankujidu/cpolar/main/cpolar.py")
        with open("cpolar.py", "wb") as f:
            f.write(res.content)
    if not os.path.exists("cpolar"):
        res = requests.get("https://static.cpolar.com/downloads/releases/3.3.18/cpolar-stable-linux-" + cpu + ".zip")
        with open("cpolar.zip", "wb") as f:
            f.write(res.content)
        os.system("unzip cpolar.zip >/dev/null 2>&1&&rm -f cpolar.zip&&chmod +x cpolar&&" + app_path + " authtoken  " + authtoken + ">/dev/null 2>&1")
    start_nwct()        

# 获取穿透url
def get_url():
    try:
        with open(log_file, encoding='utf-8') as f:
            log_content = f.read()
        reg = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        for i in re.findall(reg, log_content):
            if 'cpolar' in i:
                print("获取穿透链接成功...")
                return i.replace('\\', '')
                break
    except:
        print("运行异常")
        return "https://mirror.ghproxy.com/https://raw.githubusercontent.com/jiankujidu"

# 进程守护
def process_daemon():
    print("正在检测穿透状态...")
    global qlurl
    qlurl = get_url()
    try:
        res = requests.get(qlurl + "/login").text
        if "/images/g5.ico" in res or "/images/favicon.svg" in res:
            return True
        else:
            return False
    except:
        return False


# 执行程序
def start_nwct():
    if not process_daemon():
        os.system("rm -rf " + log_path)
        os.system("mkdir -p " + log_path)
        os.system("killall cpolar >/dev/null 2>&1")
        print("正在启动内网穿透...")
        os.system(commond)
        sleep(10)
        if process_daemon():
            if load_send():
                print("启动内网穿透成功！\n青龙面板：%s" % qlurl)
                send("内网穿透通知", "青龙面板访问地址：" + qlurl)
        else:
            print("启动内网穿透失败...")
    else:
        print("穿透程序已在运行...\nQQ交流群：706397373\n青龙面板：%s" % qlurl)


# 推送
def load_send():
    global send
    cur_path = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(cur_path)
    sendNotifPath = cur_path + "/sendNotify.py"
    if not os.path.exists(sendNotifPath):
        res = requests.get("https://mirror.ghproxy.com/https://raw.githubusercontent.com/jiankujidu/cpolar/main/sendNotify.py")
        with open(sendNotifPath, "wb") as f:
            f.write(res.content)

    try:
        from sendNotify import send
        return True
    except:
        print("加载通知服务失败！")
        return False


if __name__ == '__main__':
    version = 1.4
    try:
        authtoken = os.environ['qlnwct_authtoken']
    except:
        authtoken = ""
    try:
        token = os.environ['PUSH_PLUS_TOKEN']
    except:
        token = ""
    try:
        check_update = os.environ['qlnwctupdate']
    except:
        check_update = "true"

    if check_update != "fa>lse":
        update()
    else:
        print("变量qlnwctupdate未设置，脚本自动更新未开启！")
    if len(authtoken ) < 1:
        print("请新增变量qlnwct_authtoken！")
    else:
        check_os()
