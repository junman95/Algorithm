# 상하좌우
import sys

N = sys.stdin.readline().rstrip()
direction = list(sys.stdin.readline().rstrip().split(' '))

x_pos,y_pos = 1, 1
x_start,x_end,y_start,y_end=1,5,1,5
current_move = 0

def movePos(cur_xpos,cur_ypos,cur_direction):
  print(cur_direction)
  if(cur_direction == "L"):
    if(cur_xpos>1):
      cur_xpos-=1
  elif(cur_direction == "R"):
    if(cur_xpos<5):
      cur_xpos+=1
  elif(cur_direction == "U"):
    if(cur_ypos>1):
      cur_ypos-=1
  elif(cur_direction == "D"):
    if(cur_ypos<5):
      cur_ypos+=1
  
  return cur_xpos,cur_ypos

for i in direction:
  print(y_pos," ",x_pos)

  x_pos,y_pos=movePos(x_pos,y_pos,i)

print(y_pos," ",x_pos)
