import string
import random
import numpy as np

text = np.random.choice(list(string.ascii_letters+string.digits),1000000,replace=True)
text = ''.join(text)
with open('spam.txt','w') as f:
    f.write(text)