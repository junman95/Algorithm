n=5
m=5
data = [1,2,3,2,5]

def twoPointerSum(data,sum_partial):
  a_idx,b_idx = 0, 0
  pointer_a,pointer_b = data[0],data[0]
  counter = 0
  while(True):
    try:
      if sum(data[a_idx:b_idx+1]) == sum_partial:
        counter+=1
      
      if sum(data[a_idx:b_idx+1]) < sum_partial:
        b_idx += 1
        pointer_b = data[b_idx]
      else:
        a_idx += 1
        pointer_a = data[a_idx]
        
    except IndexError as e:
      print(e)
      break

  return counter


print(twoPointerSum(data,m))