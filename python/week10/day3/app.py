import os
with open('/home/maor/projects/di/python/week10/day3/nameslist.txt', 'r') as f:
    content = f.read()
    skywalker = content.replace('Luke','Luke Skywalker')


with open('/home/maor/projects/di/python/week10/day3/nameslist.txt', 'w') as f:
    f.write(skywalker)