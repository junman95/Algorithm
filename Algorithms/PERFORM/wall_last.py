from itertools import combinations, permutations
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
  print(biggest_combi)
  for start_wall in weak:
    temp_list = deque(n_list)
    temp_weak = deque(weak)
    for i in range(start_wall):
      temp_list.append(temp_list.popleft())
    for idx in biggest_combi:
      print(idx, temp_list)
      print(temp_weak)
      for i in range(idx+1):
        if temp_list:
          cur_pos = temp_list.popleft()
          for j in weak:
            if cur_pos == j:
              if cur_pos>159:
                print("look here : " ,temp_list)
                print(temp_weak)
              temp_weak.remove(j)
              if not temp_weak:
                return True
      
      while temp_list:
        stat = False
        for cur_weak in temp_weak:
          if cur_weak == temp_list[0]:
            stat = True
            break
        if stat == True:
          break
        temp_list.popleft()

  return False

for i in range(1,len(dist)+1):
  friends_combi = list(permutations(dist,i))
  print(friends_combi)
  print("-----------------------------------------------")
  if possible(friends_combi,weak) == True:
    print(i)
    break

#테스트 케이스 통과