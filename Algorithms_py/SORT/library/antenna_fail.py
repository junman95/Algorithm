n = int(input())
house = list(map(int,input().split(' ')))

def dist(num,array):
  sum = 0
  for i in array:
    sum += abs(num-i)
  return sum

spot = min(house)
minimum = dist(spot,house)

for i in range(min(house),max(house)+1):
  if minimum > dist(i,house):
    minimum = dist(i,house)
    spot = i

print(spot)
