# -*- coding: utf-8 -*-
# @Author  : itswcg
# @File    : utils.py
# @Time    : 19-2-20 上午11:19
# @Blog    : https://blog.itswcg.com
# @github  : https://github.com/itswcg

import requests

AK = ''  # 百度LBS AK
GEOCODER_URI = 'http://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak=' + AK


def geocoder(address):
    """
    百度lbs：地址转坐标(百度经纬坐标系)
    :param address: 地址
    :return: 坐标
    """
    res = requests.get(GEOCODER_URI.format(address)).json()
    if res.get('status') == 0:
        location = res.get('result').get('location')

        return location.get('lng'), location.get('lat')
    else:
        raise Exception('geocoder error\n {}'.format(res))


if __name__ == '__main__':
    print(geocoder('上海市'))
