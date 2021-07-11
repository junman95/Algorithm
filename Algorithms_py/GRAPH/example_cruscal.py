

def find_parent(parent,x):
  #루트노드가 아니면 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a<b:
    parent[b] =a
  else:
    parent[a]=b

v, e = map(int,input().split())
parent = [0]*(v+1)

edges = []
result =0

for i in range(1,v+1):
  parent[i]=i

