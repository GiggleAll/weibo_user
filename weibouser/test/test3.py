from datetime import datetime, timedelta
import time

a = datetime.now() - timedelta(days=1)
# time.sleep(1)
b = datetime.now()

c = b-a
if c > timedelta(seconds=1):
    print 123

import redis
import pickle

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True, db=1)
test = {'datetime': pickle.dumps(a)}
# r.hmset('test', test)
dd = r.hget('fadsg', 'fdsggsd')
print dd
print dd is None
# dd = pickle.loads(dd)
# print dd , type(dd)
