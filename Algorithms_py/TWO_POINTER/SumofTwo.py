import sys

N,M = map(int,input().split())
A = list(map(int,sys.stdin.readline().rstrip().split()))

end = 0
interval_sum=0
count = 0
for start in range(N):
  while interval_sum<M and end<N:
    interval_sum+=A[end]
    end+=1
  
  if interval_sum == M:
    count+=1
  
  interval_sum-=A[start]

print(count)