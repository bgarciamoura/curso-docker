import redis
import json
import os
from time import sleep
from random import randint

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')
    r = redis.Redis(host=redis_host, port=6379, db=0)
    # r = redis.Redis(host='queue', port=6379, db=0)
    print('[WAITING FOR E-MAILS...]')
    while True:
        mensagem = json.loads(r.blpop('sender')[1])
        # Simulando o envio de e-mail...
        print('[SENDING E-MAIL]')
        print('[E-MAIL SUBJECT]', mensagem['assunto'])
        sleep(randint(5, 10))
        print('[E-MAIL SENT]')