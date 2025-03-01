import os
import string
import random
import time
from datetime import datetime

def create_new_commit(char = string.ascii_letters+string.digits):
    text = ''.join(random.choice(char) for _ in range(1000000))
    with open('spam.txt','w') as f:
        f.write(text)

    os.system('git add . ')

    commit_name = ''.join(random.choice(char) for _ in range(128))
    commit_name = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + commit_name

    os.system('git commit -m "%s"'%commit_name)
    os.system('git push origin main')

for i in range(10):
    create_new_commit()
    time.sleep(5*60)