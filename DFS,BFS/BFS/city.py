from collections import deque
from collections import defaultdict
# n:도시수 m:도로수 k:검색거리 x:출발도시

hihi = defaultdict(list)

n, m, k, x = map(int, input().split())

graph = []

visited = [False] * n
for i in range(m):
    graph.append(list(map(int, input().split())))

# 1->3 [1,3]
# dict를 써라~
#graph[1] = [2, 3]
#graph[a].append(b)
# [1,2]
# [1,3]
# [2,3]
# [2,4]
# 
#


def city():
    # 변수명 보기편하게
    taken_path = 0
    start_city = [x,taken_path]
    num_road = m
    answer_city = []
    visited[start_city[0] - 1] = True
    queue = deque([start_city])
    
    while queue:
    
        current_city = queue.popleft()
        
        taken_path+=1

        for i in range(num_road):

            if graph[i][0] == current_city[0] and visited[graph[i][1] - 1] == False:
                queue.append([graph[i][1],taken_path])
                visited[graph[i][1] - 1] = True
                if taken_path == k:
                    answer_city.append(graph[i][1])


    if answer_city != []:
        for i in answer_city:
            print(i,end=" ")
    else:
        print('-1')
##################################################
#run#

city()