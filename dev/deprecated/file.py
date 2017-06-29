f = open('data.txt', 'w')
f.write('some data')
f.close()

f = open('data.txt')
r = f.read()
f.close()

print (r)

import os

print (os.listdir())

# ['boot.py', 'data.txt']

os.remove('data.txt')

print (os.listdir())
