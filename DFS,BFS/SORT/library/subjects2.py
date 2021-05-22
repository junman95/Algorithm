n = int(input())
array = [tuple(input().split(' ')) for _ in range(n)]

def sortingFunc(student):
  return student[1]


array = sorted(array,key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in array:
  print(i[0],end=" ")