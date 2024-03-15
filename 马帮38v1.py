#因抓包简单和服务器会检测ip等因素 故不做账密登录处理
#入口http://mb.mabangdashang.cn/#/pages/login/reg?invite_code=KUjUNPBj&from=invite 
#抓token 填入 yuanshen_mabang 多号@分割
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
#勿开刷金币模式 有封号风险
import os
import requests
import time
import json
import random
 
 
gold = False #勿开 ！！！！有封号风险！！！！！！！！！！！！！！！！
gold_time = 3
def headers(token):
  header = {
    "XX-Device-Type": "mobile",
    "X-requested-With": "XMLHttpRequest",
    "XX-Token": token,
    "user-agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/36.363636)",
    "Content-Type": "application/json",
    "Host": "mb.mabangdashang.cn",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}
  return header

def ok_10(num):
    return num % 10 == 0

def sign(header):
  url = "http://mb.mabangdashang.cn/api/portal/Sign/sign"
  data = "{}"
  re = requests.post(url,headers=header,data=data)
  re = json.loads(re.text)
  if re["msg"] == "签到成功":
    print("签到成功，尝试double")
    id = re["data"]
    id = f"{id}"
    data = json.dumps({       
      "type":1,
      "object_id":id
      })
    url = "http://mb.mabangdashang.cn/api/portal/Sign/get_double_score_by_video"
    time.sleep(random.randint(45,60))
    re = requests.post(url,headers=header,data=data)
    re = json.loads(re.text)
    if re["msg"] == "领取成功":
      print("签到double成功！")
  else:
    print("签到失败",re["msg"])
  re = requests.get("http://mb.mabangdashang.cn/api/portal/Sign/sign",headers=header)
  re = json.loads(re.text)
  if re["msg"] == "请求成功":
    print("账户总金币：",re["data"]["score"])

def video(header,i):
  url = "http://mb.mabangdashang.cn/api/portal/Sign/watch_video"
  data = json.dumps({"type":1,"video_type":1})
  re = requests.post(url,headers=header,data=data)
  re = json.loads(re.text)
  if re["msg"] == "观看成功":
    print(f"观看第{i}日常视频成功")
    i += 1
    video_add(header)
    spt = random.randint(60,80)
    print(f"等待{spt}秒")
    print("=" * 10)
    time.sleep(spt)
    video(header,i)
  else:
    print("观看第",i,"日常视频失败",re["msg"])
    return

def video_add(header):
  url = "http://mb.mabangdashang.cn/api/portal/Sign/get_score_by_video"
  data = "{}"
  re = requests.post(url,headers=header,data=data)
  re = json.loads(re.text)
  if re["msg"] == "请求成功":
    print(f"获得金币：{re['data']}")
    return True
  else:
    print("获得金币失败",re["msg"])
    return False

def draw(header):
  url = "http://mb.mabangdashang.cn/api/portal/Sign/get_score_lottery"
  data = "{}"
  re = requests.post(url,headers=header,data=data)
  re = json.loads(re.text)
  if re["msg"] == "抽奖成功":
    gold = re["data"]["score"]
    print("抽奖成功，获得金币：",gold)
    print("尝试double中....")
    spt = random.randint(60,80)
    print(f"等待{spt}秒")
    time.sleep(spt)
    lotty_id = re["data"]["lottery_id"]
    lotty_id = f"{lotty_id}"
    url = "http://mb.mabangdashang.cn/api/portal/Sign/get_double_score_by_video"
    data = json.dumps({       
      "type":2,
      "object_id":lotty_id
      })
    re = requests.post(url,headers=header,data=data)
    print(re.text)
    re = json.loads(re.text)
    if re["msg"] == "领取成功":
      print("double成功，获得金币：",gold * 2)
      time.sleep(random.randint(25,40))
      print("==================")
      draw(header)
    else:
      print("double失败",re["msg"])
  else:
    print("抽奖失败",re["msg"])
    return
  
def add_gold(header,i,gold_times):
  stu = video_add(header)
  if stu:
    sptm = random.randint(60,80)
    print(f"等待{sptm}秒后进行下一次刷金币操作...")
    print(f"====第{gold_times}轮的第{i}次刷金币成功！====")
    time.sleep(sptm)
    if ok_10(i):
      print("满10次休眠5分钟ing....")
      print(f"==========当前轮次:{gold_times}===========")
      url = "http://mb.mabangdashang.cn/api/portal/Sign/get_user_score"
      re = requests.get(url,headers=header)
      re = json.loads(re.text)
      gold = re["data"]["score"]
      print(f"当前金币：{gold}")
      print(f"==========当前轮次:{gold_times}===========")
      time.sleep(300)
      gold_times += 1
      if gold_times > gold_time:
        print("===============结束疯狂刷金币模式===============")
        return
    add_gold(header,i + 1,gold_times)

  else:
    print(f"====第{gold_times}轮的第{i}次刷金币失败！====")
    return
  

def main_task(token):
  header = headers(token)
  sign(header)
  video(header,1)
  draw(header)
  if gold:
   print("========启动疯狂刷金币模式========\n" * 3)
   print("====================="* 6)
   add_gold(header,1,1)
  else:
    print("不进行疯狂金币模式")


if __name__ == "__main__":
 cookies = ''
 if not cookies:
    cookies = os.getenv('yuanshen_mabang')
 if not cookies:  
    print('没有token')
 cookies = cookies.split("@")
 print(f"一共获取到{len(cookies)}个账号")
 i = 1
 for cookie in cookies:
    print(f"\n--------开始第{i}个账号--------")
    try:
     main_task(cookie)
    except Exception as e:
     print("发生错误：",e)
    print(f"--------第{i}个账号执行完毕--------")
    i += 1


#框架ver：1.0.8 24/1/23