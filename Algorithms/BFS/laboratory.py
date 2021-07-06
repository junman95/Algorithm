
# virus = [] / block = [] / 
# 1. 벽을 세울수있는 조합의 경우를 구한다
# 2. 바이러스가 퍼져나가는 BFS 알고리즘으로 최적결과를 도출한다.

from collections import deque
# 2:바이러스 1:벽 0:통로
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def laboratory():
  queue = duque()