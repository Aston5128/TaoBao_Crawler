# coding=utf-8
# Download 1.0.3
# Downlod html file module by Aston5128

import requests
import random
import time
import re


# noinspection PyBroadException
class download:
    def __init__(self):
        self.user_agint_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/"
            "536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 "
            "Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari"
            "/535.24"
        ]

        print('[Catching IP]。。。')
        ip_listn = re.findall('r/>(.*?)<b', requests.get('http://haoip.cc/tiqu.htm').text, re.S)
        self.ip_list = [re.sub('\n', ' ', ip).strip() for ip in ip_listn]
        # self.ip_list = ['123.233.123.555']

    def TryUrl(self, url, time_out, proxy, num_retries):
        if num_retries > 0:
            print('[Catching]。。。Spider at 6 second：Reciprocal{0}times'.format(num_retries))
            time.sleep(6)
            return self.GetHtml(url, time_out, proxy, num_retries - 1)
        else:
            i_p = random.choice(self.ip_list)
            proxy = {'http': i_p}
            print('[Proxy IP invalid]。。。Changing IP，new IP：' + i_p)
            return self.GetHtml(url, time_out, proxy=proxy)

    def GetHtml(self, url, time_out=3, proxy=None, num_retries=6):
        print('[Selecting User-Agint]。。。')
        header = {'User-Agint': random.choice(self.user_agint_list)}
        try:
            print('[Catching]。。。Proxy IP：', proxy, ' url: ' + url)
            return requests.get(url, headers=header, timeout=time_out).text
        except:
            print('[Failed]。。。Proxy IP：', proxy)
            return self.TryUrl(url, time_out, proxy, num_retries)


dl = download()
