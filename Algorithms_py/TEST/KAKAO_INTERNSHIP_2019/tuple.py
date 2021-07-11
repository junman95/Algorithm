#testcases
tc1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"	#[2, 1, 3, 4]
tc2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"	#[2, 1, 3, 4]
tc3 ="{{20,111},{111}}"	#[111, 20]
tc4 = "{{123}}"	#[123]
tc5 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"	#[3, 2, 4, 1]

def solution(s):
    list_s = list()
    temp_list = list()
    temp_num =''
    for i in range(1,len(s)-1): #겉 { } 절삭
        if s[i] == '{':
            pass
        elif s[i] == '}':
            temp_list.append(int(temp_num))
            temp_num = ""
            list_s.append(temp_list)
            temp_list=list()
        elif s[i] == ',': #내부쉼표 외부쉼표 구분
            if temp_num:
                temp_list.append(int(temp_num))
            temp_num = ""
        else: #숫자일때
            temp_num += s[i]
    print(list_s)
    list_s.sort(key=len)
    print(list_s)
    
    answer = [list_s[0][0]]
    for idx in range(len(list_s)-1):
        for j in answer:
            list_s[idx+1].remove(j)
        print(list_s)
        answer.append(list_s[idx+1][0])
    return answer

print(solution(tc3))