import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
apples = deque(list(sys.stdin.readline().rstrip().split() for _ in range(K)))
for i in range(K):
  apples[i] = list(map(int,apples[i]))
  
L = int(sys.stdin.readline().rstrip())
#D = 오른쪽 / L = 왼쪽
rotations = deque(list(sys.stdin.readline().rstrip().split() for _ in range(L)))
for i in range(L):
  rotations[i][0] = int(rotations[i][0])
#맵초기화
game_map = list(list([0]*N) for _ in range(N))
for i in range(len(game_map)):
  for j in range(len(game_map[i])):
    for k in range(len(apples)):
      if apples[k][0]-1 == i and apples[k][1]-1 == j:
        game_map[i][j] = 1


def moveDummy(dummy,direction):
  dummy_head = dummy[0]
  if -1<dummy_head[0]<N and -1<dummy_head[1]<N:
    if direction == 'Right':
      dummy.insert(0,[dummy_head[0],dummy_head[1]+1])
      if game_map[dummy_head[0]][dummy_head[1]] != 1:
        for idx in range(1,len(dummy)):
          if dummy[0] == dummy[idx]:
            return False
        dummy.pop()
      else:
        game_map[dummy_head[0]][dummy_head[1]] = 0
    elif direction == 'Down':
      dummy.insert(0,[dummy_head[0]+1,dummy_head[1]])
      if game_map[dummy_head[0]][dummy_head[1]] != 1:
        for idx in range(1,len(dummy)):
          if dummy[0] == dummy[idx]:
            return False
        dummy.pop()
      else:
        game_map[dummy_head[0]][dummy_head[1]] = 0
    elif direction == 'Left':
      dummy.insert(0,[dummy_head[0],dummy_head[1]-1])
      if game_map[dummy_head[0]][dummy_head[1]] != 1:
        for idx in range(1,len(dummy)):
          if dummy[0] == dummy[idx]:
            return False
        dummy.pop()
      else:
        game_map[dummy_head[0]][dummy_head[1]] = 0
    elif direction == 'Up':
      dummy.insert(0,[dummy_head[0]-1,dummy_head[1]])
      if game_map[dummy_head[0]][dummy_head[1]] != 1:
        for idx in range(1,len(dummy)):
          if dummy[0] == dummy[idx]:
            return False
        dummy.pop()     
      else:
        game_map[dummy_head[0]][dummy_head[1]] = 0
  
  dummy_head = dummy[0]
  if -1<dummy_head[0]<N and -1<dummy_head[1]<N:
    return True
  else:
    return False
    
dummy = deque([[0,0]])
directions = deque(['Right','Down','Left','Up'])
gameplay=True
count = 0 
while(gameplay):
  if rotations:
    if count == rotations[0][0]:
      if rotations[0][1] == 'L':
        directions.insert(0,directions.pop())
      elif rotations[0][1] == 'D':
        directions.insert(3,directions.popleft())
      rotations.popleft()
  count += 1
  if moveDummy(dummy,directions[0]) == False:
    gameplay=False
print(count)
