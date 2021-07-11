S = list(input())

int_idx=list()
str_idx=list()
for idx in S:
  #문자의 형태가 숫자일경우 형변환 및 정수리스트 할당
  if idx.isnumeric() == True:
    int_idx.append(int(idx))
  #아닐경우 문자리스트 할당
  else:
    str_idx.append(idx)

#문자열 알파벳 순 정렬
str_idx.sort()
print(str_idx,int_idx)

#출력형태로 변환을 위한 작업
A_string = ""
A_num = 0
for idx in str_idx:
  A_string+= idx
for idx in int_idx:
  A_num += idx

print(A_string+str(A_num))