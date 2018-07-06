import json
import datetime
import redis

client = redis.Redis(os.get('REDIS_HOST'))
key = 'ProgramGuid'
def handler(event, context):
    if not r.get(key):
        r.set(key, 70200000000)
    _next = r.incr(key)
    data = {
        'next': _next,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    red
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
