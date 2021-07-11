N = input()
#문자열로 받아서 길이측정 및 중간값 반환
pivot=int(len(N)/2)
#새 리스트에 int형으로 변환
N_num=list()
for i in range(len(N)):
  N_num.append(int(N[i]))

#중간값으로부터 좌 우 합 할당
sum_left = sum(N_num[:pivot])
sum_right = sum(N_num[pivot:])

#비교
if sum_left==sum_right:
  print("LUCKY")
else:
  print("READY")