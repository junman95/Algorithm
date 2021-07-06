import sys

T=int(input())
golds = list()
for _ in range(T):
  n,m = map(int, input().split())
  golds = (list(map(int,sys.stdin.readline().rstrip().split())))

  gold_list = list([] for _ in range(m))
  for i in range(len(golds)):
    gold_list[i%m].append(golds[i])
  print(gold_list)

  dp_list = list([0]*n for _ in range(m))
  dp_list[0] = gold_list[0]
  print(dp_list)

  for i in range(1, m):
    for j in range(n):
      if j ==0:
        dp_list[i][j] = max(dp_list[i-1][j],dp_list[i-1][j+1]) + gold_list[i][j]
      elif j == n-1:
        dp_list[i][j] = max(dp_list[i-1][j-1],dp_list[i-1][j]) + gold_list[i][j]
      else:
        dp_list[i][j] = max(dp_list[i-1][j-1],dp_list[i-1][j],dp_list[i-1][j+1]) + gold_list[i][j]

  print(max(dp_list[m]))


