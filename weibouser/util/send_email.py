# -*- encoding: utf-8 -*-


from redis import Redis


connect_redis = Redis(host='127.0.0.1', port=6379, decode_responses=True)


