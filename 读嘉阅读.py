import time
import hashlib
import requests
import random
def sha_256(text):
    "sha_256加密"
    hash = hashlib.sha256()
    hash.update(bytes(f'{text}',
                      encoding='utf-8'))
    return hash.hexdigest()
def getStr(s):
    r = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    r = ''.join([r[random.randint(0, len(r) - 1)] for i in range(s)])
    return r
def getAASKey(e):
    n = []
    o = []
    for t in range(len(e)):
        if t % 2 == 0:
            o.append(e[t])
        else:
            n.append(e[t])
    key = ''.join(o) + ''.join(n)
    md5_hash = hashlib.md5(key.encode()).hexdigest()
    return md5_hash

class Read:
    def __init__(self,cg):
        self.fsid=cg.get('afs_tokenid')
        self.did=cg.get('device_token')
        self.cat=cg.get('cash_Access_Token')
        self.headers = {
            'Access-Api-Dt': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            'Access-T-Id-In': '41',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; 22011211C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36;xsb_dujia;xsb_dujia;8.0.8;native_app;6.5.1',
            'Content-Type': 'application/json',
            'Access-T-Id': '41',
            'Access-Token': cg.get('access_token')
        }
    def updateSignature(self):
        getTimeS=str(int(time.time()*1000))
        appid = 'jiaxing'
        rstr = getStr(32)
        appkey = '7200328065bd807fe056fbaadd92deed'
        aask = getAASKey(appkey)
        md5str = f'{appid}{rstr}{getTimeS}{aask}'
        md5s = hashlib.md5(md5str.encode()).hexdigest()
        r = f'{appid};{rstr};{getTimeS};{md5s}'
        self.headers.update({'Access-Api-Signature': r})
    def getPayload(self,dictPayload):
        sorted_keys = sorted(dictPayload.keys())
        md5str=''
        for k in sorted_keys:
            v=dictPayload.get(k)
            md5str+=f'{k}={v}&'
        md5str+='appkey=7200328065bd807fe056fbaadd92deed'
        md5s = hashlib.md5(md5str.encode()).hexdigest()
        dictPayload.update({"signature": md5s})
        return dictPayload
    def _optionp_list(self):
        u = 'https://yapi.y-h5.iyunxh.com/api/aoslearnfoot/_optionp_list?activity_id=226'
        self.updateSignature()
        r = requests.get(u, headers=self.headers)
        rj = r.json()
        data = rj.get('data')
        time.sleep(random.randint(1, 2))
        for i in data:
            print('=' * 20)
            title = i.get('title')
            module_id = i.get('m_id')
            activity_id = i.get('id')
            print(f'do task:{title}')
            uu = f'https://yapi.y-h5.iyunxh.com/api/aoslearnfoot/optionp_detail?id={activity_id}'
            self.updateSignature()
            user_undone_num = requests.get(uu, headers=self.headers).json().get('data').get('user_undone_num')
            if user_undone_num == 0:
                print('all task is over break')
                continue
            self._task_list(module_id, activity_id)
            time.sleep(random.randint(1, 2))

    def _task_list(self, module_id, activity_id):
        u = f'https://yapi.y-h5.iyunxh.com/api/aosbasemodule/_task_list?offset=0&count=50&module_id={module_id}&activity_id={activity_id}'
        self.updateSignature()
        r = requests.get(u, headers=self.headers)
        rj = r.json()
        # print(r.text)
        data = rj.get('data')
        time.sleep(random.randint(1, 2))
        for i in data:
            print('-' * 20)
            title = i.get('title')
            id = i.get('id')
            user_done = i.get('user_done')
            if user_done == 1:
                print(f'task is over break:{title}')
                continue
            print(f'do task:{title}')
            self.f_task(id)
            time.sleep(2)

    def f_task(self, task_id):
        self.updateSignature()
        u = f'https://yapi.y-h5.iyunxh.com/api/aosbasemodule/task_create'
        p = {"task_id": task_id}
        r = requests.post(u, headers=self.headers, json=p)
        rj = r.json()
        print(r.text)
        task_record_id = rj.get('data').get('task_record_id')
        uu = 'https://yapi.y-h5.iyunxh.com/api/aosbasemodule/task_done'
        pp = {"task_record_id": str(task_record_id), "collect_info": "",
              "afs_tokenid": self.fsid, "device_token": self.did}
        self.updateSignature()
        rr = requests.post(uu, headers=self.headers, json=pp)
        rrj = rr.json()
        print(rr.text)
        if rrj.get('code') == 0:
            print(rr.text)
        time.sleep(random.randint(2, 3))
        self.ac_lottery_times()

    def ac_lottery_times(self):
        u = 'https://yapi.y-h5.iyunxh.com/api/aoslottery/ac_lottery_times?id=2866'
        self.updateSignature()
        r = requests.get(u, headers=self.headers)
        rj = r.json()
        print(r.text)
        data = rj.get('data')
        if data.get('show_remain') != 0:
            self.ac_sub()

    def ac_sub(self):
        u = 'https://yapi.y-h5.iyunxh.com/api/aoslottery/ac_sub'
        self.updateSignature()
        p = {"id": 2866, "verif_uuid": "", "verif_code": "", "afs_tokenid": self.fsid,
             "collect_info": "", "longitude": 0, "latitude": 0, "device_token": self.did}
        r = requests.post(u, headers=self.headers, json=p)
        rj = r.json()
        print(r.text)
        if rj.get('code') == 0:
            goods_title = rj.get('data').get('goods_title')
            print(goods_title)
        time.sleep(random.randint(2, 3))
        self.ac_lottery_times()

    def tx(self):
        u = 'https://yapi.y-h5.iyunxh.com/api/aoslottery/act_user?offset=0&count=20&activity_id=2866&module_id=40602'
        self.updateSignature()
        r = requests.get(u, headers=self.headers)
        rj = r.json()
        print(r.text)
        data = rj.get('data')
        for i in data:
            print("-"*20)
            print('奖品：',i.get('goods_title'))
            if i.get('state')==0:
                self.cash_send(i.get('cash_data'))
            else:
                print('已经提现过了')
                print(i.get('callback_text'))
            time.sleep(2)
    def cash_send(self,params):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8259',
            'Content-Type': 'application/json',
            'Access-Wxclient-Type': 'wx_minipro',
            'Access-Token': self.cat,
            'referer': 'https://servicewechat.com/wx57d3a2086852ddcd/7/page-frame.html',
            'xweb_xhr': '1',
            'Access-Api-Unique-Token': '1',
            'Access-T-Id': '1',
        }
        u = 'https://ya.iyunxh.com/api/aosbasemodule/cash_send'
        r=requests.get(u,headers=headers,params=params)
        print('提现结果',r.text)

if __name__ == '__main__':
    #name随便，afs_tokenid，access_token，device_token，抓包task_done接口，看headers和响应体
    #cash_Access_Token提现token需要手动抓包小程序。
    #换设备登录需要重新抓包
    cgl = [
        {
            'name': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            'afs_tokenid': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            'device_token': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            'access_token':'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX==',
            'cash_Access_Token' :'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=='

        },
    ]
    for cg in cgl:
        api = Read(cg)
        api._optionp_list()
        api.tx()