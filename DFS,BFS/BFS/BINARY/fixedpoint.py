import sys

N = sys.stdin.readline().rstrip()
array = list(map(int,sys.stdin.readline().rstrip().split(' ')))


def binary(array,start_idx,end_idx):
  mid_idx = (start_idx+end_idx)//2;

  if(start_idx>end_idx):
    return -1

  if(array[mid_idx]>mid_idx):
    end_idx = mid_idx-1;
    return binary(array,start_idx,end_idx);
  elif(array[mid_idx]<mid_idx):
    start_idx = mid_idx+1;
    return binary(array,start_idx,end_idx);
  else:
    return mid_idx;
  
print(binary(array,0,len(array)-1))
