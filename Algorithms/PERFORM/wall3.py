from itertools import combinations,permutations
from collections import deque

def possible(permu_list,weak,n_list):
    min_count = len(n_list)+1
    pivot = len(permu_list[0])
    for cur_permu in permu_list:
        for start_wall in weak:
            temp_list = deque(n_list)
            temp_weak = deque(weak)
            count = 0 
            for i in range(start_wall):
                temp_list.append(temp_list.popleft())
            for idx in cur_permu[0:pivot]:
                count += 1
                for i in range(idx+1):
                    if temp_list:
                        cur_pos = temp_list.popleft()
                        for j in weak:
                            if cur_pos == j:
                                temp_weak.remove(j)
                                if not temp_weak:
                                    if min_count > count:
                                      min_count = count
                                      pivot = count

                while temp_list:
                    stat = False
                    for cur_weak in temp_weak:
                        if cur_weak == temp_list[0]:
                            stat = True
                            break
                    if stat == True:
                        break
                    temp_list.popleft()
    if min_count == len(n_list)+1:
        return -1
    else:
        return min_count

def solution(n, weak, dist):
    n_list = list(i for i in range(n))
    friends_permu = list(set(permutations(dist)))

    print(possible(friends_permu,weak,n_list))


solution(12,[1,5,6,10],[1,2,3,4])