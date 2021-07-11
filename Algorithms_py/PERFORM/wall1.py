from itertools import combinations,permutations
from collections import deque

def possible(combi_list,weak,n_list):
    biggest_combi = tuple()
    for cur_combi in combi_list:
        if sum(cur_combi)>sum(biggest_combi):
            biggest_combi = cur_combi
        
    permu_list = list(set(permutations(biggest_combi,len(biggest_combi))))
    for cur_combi in permu_list:
        print(cur_combi)
        for start_wall in weak:
            temp_list = deque(n_list)
            temp_weak = deque(weak)
            for i in range(start_wall):
                temp_list.append(temp_list.popleft())
            for idx in cur_combi:
                for i in range(idx+1):
                    if temp_list:
                        cur_pos = temp_list.popleft()
                        for j in weak:
                            if cur_pos == j:
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

def solution(n, weak, dist):
    n_list = list(i for i in range(n))
    for i in range(1,len(dist)+1):
        friends_combi = list(combinations(dist,i))

        if possible(friends_combi,weak,n_list) == True:
            return i
        
    return -1

list_a = [1,1,1,1,1,1,1,1]
list_b = [3, 5, 7, 50, 70, 10, 199, 105]
print(list_a,list_b)
print(solution(200,list_b,list_a))