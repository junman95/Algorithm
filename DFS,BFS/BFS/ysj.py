from collections import deque
from itertools import permutations,combinations

N = int(input())
number_raw = list(map(int,input().split(' ')))
operators = list(map(int,input().split(' ')))

# 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷) : 0 1 2 3
operator_sets = list()
for i in range(4):
  for _ in range(operators[i]):
    operator_sets.append(i)
def ysj() :
  
  

  answer_min = 0
  answer_max = 0 
  for i in permutations(operator_sets,N-1):
    count = 0
    temp = number_raw[0]
    for j in i:
      if j == 0:
        count += 1
        temp += number_raw[count]
      elif j == 1:
        count += 1
        temp -= number_raw[count]
      elif j == 2:
        count += 1
        temp *= number_raw[count]
        temp = int(temp)
      elif j == 3:
        count += 1
        temp /= number_raw[count]
        temp = int(temp)
      #print(count)
    if answer_max == 0 and answer_min == 0:
      answer_max = temp
      answer_min = temp
    
    else:
      if answer_min > temp:
        answer_min = temp

      if answer_max < temp:
        answer_max = temp

  
  print(answer_max)
  print(answer_min)

ysj()
