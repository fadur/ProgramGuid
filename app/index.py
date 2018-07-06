import os
import json
import datetime
import redis

client = redis.Redis(
    host=os.environ.get('REDIS_HOST'),
    port=os.environ.get('REDIS_PORT')
)
key = 'ProgramGuid'

def handler(event, context):
    if not client.get(key):
        client.set(key, 70200000000)
    _next = client.incr(key)
    data = {
        'next': _next,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
