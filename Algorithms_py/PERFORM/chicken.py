from itertools import combinations
from collections import deque
N,M = map(int,input().split())
city_map = list(list(map(int,input().split())) for _ in range(N))

house_loc = list()
chicken_loc = list()
for i in range(N):
  for j in range(N):
    if city_map[i][j] == 1:
      house_loc.append((i,j))
    elif city_map[i][j] == 2:
      chicken_loc.append((i,j))

print(house_loc)
print(chicken_loc)

chicken_loc_lists = deque(list(combinations(chicken_loc,M)))
chicken_dist=1000000
while(chicken_loc_lists):
  cur_chicken_loc = chicken_loc_lists.popleft()
  min_dist=0

  for house in house_loc:
    min_candidate = list()
    for chicken in cur_chicken_loc:
      min_candidate.append(sum([abs(i-j) for i,j in zip(house,chicken)]))
      print('current chicken house location : ',cur_chicken_loc)
      print('current house location : ',house)
      print(min_candidate)
    min_dist += min(min_candidate)
      
  if min_dist < chicken_dist:
    chicken_dist = min_dist

print(chicken_dist)

