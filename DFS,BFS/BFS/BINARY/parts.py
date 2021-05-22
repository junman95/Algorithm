import sys

N = sys.stdin.readline().rstrip()
N_list = list(sys.stdin.readline().rstrip().split(' '))
M = sys.stdin.readline().rstrip()
M_list = list(sys.stdin.readline().rstrip().split(' '))


print(N,N_list,M,M_list)

N_list.sort()

def binary(array,target,start_idx,end_idx):
  mid_idx = (start_idx+end_idx)//2
  if(start_idx>end_idx):
    return "NO"
  
  if(array[mid_idx]<target):
    start_idx=mid_idx+1
    return binary(array,target,start_idx,end_idx)
  elif(array[mid_idx]>target):
    end_idx=mid_idx-1
    return binary(array,target,start_idx,end_idx)
  else:
    return "YES"

for i in M_list:
  print(binary(N_list,i,0,len(N_list)-1),end=" ")