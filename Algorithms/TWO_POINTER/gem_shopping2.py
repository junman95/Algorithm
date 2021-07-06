#정확성 통과 효율성 미통과


gems1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gems2 = ["AA", "AB", "AC", "AA", "AC"]
gems3 = ["XYZ", "XYZ", "XYZ"]
gems4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

from collections import deque
def solution(gems):
  gem_list = list(set(gems))
  gem_nums = len(gem_list)
  shopping_cart = deque(set())
  ans = list() # 모든 젬들을 포함하는 쇼핑카트의 start와 end
  ans_dist = 100001
  end = 0
  for start in range(len(gems)):
    print(len(set(shopping_cart)),shopping_cart)
    while len(set(shopping_cart))<gem_nums and end < len(gems):
      shopping_cart.append(gems[end])
      end += 1

    if len(set(shopping_cart)) == gem_nums:
      if ans_dist> end - start:
        ans_dist = end -start
        ans = [start+1,end]
    shopping_cart.popleft()
    start+=1
  
  return ans

print(solution(gems4))