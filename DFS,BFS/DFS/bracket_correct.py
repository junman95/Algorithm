
bracket = input()
counter = 0
def bracketFunc(bracket_str):
  global counter
  counter +=1
  u = ""
  v = ""
  # No.1
  if bracket_str == "":
    return ""
  # No.2
  else:
    counter_open = 0
    counter_close = 0

    for i in range(len(bracket_str)):
      if bracket_str[i] =="(":
        counter_open+=1
      else:
        counter_close+=1
      
      if counter_open == counter_close:
        u = bracket_str[:i+1]
        v = bracket_str[i+1:]
        break;
    #No 3    
    if isCorrect(u,v) == True:
      #No.3-1
      u += bracketFunc(v)
      return u
    #No. 4  
    elif isCorrect(u,v) == False:
      #No. 4-1
      temp = '('
      #No. 4-2
      temp += bracketFunc(v)
      #No. 4-3
      temp += ')'
      temp += setReverse(u)
      return temp


def isCorrect(u,v):
  # No.3
  stack = []
  for i in u:
    if stack == []:
      stack = [u[0]]
    # 이전에 스택에 들어간 괄호가 ( 이고, 들어오는 괄호가 )이면 올바르므로 제거
    elif stack != []:
      if stack[-1] == '(' and i ==')':
        stack.pop()
      else:
        stack.append(i)

  if stack != []:
    return False
  elif stack == []:
    return True

def setReverse(object):
  object_list = list(object[1:-1])
  object = ''
  for i in range(len(object_list)):
    if object_list[i] == '(':
      object_list[i] =')'
    elif object_list[i] == ')':
      object_list[i] ='('
    object += object_list[i]
  return object


print(bracketFunc(bracket))