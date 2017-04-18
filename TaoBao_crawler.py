# Taobao data crawler

import json, threading
from Download import dl
from urllib.parse import urlencode

def getUrl(page, keyword):
    start_url = 'https://s.taobao.com/api?'
    add_dict = {
        '_ksTS': '1492391041115_231',
        'ajax': 'true',
        'm': 'customized',
        'rn': 'fcb53e078ddd635d41aa048a8a671207',
        'q': keyword,
        'ie': 'utf8',
        's': page,
        'bcoffset': 0
    }
    return start_url + urlencode(add_dict)

def getDetail(page, keyword, output):
    print('[Catching]。。。 page: ', page)
    data = json.loads(dl.GetHtml(getUrl(page, keyword)))
    if data and data['API.CustomizedApi']['itemlist']['auctions']:
        for item in data['API.CustomizedApi']['itemlist']['auctions']:
            detail_url = 'http:' + item['detail_url']
            detail_title = item['raw_title']
            store_name = item['nick']
            if item['icon']:
                store = item['icon'][0]['innerText']
            else:
                store = '普通淘宝'
            sales_volume = item['view_sales']
            price = item['view_price']
            output.write(store+'\n'+store_name+'\n'+detail_title+'\n'+price+'元\n'+sales_volume+'\n'+detail_url+'\n\n')

def get(keyword):
    out_put_file = open(keyword + '.txt', 'w', encoding='utf8')
    for page in range(0, 1000, 10):
        th = threading.Thread(target=getDetail, args=(page, keyword, out_put_file))
        th.start()

if __name__ == '__main__':
    get(input('input keyword: '))
