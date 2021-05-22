

array = [1,3,5,7,9,11,13,15,17,19]

def binary_search(array,target,start_idx,end_idx):
  while(start_idx<=end_idx):
    mid_idx = (start_idx+end_idx)//2
    print("current mid idx : ",mid_idx)
    if array[mid_idx] < target:
      start_idx=mid_idx+1
      print("change start idx : ",start_idx)
    elif array[mid_idx] > target:
      end_idx=mid_idx-1
      print("change end idx : ",end_idx)
    else:
      return mid_idx
    
  return "찾으시는 원소가 없습니다!"


print(binary_search(array,17,0,len(array)-1))