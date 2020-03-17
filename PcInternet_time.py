# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:12:26 2020

@author: pc
"""

import os
import ntplib
import time

ntp_server_url = 'ntp5.aliyun.com'


def get_ntp_time(ntp_server_url):
    """
    通过ntp server获取网络时间
    :param ntp_server_url: 传入的服务器的地址
    :return: time.strftime()格式化后的时间和日期
    """

    ntp_client = ntplib.NTPClient()
    ntp_stats = ntp_client.request(ntp_server_url)
    fmt_time = time.strftime('%X', time.localtime(ntp_stats.tx_time))
    fmt_date = time.strftime('%Y-%m-%d', time.localtime(ntp_stats.tx_time))
    return fmt_time, fmt_date


def set_system_time(new_time, new_date):
    """
    通过os.system来设置时间,需要管理员权限
    :param new_time:
    :param new_date
    :return: 无返回值
    """
    os.system('time {}'.format(new_time))
    os.system('date {}'.format(new_date))

'''
if __name__ == '__main__':
    ntp_server_time, ntp_server_date = get_ntp_time(ntp_server_url)
    set_system_time(ntp_server_time, ntp_server_date)
    print('时间已经与{}同步'.format(ntp_server_url))
'''

if __name__ == '__main__':
    exit_code = os.system('ping www.baidu.com')
    if not exit_code:
        ntp_server_time, ntp_server_date = get_ntp_time(ntp_server_url)
        set_system_time(ntp_server_time, ntp_server_date)
        print('时间已经与{}同步'.format(ntp_server_url))
    else:
        print('网络未连接')

