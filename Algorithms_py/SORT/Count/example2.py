array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
array2 =[0]*(max(array)+1)

for i in range(len(array)):
  array2[array[i]] +=1

for i in range(len(array2)):
  for j in range(array2[i]):
      print(i,end=" ")
