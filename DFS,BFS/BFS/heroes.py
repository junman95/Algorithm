import sys
N, K = map(int,sys.stdin.readline().rstrip().split(' '))
players = []
for _ in range(N):
  players.append(int(sys.stdin.readline().rstrip()))

players.sort();

def binary(array,K,start_idx,end_idx,prev_area):
  mid_idx = (start_idx+end_idx)//2
  #print("mid_idx: ",mid_idx," start_idx: ",start_idx," end_idx: ",end_idx)
  fill_area=((mid_idx+1)*array[mid_idx])-sum(array[:mid_idx+1])
  if(start_idx>end_idx):
    return mid_idx;
  
  if (fill_area<K):
    start_idx=mid_idx+1;
    return binary(array,K,start_idx,end_idx,fill_area)
  elif (fill_area>K):
    end_idx=mid_idx-1;
    return binary(array,K,start_idx,end_idx,fill_area)
  elif(fill_area ==K):
    return mid_idx;




answer_idx=binary(players,K,0,len(players)-1,len(players)*players[-1])

rest_K=K-((answer_idx+1)*players[answer_idx]-sum(players[:answer_idx+1]))
answer = int(rest_K/(answer_idx+1))+players[answer_idx]

print(answer)
