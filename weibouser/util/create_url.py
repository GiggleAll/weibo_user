# -*- encoding: utf-8 -*-

COMMENT_URL = 'https://weibo.com/aj/v6/comment/big?' \
              'ajwvr=6&id={id}&page={page}&filter=all&filter_tips_before=1&from=singleWeiBo'

HOT_URL = 'https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=0&page={page}&lefnav=0'
max_page = 1

USER_MESSAGE_URL = 'https://api.weibo.cn/2/profile/statuses?' \
                   'page=1&lfid=100103type=1&q={name}&t=3&s=2b166666&fid=107603{id}_-_WEIBO_SECOND_PROFILE_WEIBO&containerid=107603{id}_-_WEIBO_SECOND_PROFILE_WEIBO&from=1083195010&c=android&gsid=_2AkMt-wizf8NhqwJRmPESxWzhaY90wwvEieKbp_loJRMxHRl-wT9kqkIYtRV6BkKgVNEgZchYcwoMSU8Bd-itaClQGZNX&luicode=10000003&'


class GeneratorUrl(object):
    def __init__(self):
        self.comment_url = COMMENT_URL
        self.hot_url = HOT_URL

    def get_comment_urls(self, id_):
        urls = self.comment_url.format(id=id_, page='1')
        return urls

    def get_hot_urls(self):
        urls = []
        for page in xrange(0, max_page):
            urls.append(self.hot_url.format(page=max_page))
        return urls

    def get_bigv_url(self, id, name):
        url = USER_MESSAGE_URL.format(id=id, name=name)
        return url


if __name__ == '__main__':
    a = GeneratorUrl()
    print a.get_bigv_url(id='2494453215', name='大白来迟')
