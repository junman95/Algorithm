import sys

N,S = map(int,input().split())
A = list(map(int,sys.stdin.readline().rstrip().split()))

end = 0
interval_sum=0
ans_candidates = list()
for start in range(N):
  while interval_sum<S and end<N:
    interval_sum+=A[end]
    end+=1
  if interval_sum >= S:
    ans_candidates.append(end-start)
    interval_sum-=A[start]

if ans_candidates:
  print(min(ans_candidates))
else:
  print(0)