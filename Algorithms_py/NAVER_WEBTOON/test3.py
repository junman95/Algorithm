# letters = 1~500000
# 소문자로만
# 1~k~letters

input1 = "acdbezzzz"
input2 = 9

def solution(letters, k):
    answer = list()

    #letter_enum = enumerate(letters)
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


print(solution(input1,input2))