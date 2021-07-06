S = "tegsornamwaresomran" 
pattern =	"ransom"
# "wreawerewa"	"ware"	4
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
            print(count)
            checker = 1
            cur_pattern_list = copy.deepcopy(pattern_list)
            cur_pattern_list.remove(cur_pattern_list[0])
            for idx in cur_pattern_list:
                pin1 = count-len(pattern_list) if count-len(pattern_list)>0 else 0
                pin2 = count+len(pattern_list) if count+len(pattern_list)<len(S) else len(S)

                print(pin1,pin2)
                for i in range(pin1,pin2):
                    if idx == S_list[i] and checker<len(pattern_list):
                        checker +=1

            print(checker)
            if checker == len(pattern_list):
                answer+=1

        count += 1
    return answer

print(solution(S,pattern))
