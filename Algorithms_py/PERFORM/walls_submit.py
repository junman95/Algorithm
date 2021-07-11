from itertools import combinations
from collections import deque

n = int(input())
n_list = list(i for i in range(n))
weak = list(map(int,input().split()))
dist = list(map(int,input().split()))


def possible(combi_list,weak):
  biggest_combi = tuple()
  for cur_combi in combi_list:
    if sum(cur_combi)>sum(biggest_combi):
      biggest_combi = cur_combi

  for start_wall in weak:
    temp_list = deque(n_list)
    temp_weak = deque(weak)
    for idx in biggest_combi:
      for i in range(start_wall):
        temp_list.append(temp_list.popleft())
      for i in range(idx+1):
        cur_pos = temp_list.popleft()
        for j in weak:
          if cur_pos == j:
            temp_weak.remove(j)
            if not temp_weak:
              return True

  return False

for i in range(1,len(dist)+1):
  friends_combi = list(combinations(dist,i))
  print(friends_combi)

  if possible(friends_combi,weak) == True:
    break

#테스트 케이스 통과