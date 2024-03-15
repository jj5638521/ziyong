import os
import requests
import json
import logging
import time
import random

#入口https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx77195e30616a93f9&redirect_uri=http://www.x4q4.cn/getinfo&response_type=code&scope=snsapi_userinfo&state=STATE&connect_redirect=1#wechat_redirect
# 设置日志级别
logging.basicConfig(level=logging.INFO)

# 假设你的环境变量yddk的值为"unionid1#token1\nunionid2#token2\n..."
yddk = os.environ.get('yddk')
if yddk is None:
    raise Exception("环境变量'yddk'未设置")

accounts = yddk.split("\n")

for i, account in enumerate(accounts, start=1):
    unionid, token = account.split('#')
    
    # 第一个操作
    url1 = "http://www.x4q4.cn/user/activeone"
    headers1 = {
        "unionid": unionid,
        "token": token,
        "user-agent": "Mozilla/5.0 (Linux; Android 13; PHP110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/31.428572)",
        "Content-Type": "application/json",
        "Host": "www.x4q4.cn",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    data1 = {"unionid": unionid}
    response1 = requests.post(url1, headers=headers1, data=json.dumps(data1))
    logging.info(f"账号{i} activeone：\n{response1.text}\n")
    time.sleep(random.uniform(5, 10))  # 随机延迟5到10秒

    # 第二个操作
    url2 = "http://www.x4q4.cn/trade/pushcash"
    headers2 = headers1  # 假设头信息相同
    data2 = {
        "unionid": unionid,
        "money": 0.15
    }
    response2 = requests.post(url2, headers=headers2, data=json.dumps(data2))
    logging.info(f"账号{i} pushcash：\n{response2.text}\n")
    time.sleep(random.uniform(5, 10))  # 随机延迟5到10秒