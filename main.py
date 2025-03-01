import os
import string
import random
import time
from datetime import datetime

def create_new_commit():
    text = np.random.choice(list(string.ascii_letters+string.digits),1000000,replace=True)
    text = ''.join(text)
    with open('spam.txt','w') as f:
        f.write(text)

    os.system('git add . ')

    commit_name = np.random.choice(list(string.ascii_letters+string.digits),128,replace=True)
    commit_name = ''.join(commit_name)
    commit_name = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + commit_name


    os.system('git commit -m "%s"'%commit_name)

    os.system('git push origin main')


for i in range(10):
    create_new_commit()
    time.sleep(5*60)