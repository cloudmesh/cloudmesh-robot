#import cm
#import marvelmind

#left = cm.Motor("left")
#right = cm.Motor("right")


filename = "move-algorithm.txt"
f = open(filename)
lines = f.readlines()
f.close()

for line in lines:
    name, position = line.split(":")
    endx, endy = position.split(" ")
    print(name, position)
    print(endx, endy)
