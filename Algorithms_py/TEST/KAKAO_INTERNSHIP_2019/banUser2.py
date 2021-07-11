user_id1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]	
banned_id1 = ["fr*d*", "abc1**"]	
#2
user_id2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id2 = ["*rodo", "*rodo", "******"]	
# candidate = [crodo frodo][crodo frodo][abc123 frodoc]

#2
user_id3 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]	
banned_id3 =["fr*d*", "*rodo", "******", "******"]	
#3

from itertools import product
from collections import deque
import copy

def solution(user_id, banned_id):
    banned_list = []
    for idx in banned_id:
        banned_list.append([idx[i] for i in range(len(idx))])
    cur_stat = True
    candidate_list=[]
    for ban in banned_list:
        temp_list = []
        for user in user_id:
            if len(ban) == len(user):
                for i in range(len(ban)):
                    if ban[i] != user[i]:
                        if ban[i] =='*':
                            continue
                        else:
                            cur_stat=False
                            break
                if cur_stat:
                    temp_list.append(user)
                cur_stat=True
        candidate_list.append(temp_list)
    answer = list(product(*candidate_list))
    finished = False
    temp_ans = copy.deepcopy(answer)
    for i in answer:
        if len(set(i)) != len(i):
            temp_ans.remove(i)

    print(temp_ans)
    
    temp_temp_ans = []
    # for i in range(len(temp_ans)):
    #     print(temp_ans[i])

    #     temp_temp_ans.append(set(temp_ans[i]))

    for i in range(len(temp_ans)):
        temp_ans[i] = tuple(sorted(temp_ans[i]))
    print(len(set(tuple(temp_ans))))
    return answer



solution(user_id2,banned_id2)