import copy

def solution(S, pattern):
    S_list = list(S)
    pattern_list = list(pattern)
    answer = 0
    count = 0

    for start in range(len(S_list)):
        temp_pattern_list = copy.deepcopy(pattern_list)
        if start+len(pattern_list)<=len(S_list):
            for i in range(start,start+len(pattern_list)):
                for j in temp_pattern_list:
                    if S_list[i] == j:
                        temp_pattern_list.remove(j)
                        break
                    
                if not temp_pattern_list:
                    answer += 1
                    break
            
            temp_pattern_list.append(S_list[start])

    return answer