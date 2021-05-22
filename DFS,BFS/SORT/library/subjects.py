n = int(input())
array = [(input().split(' ')) for _ in range(n)]

def sortingFunc(student):
  return student[1]


array = sorted(array,key=sortingFunc,reverse=True)
print(array)

temp = []
for i in range(len(array)-1):
  if array[i][1] == array[i+1][1]:
    temp.append(array[i])
if array[-2][1] == array[-1][1]:
  temp.append(array[-1])
print(temp)
temp = sorted(temp,key = lambda x:x[2])

print(temp)