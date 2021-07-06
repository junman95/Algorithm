from itertools import combinations,permutations,islice
from collections import deque

def possible(combi_list,weak,n_list):
    biggest_combi = tuple()
    for cur_combi in combi_list:
        if sum(cur_combi)>sum(biggest_combi):
            biggest_combi = cur_combi
        
    permu_list = list(set(permutations(biggest_combi,len(biggest_combi))))
    for cur_combi in permu_list:
        for start_wall in weak:
            print("start_wall",start_wall)
            temp_list = deque(n_list)
            temp_weak = deque(weak)
            for i in range(start_wall):
                temp_list.append(temp_list.popleft())
            for idx in cur_combi:
                flag = 0
                for i in range(idx+1):
                    if temp_list:
                        cur_pos = temp_list.popleft()
                        for j in range(len(weak)):
                            if cur_pos == weak[j]:
                                if weak[j] != weak[-1] and (weak[j+1] in temp_weak):
                                    print("len : ", weak[j+1]-weak[j])
                                    islice(temp_list,weak[j+1]-weak[j],len(temp_list))
                                    print('poss')
                                    flag=weak[j+1]
                                elif weak[0] in temp_weak:
                                    print("len : ", len(n_list)-weak[j]+weak[0])
                                    islice(temp_list,len(n_list)-weak[j]+weak[0],len(temp_list))
                                    print('notposs')
                                    flag=weak[0]
                                print(flag)
                                print("temp list :",temp_list)
                                print("temp weak :",temp_weak)
                                temp_weak.remove(weak[j])
                                if not temp_weak:
                                    return True

                # while temp_list:
                #     stat = False
                #     for cur_weak in temp_weak:
                #         if cur_weak == temp_list[0]:
                #             stat = True
                #             break
                #     if stat == True:
                #         break
                #     temp_list.popleft()
    return False

def solution(n, weak, dist):
    n_list = list(i for i in range(n))
    for i in range(1,len(dist)+1):
        friends_combi = list(combinations(dist,i))

        if possible(friends_combi,weak,n_list) == True:
            return i
        
    return -1

print(solution(20,[0,100],[1,1]))