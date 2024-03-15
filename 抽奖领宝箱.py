import json
import random
import requests
import time
#只需要Authorization,写在脚本里就行了,手动挂满听书180分钟就可以,一天跑一次,一定先挂满180分钟再跑
Authorization = "eyJhbGciOiJSUzI1NiIsImNyaXQiOlsiaXNzIiwianRpIiwiaWF0IiwiZXhwIl0sImtpZCI6IjE1MzEyMDM3NjkiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2OTU1NTUyNzUsImlhdCI6MTY5NDI1OTI3NSwiaXNzIjoiIiwianRpIjoiODIwMjgzMGY2NTBmM2ZmYmYyYmY1Yjg2NjY5OTQyM2YiLCJ1c2VyIjp7InVpZCI6NDYyOTg5ODc5LCJuaWNrbmFtZSI6IuapmeeMq-eMqyIsImltZWkiOiIiLCJ1dWlkIjoiIiwiZGV2aWNlSWQiOiIiLCJyZWdUaW1lIjoxNjg0ODc5NzEwLCJ2aXBFeHBpcmVBdCI6MTY5MjQ1MTQyNCwic21faWQiOiIyMDIzMDUyNDA2MDgyMjdjYzI0ZDQ1ZGZiZTk1YjVkYzkyZjVlZGYxMjA3NjVmMDBiNmE3M2ExNzdmYWY0MCIsIm51dCI6MTY4NDg3OTczNywiaWZ1IjowLCJpc19yYmYiOjAsImFjdF9pZCI6MCwiYmluZF9hdCI6MCwidGlkIjoiRFV5dXlyUXY1dmtuRDJ0UGRBTkN5X3hBYTg2aE5wX2NUMDYwUkZWNWRYbHlVWFkxZG10dVJESjBVR1JCVGtONVgzaEJZVGcyYUU1d1gyTlVNRFl3YzJoMSIsInRfbW9kZSI6Mn19.E7vKbn83sp37-mXJxmTiO0rAHYaOEcbNgoTc2ynHopsGgNSiqnRW6bC6m1_hHuOT3KJlUWjewpfYaKRvBfwKKWpOZ7A4QPAavTKQ-1GyZba3-FGq13YWQ_YDSnZfMN35oq2Q6gUpaEdOA8GoAtUyjbIQE1bJaEuQ_Ph69vP_XI8
eyJhbGciOiJSUzI1NiIsImNyaXQiOlsiaXNzIiwianRpIiwiaWF0IiwiZXhwIl0sImtpZCI6IjE1MzEyMDM3NjkiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2OTU1NTU3NzUsImlhdCI6MTY5NDI1OTc3NSwiaXNzIjoiIiwianRpIjoiYjY0YmFjMTk3YjA2NmI5MTM0MmYzNzA1YWMxZWI0YTEiLCJ1c2VyIjp7InVpZCI6NDk1Nzk2MjA2LCJuaWNrbmFtZSI6Iue6ouitpuaciOS6rjMiLCJpbWVpIjoiIiwidXVpZCI6IiIsImRldmljZUlkIjoiIiwicmVnVGltZSI6MTY5MTQ0ODUxMSwidmlwRXhwaXJlQXQiOjAsInNtX2lkIjoiMjAyMzA4MDgwNjQ4MjhiYjMyNmVhZjA4MDRkNGIzNjcwMDZkMDJhMmIwZjM0MjAwMzkzZWMxYTllYTEwOGIiLCJudXQiOjAsImlmdSI6MCwiaXNfcmJmIjowLCJhY3RfaWQiOjAsImJpbmRfYXQiOjAsInRpZCI6IkRVeXV5clF2NXZrbkQydFBkQU5DeV94QWE4NmhOcF9jVDA2MFJGVjVkWGx5VVhZMWRtdHVSREowVUdSQlRrTjVYM2hCWVRnMmFFNXdYMk5VTURZd2MyaDEiLCJ0X21vZGUiOjJ9fQ.nGnlT1pXTXkm6RSKP1-O37admpTNfwG_W7-bxtcAX_gl1mhbt_AHXOMVr9N1Uwh25EpoHouvVO2dA4pvrq-uFvgw-xZOskRw1GeGk9ZQ0R0dKLoT-JIBeWhU9yOiuZfdYyUfpPGCRZm8-ir_OmsVzpaddhGsxVctIYGUIgcyrik"
t = time.time()
# 查余额
def coin():
    url = "https://api-gw.wtzw.com/welf/h5/v1/task-list"
    headers = {
        "Authorization": Authorization
    }
    data = {
        "module_sign": [
            {
                "sign": "9fdefb36c2ec66942d79b1a9a0a8d85d",
                "category": "time_limit"
            },
            {
                "sign": "0d7debfbc25c2184926b23b480bd2450",
                "category": "daily_task"
            }
        ],
        "t": t
    }
    getJson = json.dumps(data).encode("utf-8")
    response = requests.post(url=url, headers=headers, data=getJson)
    # print(response.text)
    jsondata = json.loads(response.text)
    result = jsondata["user"]["coin_data"]
    print("余额是" + result + "金币")


# 五次幸运抽奖
def lucky_draw():
    print("=======开始幸运抽奖=======\r")
    url = "https://xiaoshuo.wtzw.com/api/v2/lucky-draw/do-extractin"
    headers = {
        "Authorization": Authorization
    }
    data = {
        "t": t,
        "apiVersion": 20190309143259 - 1.9
    }
    for i in range(0, 5):
        response = requests.get(url=url, headers=headers, params=data)
        print(response.text)
        time.sleep(random.randint(1, 5))


# 五次幸运7抽奖
def lucky_draw_seven():
    print("=======开始幸运7抽奖=======\r")
    url = "https://api-gw.wtzw.com/lucky-seven/h5/v1/lottery"
    querystring = {"t": t}
    payload = "source=3&apiVersion=20190309143259 - 1.9"
    headers = {
        "Authorization": Authorization,
        "content-type": "application/x-www-form-urlencoded"
    }
    for i in range(0, 5):
        response = requests.post(url=url, data=payload, headers=headers, params=querystring)
        jsondata = json.loads(response.text)
        result = jsondata["data"]["title"]
        print(result)
    time.sleep(random.randint(1, 5))


# 领宝箱
def box():
    print("=======开始领宝箱=======\r")
    url = "https://api-gw.wtzw.com/welf/h5/v1/task/treasure/reward"
    headers = {
        "Authorization": Authorization,
        "content-type": "multipart/form-data;"
    }
    querystring_box = {"t": t}
    response_box = requests.post(url=url,headers=headers, params=querystring_box)
    print(response_box.text)
    time.sleep(random.randint(1, 5))


# 领宝箱视频
def box_video():
    print("=======开始领宝箱视频=======\r")
    url = "https://api-gw.wtzw.com/welf/h5/v1/task/treasure/video/reward"
    headers = {
        "Authorization": Authorization,
        "content-type": "application/json"
    }
    querystring = {"t": t}
    payload = {
        "position": "welfare_treasurebox_timely",
        "video_prefix": "task_video_two"
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    print(response.text)
    time.sleep(random.randint(1, 5))


# 100次金币
def coin_150():
    print("=======开始领取100次150金币=======\r")
    url = "https://api-ks.wtzw.com/api/v1/coin/add"
    payload = "position_id=inchapter_top&type=6&sign=1"
    headers = {
        "Authorization": Authorization,
        "Host": "api-ks.wtzw.com",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    for i in range(0, 101):
        response = requests.post(url=url, data=payload, headers=headers)
        jsondata = json.loads(response.text)
        print("增加了" + jsondata["data"]["coin"] + "金币", "剩余" + jsondata["data"]["times"] + "次")
        time.sleep(random.randint(1, 5))


def finish_reward():
    # 113,161
    task_id = [22, 24, 154, 155, 156, 157, 158, 159, 160, 100, 105, 111, 113, 115, 116, 161, 42, 43, 44, 45, 46, 47]
    url = "https://api-gw.wtzw.com/welf/h5/v1/task/finish-task"
    do_url = "https://api-gw.wtzw.com/welf/h5/v1/task/reward"
    headers = {
        "Authorization": Authorization
    }
    for id in task_id:
        data = {
            "t": t,
            "task_id": id

        }
        task_data = {
            "t": t,
            "task_id": id,
            "type_prefix": "task"
        }
        video_data = {
            "t": t,
            "task_id": id,
            "type_prefix": "video"
        }
        if id == 113:
            for i in range(0, 5):
                r4 = requests.post(url=url, headers=headers, data=data)
                print(r4.text)
                time.sleep(random.randint(1, 5))
                r5 = requests.post(url=do_url, headers=headers, data=task_data)
                print(r5.text)
                time.sleep(random.randint(1, 5))
                r6 = requests.post(url=do_url, headers=headers, data=video_data)
                print(r6.text)
                time.sleep(random.randint(1, 5))
        else:
            r1 = requests.post(url=url, headers=headers, data=data)
            print(r1.text)
            time.sleep(random.randint(1, 5))
            r2 = requests.post(url=do_url, headers=headers, data=task_data)
            print(r2.text)
            time.sleep(random.randint(1, 5))
            r3 = requests.post(url=do_url, headers=headers, data=video_data)
            print(r3.text)
            time.sleep(random.randint(1, 5))


if __name__ == '__main__':
    # lucky_draw()
    # coin_150()
    lucky_draw_seven()
    box()
    box_video()
    finish_reward()
    # coin()
