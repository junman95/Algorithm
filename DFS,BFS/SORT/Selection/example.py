array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  for j in range(i+1,len(array)):
    if array[i] > array[j]:
      array[i],array[j] = array[j],array[i]

  print(array)

