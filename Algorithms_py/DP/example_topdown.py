#
# MEMOIZATION
# 1. 큰 문제를 작은문제로 나눌 수 있다
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
#

import time

start = time.time()
#메모이제이션 리스트
d = [0] * 1000

def fibo(x):
  if x == 1  or x == 2:
    return 1
  #계산 한 적있는 문제라면 반환
  if d[x] != 0:
    return d[x]
  
  #아직 계산하지 않았다면 피보나치 반환
  d[x] = fibo(x-1) + fibo(x-2)
  return d[x]

print(fibo(99))
end = time.time() - start
print("실행 시간 : ",end)