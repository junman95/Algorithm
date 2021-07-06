import sys
N,C = map(int,sys.stdin.readline().rstrip().split(' '));
house_loc=[]
for i in range(N):
  house_loc.append(int(sys.stdin.readline().rstrip()));

house_loc.sort();

print(house_loc);
average_dist=house_loc[-1]//C;

def binary(array,C,target_dist,start_idx,end_idx):
  mid_idx = (start_idx+end_idx)//2;

  if array[end_idx]-array[start_idx]>=C:
    if array[mid_idx]-array[start_idx]>=C:
      r_start_idx=mid_idx;
      r_end_idx=end_idx;
      l_start_idx=start_idx;
      l_end_idx=mid_idx;