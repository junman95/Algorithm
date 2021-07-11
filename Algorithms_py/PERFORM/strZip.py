S= input()

list_S = list()
ans_list = list()
#문자열의 크기가 1보다 클때(예외처리 필수)
if len(S) > 1:
  #문자열 완전탐색
  for i in range(1,int(len(S)/2)+1):
    print(i)
    counter=0
    #1~문자열길이/2 만큼 문자열나누기
    while(len(list_S) != int(len(S)/i)+1):
      list_S.append(S[counter:counter+i])
      counter+=i
    #빈문자열 제거 => 최적화 가능 마지막거만 보자
    for i in list_S:
      if i == '':
        list_S.remove(i)
    print(list_S)

    #다음의 문자열과 같을경우 중복문자열을 1로 교체
    for i in range(len(list_S)-1):
      if list_S[i] == list_S[i+1]:
        list_S[i]=1
    print(list_S)

    #문자열이 아닌 숫자값이 연속될경우 더함
    for i in range(len(list_S)-1):
      if type(list_S[i]) == int and type(list_S[i+1]) == int:
        list_S[i+1] +=list_S[i]
        list_S[i]=''
    print(list_S)

    ans = ''
    for i in list_S:
      #숫자 +1을 해줘야한다 -> 10개중복시 9,중복값으로 현재 코드가 동작하기때문에
      #마지막것까지 더해주는 코드 필요(예외처리 필수)
      if type(i) == int:
        i+=1
      #리스트 => 문자열 변환
      ans+=str(i)
    #정답들의 후보 리스트 할당
    ans_list.append(len(ans))

    list_S=[]

  #정답 후보중 최솟값 출력
  print(min(ans_list))

else:
  print('1')