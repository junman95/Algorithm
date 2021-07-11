#X가 3으로 나누어 떨어지면, 3으로 나눈다.
#X가 2로 나누어 떨어지면, 2로 나눈다.
#1을 뺀다.
#정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

N = int(input())
memo = [0] * (N+1)
memo[1] = 0
def makeOne(x):
  for idx in range(2,x+1):
    temp_div3, temp_div2 , temp_sub1 = 0,0,0
    if idx>=3 and idx%3 == 0:
      temp_div3 = memo[idx//3]+1
    if idx>=2 and idx%2 == 0:
      temp_div2 = memo[idx//2]+1
    
    temp_sub1 = memo[idx-1]+1

    min_candidates = list()
    min_candidates.append(temp_sub1)
    if temp_div2 != 0:
      min_candidates.append(temp_div2)
    if temp_div3 != 0:
      min_candidates.append(temp_div3)
    memo[idx] = min(min_candidates)
  
  return memo[N]

print(makeOne(N))