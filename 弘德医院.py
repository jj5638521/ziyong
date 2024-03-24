'''
https://hongdewx.rrshop.cc/
抓openid
多号用@隔开，青龙变量：MM_hdyy
每天0.3，黑号跑不了
'''
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import random
import time
import requests
import base64
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


open_id_all = ''
if not open_id_all:
    open_id_all = os.getenv('MM_hdyy')
if not open_id_all:
    print('没有open_id,不执行')
    exit()
activity_id = '1536'

headers = {
    'Host': '007wxapi.hema.ren',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309092b) XWEB/8555 Flue',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'origin': 'https://hongdewx.rrshop.cc',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://hongdewx.rrshop.cc/',
    'accept-language': 'zh-CN,zh;q=0.9',
}


today = datetime.now().strftime('%Y-%m-%d')
def get_all_spid():
    if not os.path.exists('hdyy_spid'):
        with open('hdyy_spid', 'w', encoding='utf-8') as f:
            f.write('{"2024-03-05": "1536"}\n')
    with open('hdyy_spid', 'r', encoding='utf-8') as f:
        id_read = f.read()
    id_list = id_read.split('\n')
    id_list.reverse()
    for sp_dict in id_list:
        if sp_dict:
            sp_dict = json.loads(sp_dict).values()
            sp_id = list(sp_dict)[0]
            print('上一期的视频id：', sp_id)

            data = {
                'id': sp_id,
                'user_id': '670511',
            }
            for i in range(int(sp_id), int(sp_id) + 200):
                data['id'] = str(i)
                response = requests.post('https://007wxapi.hema.ren/apiadmin/activity.Activity/ActivityIntro',
                                         headers=headers, data=data).json()
                if response['code'] == 200:
                    if response['data']['company_id'] == 15 and today in response['data']['begin_time']:
                        today_id = str(response['data']['id'])
                        print('获取到今天的视频id', today_id)
                        with open('hdyy_spid', 'a+', encoding='utf-8') as wf:
                            wf.write(json.dumps({today: today_id}) + '\n')
                        break
            else:
                print('没有获取到今天的视频id')
            break


get_all_spid()

with open('hdyy_spid', 'r', encoding='utf-8') as f:
    id_read = f.read()
id_list = id_read.split('\n')
id_list.reverse()
for sp_dict in id_list:
    if sp_dict:
        sp_dict = json.loads(sp_dict)
        today_id = sp_dict.get(today)
        if today_id:
            activity_id = today_id
            break
else:
    print('今天的视频id未找到，不允许脚本')
    exit()


proxies = {'http': '', 'https': ''}
def modify_proxy(minute=5):
    pass    # 要加代理在这加，测试过了，黑号好像和代理没太大关系，加不加都行

class AES_:
    def __init__(self):
        self.key = '*!RnOVwZXdpoHzCf'
        self.iv = '34mmPuV$Wy*L@VwU'

    def AES_Encrypt(self, word, mode="CBC", padding="Pkcs7"):
        key = self.key.encode()
        iv = self.iv.encode()
        word = word.encode()
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(pad(word, AES.block_size))
        return base64.b64encode(encrypted).decode()

    def AES_Decrypt(self, word, mode="CBC", padding="Pkcs7"):
        key = self.key.encode()
        iv = self.iv.encode()
        word = base64.b64decode(word)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(word), AES.block_size)
        return decrypted.decode()


aes = AES_()


def ksp_main(open_id, activity_id):
    def lingqian(nick_name, uid):
        for i in range(10):
            try:
                data = {
                    'activity_id': aes_activity,
                    'uid': aes_uid,
                    'openid': aes.AES_Encrypt(open_id),
                    'v': '1',
                }
                response = requests.post('https://007moneyapi.hema.ren/apiadmin/system.Shop/lingqianpay', headers=headers,
                                         data=data, proxies=proxies)
                if response.status_code == 200:
                    print(f'{nick_name, open_id}--- {uid} 领钱结果 -----', response.text)
                    if '0.3' in response.text:
                        return True
                    if '黑名单' in str(response):
                        print('黑名单uid', uid)
                    break
                else:
                    print(f'领钱异常，重试第{i + 1}次----')
            except Exception as e:
                if 'proxy' in str(e).lower():
                    modify_proxy()

    def login(open_id):
        data = {
            'openid': open_id,
        }
        for i in range(5):
            try:
                response = requests.post('https://007wxapi.hema.ren/apiadmin/weixin.Fans/havefans', headers=headers,
                                         data=data, proxies=proxies)
                time.sleep(random.randint(1, 2))
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f'{open_id}登录异常，重试第{i + 1}次')
            except Exception as e:
                if 'proxy' in str(e).lower():
                    modify_proxy()

    def get_timu_info(data):
        for i in range(5):
            try:
                response = requests.post('https://007wxapi.hema.ren/apiadmin/activity.Activity/ActivityIntro',
                                         headers=headers, data=data, proxies=proxies)
                if response.status_code == 200:
                    response = response.json()
                    minutes = response['data']['minutes']
                    question_id = response['data']['question_id']
                    answer = []
                    question_id_list = []
                    for question in response['data']['questionlist']:
                        answer.append(question['answer'])
                        question_id_list.append(str(question['id']))
                    answer_str = ','.join(answer)
                    question_id_str = ','.join(question_id_list)
                    print(f'minutes ------- {minutes}')
                    print(f'question_id: {question_id} --------- answer:{answer_str}, quertion_id_list:{question_id_str}')
                    time.sleep(random.randint(1, 6))

                    # 增加观看次数
                    data = {
                        "id": uid,
                        "sum": minutes
                    }
                    for i in range(5):
                        try:
                            response = requests.post('https://007wxapi.hema.ren/apiadmin/weixin.Fans/addview',
                                                     headers=headers, data=data, proxies=proxies)
                            if response.status_code == 200:
                                break
                            else:
                                print(f'增加观看次数异常，重试{i + 1}次')
                        except Exception as e:
                            if 'proxy' in str(e).lower():
                                modify_proxy()
                    return question_id, answer_str, question_id_str
                else:
                    print(f'获取题目信息失败，重试第{i + 1}次')
            except Exception as e:
                if 'proxy' in str(e).lower():
                    modify_proxy()

    def isBlack(uid):
        try:
            data = {
                'id': str(uid),
            }
            response = requests.post('https://007wxapi.hema.ren/apiadmin/weixin.Fans/fansBlack', headers=headers,
                                     data=data, proxies=proxies).text
            if '是' in response:
                return True
        except Exception as e:
            if 'proxy' in str(e).lower():
                modify_proxy(1)

    response = login(open_id)
    print('登录信息：', response)
    if not response:
        return
    nick_name = response['data']['nick_name']
    agent_id = str(response['data']['agent_id'])
    uid = str(response['data']['id'])

    if isBlack(uid):
        print('黑名单uid', uid)
        return

    aes_uid = aes.AES_Encrypt(uid)
    aes_agent = aes.AES_Encrypt(agent_id)
    aes_activity = aes.AES_Encrypt(activity_id)

    def watch_sp():
        # 加入观看
        data = {
            'id': aes_activity,
            'user_id': aes_uid,
            'agent_id': aes_agent,
            'v': '1',
        }
        for i in range(5):
            time.sleep(random.randint(1, 3))
            try:
                response = requests.post('https://007wxapi.hema.ren/apiadmin/activity.Activity/addviews', headers=headers,
                                         data=data, proxies=proxies).json()
                print(response)
                if response['code'] == 200:
                    break
            except Exception as e:
                if 'proxy' in str(e).lower():
                    modify_proxy()
        time.sleep(random.randint(1, 3))

        # 获取时长
        data = {
            'id': activity_id,
            'user_id': '670511',
        }
        question_id, answer_str, question_list = get_timu_info(data)

        # 观看完毕
        data = {
            'user_id': aes_uid,
            'minutes': '++vQ0ZiPuBHGbeghf1n85A==',
            'begin_time': '/VwyeTAEXp93S4zwYu950Q==',
            'end_time': '/VwyeTAEXp93S4zwYu950Q==',
            'status': 'FsonAzkH9vNdNNYcTlxnKA==',
            'activity_id': aes_activity,
            'v': '1',
        }
        for i in range(10):
            try:
                response = requests.post('https://007wxapi.hema.ren/apiadmin/log.ActivityUser/activityLog', headers=headers, data=data, proxies=proxies).json()
                print(response)
                if response['code'] == 200:
                    act_data = {
                        'id': activity_id,
                        'user_id': uid,
                    }
                    requests.post('https://007wxapi.hema.ren/apiadmin/log.ActivityUser/activityActivity', headers=headers, data=act_data, proxies=proxies)
                    break
                else:
                    print(f'观看异常，重试{i + 1}次')
            except Exception as e:
                if 'proxy' in str(e).lower():
                    modify_proxy()
        time.sleep(random.randint(1, 6))

        print('开始答题 ------')
        # 答题
        data = {
            'activity_id': aes_activity,
            'user_id': aes_uid,
            'question_id': aes.AES_Encrypt(str(question_id)),
            'list_id': aes.AES_Encrypt(question_list),
            'answer': aes.AES_Encrypt(answer_str),
            'answer_correct': 'FGr1FPfkapWQwir/fKh62A==',
            'correct': aes.AES_Encrypt(answer_str),
            'num': 'FsonAzkH9vNdNNYcTlxnKA==',
            'v': '1',
        }
        for i in range(2):
            try:
                resp = requests.post('https://007wxapi.hema.ren/apiadmin/log.QuestionUser/questionLog', headers=headers,
                                     data=data, proxies=proxies)
                if resp.status_code == 200:
                    break
                else:
                    print(f'答题失败，重试{i + 1}次， {resp.text}')
                    time.sleep(1)
            except Exception as e:
                if 'proxy' in str(e).lower():
                    modify_proxy()
        time.sleep(random.randint(1, 5))

        data = {
            'id': uid,
            'correct': '1',
        }
        for i in range(5):
            try:
                resp = requests.post('https://007moneyapi.hema.ren/apiadmin/weixin.Fans/addanswer', headers=headers,
                                     data=data, proxies=proxies)
                if resp.status_code == 200:
                    break
            except Exception as e:
                if 'proxy' in str(e).lower():
                    modify_proxy()
        time.sleep(random.randint(1, 3))
        for i in range(3):
            try:
                data = {
                    'id': uid,
                    'red': '0.3',
                }

                response = requests.post('https://007wxapi.hema.ren/apiadmin/weixin.Fans/addred', headers=headers,
                                         data=data, proxies=proxies)
                if response.status_code == 200:
                    break
            except Exception as e:
                if 'proxy' in str(e).lower():
                    modify_proxy()
        time.sleep(random.randint(1, 3))
    watch_sp()
    lingqian(nick_name, uid)


def main_thread(open_id):
    try:
        ksp_main(open_id, activity_id)
    except Exception as e:
        print(e)
        print(f'open_id ----> {open_id} 执行报错 ！！！！！！！')


for open_id in open_id_all.split('@'):
    main_thread(open_id)
