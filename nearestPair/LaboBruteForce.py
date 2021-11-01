import math
import random
import time
import matplotlib.pyplot as plt

dot = [(2, 3),(12, 30),
    (40, 50),(5, 1),
    (12, 10),(3, 4)]

plt.plot(dot)
plt.show
def calDist(A,B):
    dist = math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
    return dist
def closestPoint(cloud):
    distRef = math.inf
    for i in range(len(cloud)):
       for j in range(i+1,len(cloud)):
           shorterDist = calDist(cloud[i],cloud[j])
           if shorterDist<distRef:
               distRef = shorterDist
               nearestPair = [cloud[i],cloud[j]] 
    return distRef,nearestPair

start = time.time()
pair = closestPoint(dot)
end = time.time()
print (end - start)
print(pair)

