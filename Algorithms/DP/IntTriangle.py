#맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
# 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
import sys
n = int(input())

triangle = list()
dp_table = list()

for i in range(n):
  triangle.append(list(map(int,sys.stdin.readline().rstrip().split())))
  dp_table.append([0]*(i + 1))
print(dp_table)

def maxPath():
  for i in range(n,0,-1):
    cur_floor = i-1
    #맨 아랫층 깔아주기
    if i == len(triangle):
      print(triangle[cur_floor])
      dp_table[cur_floor] = triangle[cur_floor]
    #바텀업으로 현재 인덱스의 이전층 좌우 대소비교 + 현재인덱스 값
    else:
      for idx in range(len(triangle[cur_floor])):
        cur_element = triangle[cur_floor][idx]
        dp_table[cur_floor][idx] = max(dp_table[cur_floor+1][idx],dp_table[cur_floor+1][idx+1])+cur_element


maxPath()
print(dp_table[0][0])