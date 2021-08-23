import math

data = [60,61,65,63,98,99,90,95,91,96]
dataArray = []
total = 0

for x in data:
    total = total + x

mean = total/len(data)

squareList = []
for input in data:
    a = input-mean
    a = a**2
    squareList.append(float(a))

num = 0
for x in squareList:
    num = num + x

nd = num/len(data)
result = math.sqrt(nd)
print(result)