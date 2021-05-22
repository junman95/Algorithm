array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
array2 =[0]*len(array)

for i in range(max(array)+1):
  for j in array:
    if j==i:
      array2[i] +=1
      print(i,end=" ")
