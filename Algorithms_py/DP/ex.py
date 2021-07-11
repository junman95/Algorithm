import time

start = time.time()

def fibo(x):
  if x == 1  or x == 2:
    return 1
  
  #아직 계산하지 않았다면 피보나치 반환
  else: 
    return fibo(x-1) + fibo(x-2)
  


print(fibo(37))
end = time.time() - start

print(end)