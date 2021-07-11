M = int(input())
key = list(list())
for i in range(M):
  key.append(list(input().split()))

N = int(input())
lock = list(list())
for i in range(N):
  lock.append(list(input().split()))

  a = [1]
  b = [0,1,1]

  c = a+b

  print(c)# [1, 1, 1]
cur_key = list(['0','0','0'] for _ in range(M))

keys = list([] for  _ in range((M*2-1)*(M*2-1))) # 키들의 조합
print(keys)
def getKeys(key):
  for idx in range((M*2-1)*(M*2-1)):
    for i in range(M):
      for j in range(M):
        
      # if row<=M and col<=M:
      #   for x in range(row):
      #     for y in range(col):
      #       cur_key[x][y]=key[x][y]
      #   print(cur_key)
      
      # elif row<=M and col>M:
      #   print("now : ",row,col)
      #   for x in range(row):
      #     for y in range(col):
      #       if col-y <M:
      #         cur_key[x][y]=key[x][col-y]
      #   print(cur_key)

getKeys(key)