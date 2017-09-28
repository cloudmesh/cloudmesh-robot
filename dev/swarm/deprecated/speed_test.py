import time
from marvelmind import MarvelmindHedge
import swarm6

time.sleep(2)
rs = swarm6.RobotSwarm('swarm.txt')
t = time.time()
tnow = time.time() - t
count = 0
while tnow < 5:
    count += 1
    ls = rs.get_positions()
    tnow = time.time() - t
    rate = count / tnow
    print('time:', str(tnow))
    print('iterations:', str(count))
    print('rate:', str(rate), 'counts per second')
    print(ls)

t = time.time()
newcount = 0
tnow = time.time() - t
while tnow < 10:
    for robot in rs.robots:
        robot.move('set', '0-0')
    tnow = time.time() - t
    newcount += 1
    newrate = newcount / tnow
    print('rate:', str(newrate))

print('position rate:', str(rate))
print('command rate:', str(newrate))







