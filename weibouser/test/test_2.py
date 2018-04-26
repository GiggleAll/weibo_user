# -*- coding: utf-8 -*-
import requests

a = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&id=4222445466626207&page=1&filter=all&filter_tips_before=1&from=singleWeiBo'
b = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&id=4222317385695130&page=1&filter=all&filter_tips_before=1&from=singleWeiBo'
# c = 'https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fweibo.com%2Faj%2Fv6%2Fcomment%2Fbig%3Fajwvr%3D6%26id%3D4222339790871424%26page%3D1%26filter%3Dall%26filter_tips_before%3D1%26from%3DsingleWeiBo%26_rnd%3D1522236274091&domain=.weibo.com&sudaref=https%3A%2F%2Fpassport.weibo.com%2Fvisitor%2Fvisitor%3Fentry%3Dminiblog%26a%3Denter%26url%3Dhttps%253A%252F%252Fweibo.com%252Faj%252Fv6%252Fcomment%252Fbig%253Fajwvr%253D6%2526id%253D4222445466626207%2526page%253D1%2526filter%253Dall%2526filter_tips_before%253D1%2526from%253DsingleWeiBo%26domain%3D.weibo.com%26sudaref%3Dhttps%253A%252F%252Fweibo.com%252F%253Fcategory%253D0%26ua%3Dphp-sso_sdk_client-0.6.23%26_rand%3D1522236221.1544&ua=php-sso_sdk_client-0.6.23&_rand=1522236428.4741'
# b = 'https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fweibo.com%2Faj%2Fv6%2Fcomment%2Fbig%3Fajwvr%3D6%26id%3D4222317385695130%26page%3D1%26filter%3Dall%26filter_tips_before%3D1%26from%3DsingleWeiBo&domain=.weibo.com&sudaref=https%3A%2F%2Fweibo.com%2F%3Fcategory%3D0&ua=php-sso_sdk_client-0.6.23&_rand=1522234810.183'
a = 'https://login.sina.com.cn/visitor/visitor?a=crossdomain&cb=return_back&s=_2AkMt4Wm7f8NxqwJRmPkWzm3rZI9zyAvEieKbvZhgJRMxHRl-yj9jqk8HtRB6BmFHVAS8yeaHeXtJ4G3NrZ8YRWVu9MQb&sp=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFdTb81ZeCK8snOErWefUhP&from=weibo&_rand=0.9048780359784789'
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Host': 'weibo.com',
    # 'Referer': 'https://weibo.com/?category=0',
    # 'Cookie': 'YF-V5-G0=32427df11f152291036145f8d346cc49; _s_tentry=data.weibo.com; Apache=1330979959007.1191.1521011430733; SINAGLOBAL=1330979959007.1191.1521011430733; ULV=1521011430919:1:1:1:1330979959007.1191.1521011430733:; TC-Page-G0=1ac1bd7677fc7b61611a0c3a9b6aa0b4; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFGbbjnXo4MpW75iedxJrZO; TC-V5-G0=866fef700b11606a930f0b3297300d95; login_sid_t=4cff61637b5f11d6eb2d4157e26f9037; cross_origin_proto=SSL; TC-Ugrow-G0=370f21725a3b0b57d0baaf8dd6f16a18; UOR=,,www.baidu.com; YF-Ugrow-G0=b02489d329584fca03ad6347fc915997; YF-Page-G0=ee5462a7ca7a278058fd1807a910bc74; WBtopGlobal_register_version=2d333227606b1d96; SUB=_2AkMt5_x6f8NxqwJRmPESyG7laoV2yg3EieKbuw2hJRMxHRl-yj9jqm04tRB6BmfSlcyR1xG4V87b5yWpw9yUgu2YQ6dG'
}

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Host': 'api.weibo.cn',
           # 'Upgrade-Insecure-Requests': '1',
           'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
a = 'https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fweibo.com%2Faj%2Fv6%2Fcomment%2Fbig%3Fajwvr%3D6%26id%3D4223234037260758%26page%3D1%26filter%3Dall%26filter_tips_before%3D1%26from%3DsingleWeiBo&domain=.weibo.com&sudaref=https%3A%2F%2Fweibo.com%2Fa%2Faj%2Ftransform%2Floadingmoreunlogin%3Fajwvr%3D6%26category%3D0%26page%3D1%26lefnav%3D0&ua=php-sso_sdk_client-0.6.23&_rand=1522401723.3875'
a = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&id=4223054391744266&page=1&filter=all&filter_tips_before=1&from=singleWeiBo'
b = {'login': '2539a3746215f32d05c8100e941e1569', 'SUB': '_2AkMt4o7sf8NxqwJRmPkWzm3rZI9zyAvEieKbvn83JRMyHRl-yD9jqnQhtRB6BmKgA3S-DwRk4k0REeUWMRiszCywdF0k', 'SUBP': '0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFdTb81ZeCK8snOErWefUhP'}
a = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&id=4222998687461362&page=1&filter=all&filter_tips_before=1&from=singleWeiBo'
a = 'https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=0&page=1&lefnav=0'
r = requests.get(url=a)
print r.status_code, r.cookies.get_dict(), r.text

# from scrapy.crawler import Settings
#
# from redis import Redis
# redis_connect = Redis(host='127.0.0.1', port=6379, decode_responses=True, db=1)
# # redis_connect.hmset('c', {'a':'abc', 'b':'ff'})
# dict = {}
# print redis_connect.hgetall('c').__class__
# # for i in redis_connect.hscan('c'):
# #     print i