"""
需要添加环境变量 ydyCookie
作者：ノβóMakiル  QQ：419478052   团队：Maki团队网络科技
cron: 0 8,12 * * *
const $ = new Env("有道云签到");
"""

import requests
import notify
import json
import time
import os

class YouDaoController:
    POST_URL = "https://note.youdao.com/yws/mapi/user?method=checkin"
    Cookie = os.environ.get("ydyCookie");
    HEADERS = {
        "Cookie": Cookie,
        "Host": "note.youdao.com",
        "Cache-Control": "no-cache",
        "Accept": "*/*",
        "User-Agent": "YNote"
    }

    @staticmethod
    def http_request_post():
        try:
            response = requests.post(YouDaoController.POST_URL, headers=YouDaoController.HEADERS)
            response.raise_for_status()  # 检查请求是否成功
            if response.status_code == 200:
                info = json.loads(response.text)
                total = info['total'] / 1048576
                space = info['space'] / 1048576
                times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(info['time'] / 1000))
                msg = f"""
签到成功 🎉

签到获得：{space} MB
总共获得：{total} MB
签到时间：{times}
"""
            else:
                msg = f"""
签到失败 😹

返回结果：{response.text}
"""
        except requests.exceptions.RequestException as e:
            msg = f"""
签到失败 😹

错误编码：{json.loads(response.text)['error']}
错误信息：Cookie 失效了, 重新抓取一下吧
"""
        notify.send("有道云签到", msg)

    @staticmethod
    def main():
        YouDaoController.http_request_post()

if __name__ == "__main__":
    YouDaoController.main()