#签到3天 = 15r 闲鱼上卖！！！！！！！！别傻乎乎去平台卖
#入口 : 走个头谢谢:http://h5.feifan.art/#/login/singin?uid=2119949
#登录后进入网页版抓取token 填入yuanshen_fhsz 多号@分割
import requests
import json
import os
requests.packages.urllib3.disable_warnings()
code = "fhsz"
ver = "1.0.2"
def version():

    try:
     txt = requests.get("https://gitee.com/HuaJiB/yuanshen34/raw/master/pubilc.txt").text
     print(txt)
     url = f"http://101.132.127.171/api/huaji/?version={ver}&code={code}"
     r = json.loads(requests.get(url).text)
     if r["ok"]:
        if r["update"]:
            print(f"✅有新版本请更新,当前版本:{ver},最新版本:",r["latest_version"])
            exit()
        else:
            print(f"✅当前版本为最新版本或不用更新,当前版本:{ver},最新版本:",r["latest_version"])
            print("更新日志:",r["data"]["update_note"])
     else:
        print("脚本已关闭")
    except:
        print("服务器失联....")

class yuanshen:
    def __init__(self,cookie):
        self.url = 'http://feifanapi.feifan.art'
        self.cookie = cookie
        self.headers = {
    "Host": "feifanapi.feifan.art",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "appDevice": "android",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160083 MMWEBSDK/20231202 MMWEBID/98 MicroMessenger/8.0.47.2560(0x28002F30) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
    "content-type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "moduleType": "0",
    "platform": "1",
    "token": self.cookie,
    "appVersion": "41",
    "Accept": "*/*",
    "Origin": "http://h5.feifan.art",
    "X-Requested-With": "com.tencent.mm",
    "Referer": "http://h5.feifan.art",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}

    def sign_newyear(self):
           url = self.url + '/app/newYearSign/userSign'
           r = requests.post(url, headers=self.headers)
           print("✅今日活动签到结果:",r.text)
           url = self.url + '/app/newYearSign/newYearSignInfo'
           r = requests.get(url, headers=self.headers)
           if r.status_code == 200:
              r = json.loads(r.text)
              print("✅您已签到:",r["data"]["userTaskOneCoiledSignDays"],"天")
           else:
               print("查询失败",r.text)
            
           if r["data"]["userTaskOneCoiledSignDays"] == 3:
                print("✅恭喜您已连续签到3天")
                print("✅已自动领取奖励")
                url = self.url + '/app/newYearSign/receiveReward'
                data = '{"taskType":1}'
                r = requests.post(url, headers=self.headers, data=data)
                print("✅领取奖励结果:",r.text)

    def sign_daily(self):
        url = self.url + '/starPalace/user/receiveAll'
        data = "{}"
        r = requests.post(url, headers=self.headers, data=data)
        rjson = json.loads(r.text)
        print("✅今日星球领凤凰:",rjson["data"]["receiveNumber"],"个")
 


if __name__ == '__main__':
    version()
    cookie = ''
    if not cookie:
        cookie = os.getenv("yuanshen_fhsz")
        if not cookie:
            print("请设置环境变量:yuanshen_fhsz")
            exit()
    cookies = cookie.split("@")
    print(f"一共获取到{len(cookies)}个账号")
    i = 1
    for cookie in cookies:
     print(f"\n--------开始第{i}个账号--------")
     main = yuanshen(cookie)
     main.sign_newyear()
     main.sign_daily()
     print(f"--------第{i}个账号执行完毕--------")
     i += 1