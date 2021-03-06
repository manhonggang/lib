import requests
import json
import csv
import time
import random


headers = {
    'Host': 'api.taptapdada.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.10.0'

}

# 声明一个列表存储字典
data_list = []


def start_spider():
    page = 0
    while True:
        time.sleep(round(random.uniform(0.5, 1.5), 1))
        url = 'https://api.taptapdada.com/review/v1/by-app?limit=10&app_id=23452' \
              '&X-UA=V%3D1%26PN%3DTapTap%26VN_CODE%3D551%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Dtencent%26' \
              'UID%3Dda4b99bf-5e2b-4204-a92f-235474b32c4c&from={}'.format(page)
        page += 10
        resp = requests.get(url, headers=headers).json()
        datas = resp.get('data').get('list')
        if datas:
            for data in datas:
                # 评论人
                name = data.get('author').get('name')
                # 游戏时长
                played_tips = data.get('played_tips')
                # 评论内容
                contents = data.get('contents').get('text')

                # 声明一个字典储存数据
                data_dict = {}
                data_dict['name'] = name
                data_dict['played_tips'] = played_tips
                data_dict['contents'] = contents.replace('<br />', '')
                data_list.append(data_dict)

                print(data_dict)
        else:
            break


def main():

    start_spider()
    # 将数据写入json文件
    with open('data_json.json', 'a+', encoding='utf-8-sig') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)
    print('json文件写入完成')

    # 将数据写入csv文件
    with open('data_csv.csv', 'w', encoding='utf-8-sig', newline='') as f:
        # 表头
        title = data_list[0].keys()
        # 创建writer
        writer = csv.DictWriter(f, title)
        # 写入表头
        writer.writeheader()
        # 批量写入数据
        writer.writerows(data_list)
    print('csv文件写入完成')


if __name__ == '__main__':

    main()
