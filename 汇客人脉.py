'''
注册链接：http://hk.taolenet.com/#/i/13992
抓jwt_token, 定时 每半小时一次
'''
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time
import string
import requests


tx_money = 1    # 提现金额，默认1元就提
# 多号用@分割
token = ''


def get_userinfo(jwt_token):
    headers = {
        'Host': 'hkapi.taolenet.com',
        'Origin': 'http://hk.taolenet.com',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Referer': 'http://hk.taolenet.com/',
    }

    params = {
        'jwtToken': jwt_token,
    }

    response = requests.get('http://hkapi.taolenet.com/index.php/UserInfo', params=params, headers=headers).json()
    print(response)
    if response['type']:
        return response['data']['zk_money']


def match_task(jwt_token):
    headers = {
        'Host': 'hkapi.taolenet.com',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryngyCRiYQHkWsfP5k',
        'Origin': 'http://hk.taolenet.com',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1',
        'Referer': 'http://hk.taolenet.com/',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    }

    data = f'------WebKitFormBoundaryngyCRiYQHkWsfP5k\nContent-Disposition: form-data; name="jwtToken"\n\n{jwt_token}\n------WebKitFormBoundaryngyCRiYQHkWsfP5k\nContent-Disposition: form-data; name="matchTaskArr"\n\n["QQ群","QQ号","微信群","微信号"]\n------WebKitFormBoundaryngyCRiYQHkWsfP5k--\n'.encode()

    response = requests.post('http://hkapi.taolenet.com/index.php/UserCardMatch', headers=headers, data=data).json()
    print(response)
    if response['type']:
        task_id = response['data']
        print(task_id)
        time.sleep(random.randint(8, 15))
        return task_id


def task_complete(jwt_token, type, task_id):
    if '微信' in type:
        file = 'http://hk.taolenet.com/images/d0eb0478d69dea5eb05a5befbba66550.jpeg'
        account = f'wxid_{"".join(random.choice(string.digits+string.ascii_letters) for _ in range(14))}'
    elif 'QQ' in type:
        file = 'http://hk.taolenet.com/images/ebe3597718ac3c988ecc57cbf17e76a9.png'
        account = "".join(random.choice(string.digits) for _ in range(10))
    else:
        print(f'未知类型：{type}')
        return
    headers = {
        'Host': 'hkapi.taolenet.com',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarykzft1O8rBO1JRVwB',
        'Origin': 'http://hk.taolenet.com',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1',
        'Referer': 'http://hk.taolenet.com/',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    }

    data = f'------WebKitFormBoundarykzft1O8rBO1JRVwB\nContent-Disposition: form-data; name="jwtToken"\n\n{jwt_token}\n------WebKitFormBoundarykzft1O8rBO1JRVwB\nContent-Disposition: form-data; name="cardCommitId"\n\n{task_id}\n------WebKitFormBoundarykzft1O8rBO1JRVwB\nContent-Disposition: form-data; name="cardCommitText"\n\n{account}\n------WebKitFormBoundarykzft1O8rBO1JRVwB\nContent-Disposition: form-data; name="cardCommitImage"\n\n{file}\n------WebKitFormBoundarykzft1O8rBO1JRVwB--\n'

    response = requests.post('http://hkapi.taolenet.com/index.php/UserCardCommitView', headers=headers, data=data).json()
    print(response)


def task_detail(jwt_token, task_id):
    headers = {
        'Host': 'hkapi.taolenet.com',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryVtg9LogEjn2zt5JQ',
        'Origin': 'http://hk.taolenet.com',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1',
        'Referer': 'http://hk.taolenet.com/',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    }

    data = f'------WebKitFormBoundaryVtg9LogEjn2zt5JQ\nContent-Disposition: form-data; name="jwtToken"\n\n{jwt_token}\n------WebKitFormBoundaryVtg9LogEjn2zt5JQ\nContent-Disposition: form-data; name="cardCommitId"\n\n{task_id}\n------WebKitFormBoundaryVtg9LogEjn2zt5JQ\nContent-Disposition: form-data; name="cardCommitText"\n\n\n------WebKitFormBoundaryVtg9LogEjn2zt5JQ\nContent-Disposition: form-data; name="cardCommitImage"\n\n\n------WebKitFormBoundaryVtg9LogEjn2zt5JQ--\n'

    response = requests.post('http://hkapi.taolenet.com/index.php/UserCardCommitView', headers=headers, data=data).json()
    print(response)
    if response['type']:
        task_type = response['cardCommitInfo']['build_task_type']
        print(task_type)
        time.sleep(random.randint(30, 60))
        return task_type

# 提现
def tixian(jwt_token, money=1):
    headers = {
        'Host': 'hkapi.taolenet.com',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarynsqNdHbH5rhSucnf',
        'Origin': 'http://hk.taolenet.com',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1',
        'Referer': 'http://hk.taolenet.com/',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    }

    data = f'------WebKitFormBoundarynsqNdHbH5rhSucnf\nContent-Disposition: form-data; name="jwtToken"\n\n{jwt_token}\n------WebKitFormBoundarynsqNdHbH5rhSucnf\nContent-Disposition: form-data; name="money"\n\n{money}\n------WebKitFormBoundarynsqNdHbH5rhSucnf--\n'

    response = requests.post('http://hkapi.taolenet.com/index.php/UserTixian', headers=headers, data=data).json()
    print('提现------>', response)


for jwt_token in token.split('@'):
    zk_money = get_userinfo(jwt_token)
    while True:
        task_id = match_task(jwt_token)
        if task_id:
            task_type = task_detail(jwt_token, task_id)
            if task_type:
                task_complete(jwt_token, task_type, task_id)
        else:
            break
    if float(zk_money) > tx_money:
        tixian(jwt_token, tx_money)
