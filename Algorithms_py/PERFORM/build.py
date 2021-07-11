#build_frame = [x,y,a,b]
#x,y : 교차점 좌표
#a : 구조물 종류 ( 0 : 기둥, 1 : 보 )
#b : 설치,삭제 ( 0 : 설치, 1 : 삭제 )
# 기둥 : 교차점 위로 설치
# 보 : 교차점 우측으로 설치
from collections import deque

n = int(input())
N=n+1
build_frame = deque(list(list(map(int,input().split())) for _ in range(10)))

build_map = list([2]*N for _ in range(N))


def order_stack(cur_order):
  x = cur_order[0]
  y = cur_order[1]
  action = cur_order[3]
  print("기둥",x,y)

  if 0 <= x < N and 0 <= y < N-1: # 기둥바닥부터 재므로
    if action == 0: #삭제
      if build_map[x][y] == 0: #위쪽의 기둥, 위쪽의 좌우측 보가 있을경우 삭제 x
        if y+1 < N-1 and build_map[x][y+1] == 0: #기둥이 꼭대기가 아니고 위에 기둥이 있을경우
          print("here1",x,y)
          build_map[x][y] = 0
        elif x < N-1 and build_map[x][y+1] == 1: #기둥이 우측끝이 아니고 우측우로 보가 있을경우 + 우측보의 지지기둥이 또 없을경우
          print("here2",x,y)
          if build_map[x+1][y+1] == 1:
            print("this1")
            build_map[x][y]=2
          elif build_map[x+1][y] != 0:
            print("this2")
            build_map[x][y]=2
          else:
            print("this3")
            build_map[x][y] = 0
        elif 0 < x and build_map[x-1][y+1] == 1: #기둥이 좌측끝이 아니고 좌측우로 보가 있을경우 + 죄측보의 지지기둥이 또 없을경우
          print("here3",x,y)
          if 1< x and build_map[x-2][y+1] == 1: #보옆에 보이면 삭제가능
            build_map[x][y] = 2
          elif build_map[x-1][y] == 0:
            build_map[x][y] = 2
          else:
            build_map[x][y] = 0
        else:
          build_map[x][y] = 2
    
    elif action == 1: #설치
      if y == 0: #바닥일경우
        build_map[x][y] = 0
      elif y !=0 and build_map[x][y-1] == 0: #아래에 기둥이 있을경우
        build_map[x][y] = 0
      elif y !=0 and build_map[x-1][y] == 1: #왼쪽아래에 보가 있을경우
        build_map[x][y] = 0
      elif y !=0 and build_map[x][y] == 1: #오른쪽아래에 보가 있을경우
        build_map[x][y] = 0

def order_floor(cur_order):
  x = cur_order[0]
  y = cur_order[1]
  action = cur_order[3]
  print("보",x,y)

  if action == 0: #삭제
    if x<N-2 and build_map[x+1][y] == 1 and build_map[x+2][y] == 1:#보의 오른쪽과 그오른쪽이 보일경우 조건 x ->무시
      build_map[x][y] = 1
    elif 1<x and build_map[x-1][y] == 1 and build_map[x-2][y] == 1:#보의 오른쪽과 그오른쪽이 보일경우 조건 x ->무시
      build_map[x][y] = 1
    elif build_map[x][y] == 0:#보 왼쪽위 기둥일경우
      if 1<x and build_map[x-1][y] != 1: #보 왼쪽에 보가 없을경우
        build_map[x][y] = 1
    elif build_map[x][y+1] == 0:#보 오른쪽위 기둥일경우
      if x<N-2 and build_map[x+1][y] != 1: #보 왼쪽에 보가 없을경우
        build_map[x][y] = 1
    else:
      build_map[x][y] = 2
  elif action == 1: #설치
    if build_map[x][y-1] == 0 or build_map[x+1][y-1] == 0:#보의 좌우측아래에 기둥이 있는경우
      build_map[x][y] = 1
    elif 0 < x < N-2 and build_map[x-1][y] == 1 and build_map[x+1][y] == 1: #보의 좌우측에 보가있을경우
      build_map[x][y] = 1


while(build_frame):
  order = build_frame.popleft()
  #기둥과 보의 분리
  if order[2] == 0:
    order_stack(order)
  elif order[2] == 1:
    order_floor(order)
  
  print("현재 절차 : " , order)
  for i in range(N):
    print(build_map[i])

ans_list = list()
for i in range(N):
    for j in range(N):
      if build_map[i][j] != 2:
        x, y, a = i, j, build_map[i][j]
        
        ans = [x,y,a]
        ans_list.append(ans)

print(ans_list)