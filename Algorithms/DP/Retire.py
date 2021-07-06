import sys
n = int(input())

calandar = list()
dp_table = list([0]*n)

for i in range(n):
  calandar.append(list(map(int,sys.stdin.readline().rstrip().split())))

def bestSchedule():
  for i in range(n-1,-1,-1): #순차적으로 7일차~ 1일차까지 탐색
    print(dp_table)
    if calandar[i][0] + i <= n: # 현재 날짜+ 상담종료까지 걸리는 일수가 퇴사일을 넘기면 조건에 못듬.
      if i+calandar[i][0] == n: # 현재 날짜+ 상담종료까지 걸리는 일수 = 퇴사일이면 현재금액 테이블에 저장
        dp_table[i] = calandar[i][1]
      else: # 현재 날짜+ 상담종료까지 걸리는 일수 이후의 테이블값중 가장 큰값이랑 합함.
        dp_table[i] = max(dp_table[i+calandar[i][0]:]) + calandar[i][1]

bestSchedule()
print(max(dp_table))