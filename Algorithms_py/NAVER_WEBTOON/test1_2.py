# S = "tegsornamwaresomran" 
# pattern =	"ransom"
S="wreawerewa"	
pattern = "ware"	#4
# "ababababababa"	"aabba"	5
# "abcde"	"edcba"	1
# "aabbccddee"	"abcde"	0
# "aaaaaa"	"a"	6

import copy

def solution(S, pattern):
    S_list = list(S)
    pattern_list = list(pattern)
    answer = 0
    count = 0
    while count<len(S):
        if S_list[count] == pattern_list[0]:
            checker = 1

            pin1 = count-len(pattern_list) if count-len(pattern_list)>0 else 0
            pin2 = count+len(pattern_list) if count+len(pattern_list)<len(S) else len(S)

            for start in range(pin1,count+1):
                cur_pattern_list = copy.deepcopy(pattern_list)
                cur_pattern_list.remove(cur_pattern_list[0])
                if start+len(pattern)<=len(S):
                    for i in range(start,start+len(pattern_list)):

                        for j in cur_pattern_list:
                            if S_list[i] == j:
                                checker+=1
                                cur_pattern_list.remove(j)
                                print(cur_pattern_list)
                    if not cur_pattern_list:
                        print(S_list[start],start)
                        answer+=1

        count += 1
    return answer

print(solution(S,pattern))
