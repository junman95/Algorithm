knight = list(input().strip())

y_letter=['a','b','c','d','e','f']

for letter in y_letter:
  if knight[0] == letter:
    knight[0] = int(y_letter.index(letter))
    knight[1] = int(knight[1])


print(knight)

direction = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)]
count=0
for dir in direction:
  nx = knight[0] + dir[0]
  ny = knight[1] + dir[1]

  if nx<1 or nx>8 or ny<1 or ny>8:
    continue

  count+=1

print(count)

