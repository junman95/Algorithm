gems1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gems2 = ["AA", "AB", "AC", "AA", "AC"]
gems3 = ["XYZ", "XYZ", "XYZ"]
gems4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

def solution(gems):
    
    shopped_gems = [] # 보석 저장 바구니
    
    pin_a, pin_b = 0,0
    min_pin_dist = 100001
    temp_two_pins = [0,0]
    unbought_gems = list(set(gems))

    for i in range(len(gems)):
      print(pin_a, pin_b, unbought_gems)
      while unbought_gems and pin_b<len(gems):
        shopped_gems.append(gems[pin_b]) # 쇼핑된 젬 바구니에 넣기

        if gems[pin_b] in unbought_gems:
          unbought_gems.remove(gems[pin_b])
          if not unbought_gems:
            break
        print(pin_a, pin_b, unbought_gems)
        pin_b+=1

      if pin_b >=len(gems) and unbought_gems:
        print("현재 a핀 이후로는 종류별로 담기 불가 -> 탐색종료")
        break

      if min_pin_dist > pin_b-pin_a:
        min_pin_dist = pin_b-pin_a
        temp_two_pins = [pin_a,pin_b]

      print(shopped_gems)
      shopped_gems.remove(gems[pin_a])
      if gems[pin_a] not in shopped_gems:
        unbought_gems.append(gems[pin_a])
        print(unbought_gems)
      if pin_b > pin_a:
        pin_a+=1

    answer = temp_two_pins
    return answer


print(solution(gems4))