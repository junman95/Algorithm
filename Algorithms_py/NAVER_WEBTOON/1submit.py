#     악성 코드가 전산망에 침투하는지 감시하기 위해 패킷에서 알파벳으로만 이루어진 문자열 S를 분리했습니다. 그다음 문자열 S에 아래 설명에 해당하는 문자열 pattern이 포함돼 있다면 해당 패킷을 악성코드 의심 패킷으로 분류하려 합니다.

# 문자열 S에 특정 문자열 pattern이 포함돼 있다면 악성코드를 전송하는 패킷으로 분류합니다.
# 악성코드는 pattern을 무작위로 섞은 다음 문자열 S에 숨겨 전송합니다.
# 따라서, 문자열 S에 재배열해서 문자열 pattern을 만들 수 있는 부분 문자열이 포함돼 있다면 악성코드 의심 패킷으로 분류해야 합니다. 부분 문자열은 어떤 문자열의 연속된 일부를 의미합니다.
# 먼저 문자열 S에서 재배열하여 pattern을 만들 수 있는 부분 문자열이 모두 몇 개인지 구하려 합니다. 같은 부분 문자열이라도 위치가 다르다면 따로 세어야 합니다.

# 문자열 S와 pattern이 매개변수로 주어질 때, 문자열 S에서 재배열하여 pattern을 만들 수 있는 부분 문자열은 모두 몇 개인지를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 문자열 S의 길이는 1 이상 1,000 이하입니다.
# 문자열 pattern의 길이는 1 이상 8 이하입니다(S 길이가 8 이하인 경우 S의 길이 이하).
# 문자열 S와 pattern은 알파벳 소문자로만 이루어져 있습니다.
# 입출력 예
# S	pattern	result
# "tegsornamwaresomran"	"ransom"	2
# "wreawerewa"	"ware"	4
# "ababababababa"	"aabba"	5
# "abcde"	"edcba"	1
# "aabbccddee"	"abcde"	0
# "aaaaaa"	"a"	6
# 입출력 예 설명
# 입출력 예 #1

# 재배열해서 "ransom"을 만들 수 있는 부분 문자열은 다음과 같이 두 가지가 있습니다.

# tegsornamwaresomran
# tegsornamwaresomran
# 입출력 예 #2

# 재배열해서 "ware"를 만들 수 있는 부분 문자열은 다음과 같이 네 가지가 있습니다.

# wreawerewa
# wreawerewa
# wreawerewa
# wreawerewa


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