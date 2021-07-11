user_id1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id1 = ["fr*d*", "abc1**"]
# 2
user_id2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id2 = ["*rodo", "*rodo", "******"]
                #[[frod ][   crodo ][  abc123 frodoc]]
# 2
user_id3 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id3 = ["fr*d*", "*rodo", "******", "******"]
# 3

from itertools import product


def solution(user_id, banned_id):
    finished = False
    candidate_list = [[] for _ in range(len(banned_id))]
    print(candidate_list)
    counter = len(banned_id)
    while not finished:

        for ban_idx in range(len(banned_id)):
            cur_candits=len(candidate_list[ban_idx]) if candidate_list[ban_idx] else 0
            for user in user_id:
                cur_stat = True
                print(counter)
                if len(banned_id[ban_idx]) == len(user):
                    for i in range(len(banned_id[ban_idx])):
                        if banned_id[ban_idx][i] != user[i]:
                            if banned_id[ban_idx][i] == "*":
                                continue
                            else:
                                cur_stat = False
                                break
                    if cur_stat == True:
                        candidate_list[ban_idx].append(user)
                        user_id.remove(user)
                        cur_stat = False
                        break
            print(candidate_list)
            if cur_candits == len(candidate_list[ban_idx]):
                counter -= 1
        if counter < 1:
            finished=True
    print(candidate_list)
    answer = list(product(*candidate_list))
    answer = set(tuple(answer))
    print(answer)
    return answer


solution(user_id2, banned_id2)
