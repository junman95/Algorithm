import sys

N,x =map(int,sys.stdin.readline().rstrip().split(' '))
array = list(map(int,sys.stdin.readline().rstrip().split(' ')))
def binary(array,target,start_idx,end_idx):
  # 이진탐색으로 내가원하는 target값을 찾는다
  while(start_idx<=end_idx):
    mid_idx = (start_idx+end_idx)//2;
    if(array[mid_idx]<target):
      start_idx=mid_idx+1;
    elif(array[mid_idx]>target):
      end_idx=mid_idx-1;
    else:
      break;
  # 없으면 -1
  if(start_idx>end_idx):
    return "-1";
  #타겟값을 기준으로 왼쪽
  l_start_idx,l_end_idx=start_idx,mid_idx;
  
  while(l_start_idx<=l_end_idx):

    l_mid_idx=(l_start_idx+l_end_idx)//2;
    if(array[l_mid_idx]<target):
      l_start_idx=l_mid_idx+1;
    elif(array[l_mid_idx]>target):
      l_end_idx=l_mid_idx-1;
    elif(array[l_mid_idx]==target and array[l_mid_idx-1]==target):
      l_end_idx=l_mid_idx-1;
    else:
      break;

  r_start_idx,r_end_idx=mid_idx,end_idx;

  while(r_start_idx<=r_end_idx):
    r_mid_idx=(r_start_idx+r_end_idx)//2;
    if(array[r_mid_idx]<target):
      r_start_idx=r_mid_idx+1;
    elif(array[r_mid_idx]>target):
      r_end_idx=r_mid_idx-1;
    elif(array[r_mid_idx]==target and array[r_mid_idx+1]==target):
      r_start_idx=r_mid_idx+1;
    else:
      break;
  #이부분이 계산이안돼요.
  while(True):
    print("left_idx : ",left_idx,"right_idx",right_idx);
    if(array[left_idx]==target):
      left_idx-=1;
    if(array[right_idx]==target):
      right_idx+=1;

    if(array[left_idx]!=target and array[right_idx]!=target):
      left_idx+=1;
      right_idx-=1;
      break;
  print("left_idx : ",left_idx,"right_idx",right_idx);
  print(r_mid_idx,l_mid_idx)
  return r_mid_idx-l_mid_idx+1;

print(binary(array,x,0,len(array)-1))
  