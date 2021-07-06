input1 = "AAAAE"
input2 = "AAAE"
input3 = "I"
input4 = "EIO"

from itertools import permutations
def solution(word):
    alphabet = ['A','E','I','O','U']

    word_set = list(permutations(alphabet))
    word_set.sort()
    print(word_set)    
    answer = 0
    return answer

solution(input1)