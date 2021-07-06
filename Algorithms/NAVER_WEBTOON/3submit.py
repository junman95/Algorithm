# 문제 설명
# 문자열에서 문자를 k개를 선택해 순서를 유지하며 이어 붙여 사전 순으로 가장 뒤에 오는 문자열을 만들려 합니다.

# 문자열 letters와 숫자 k가 매개변수로 주어집니다. letters에서 문자를 k개 선택해 순서를 유지하며 이어 붙여 만들 수 있는 문자열 중 사전 순으로 가장 뒤에 오는 것을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# letters의 길이는 1 이상 500,000 이하입니다.
# letters는 알파벳 소문자로만 이루어져 있습니다.
# k는 1 이상 letters의 길이 이하인 자연수입니다.
# 입출력 예
# letters	k	return
# "zbgaj"	3	"zgj"
# 입출력 예 설명
# 입출력 예 #1

# 사전 순으로 가장 뒤에 오는 문자열은 첫 번째, 세 번째, 다섯 번째 문자열을 선택해 이어 붙인 "zgj"입니다.



def solution(letters, k):
    answer = list()

    letter_list = list(letters)
    letter_list.sort()
    letter_list = letter_list[-1:-k-1:-1]
    for idx in letter_list:
        for i in range(len(letters)):
            if idx == letters[i]:
                answer.append((i,idx))
                break
    
    answer.sort(key= lambda x:x[0])
    ans_str= ''
    for i in range(len(answer)):
        ans_str += answer[i][1]

    return ans_str