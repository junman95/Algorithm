import time

start = time.time()
#DP table
#탑다운의 메모이제이션과 비슷한 역할을 하나 이름이 구분됨
d = [0]*100

d[1] = 1
d[2] = 1


def fibo(x):
  for i in range(3,x+1):
    d[i] = d[i-1] + d[i-2]
  return d[x]

print(fibo(99))
end = time.time() - start
print("실행 시간 : ",end)