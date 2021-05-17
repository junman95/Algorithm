brackets = input()
bracket_list = list(brackets)
visited = [False] * (len(bracket_list))

print(bracket_list)

start_node = 0
pairs = [[] for _ in range(2)]
print(pairs)
current_pos = 0


def brackets(bracket_list, current_node, pairs, current_pos):
    visited[current_node] = True
    print(current_node, " : ", bracket_list[current_node])

    if bracket_list[current_node] == "(":
        pairs[0] = current_node
    elif bracket_list[current_node] == ")":
        if pairs[0] != "" and pairs[1] == []:
            print("pass")
            pairs[1] = current_node

    current_node += 1
    if current_node < len(bracket_list) and (pairs[1]) == []:
        brackets(bracket_list, current_node, pairs, current_pos)

    return pairs



def solution():
    for _ in range(int(len(bracket_list)/2)):
        print("Getting rid of paired brackets")
        paired_bracket = brackets(bracket_list, start_node, pairs, current_pos)
        print(paired_bracket[0])
        for i in range(len(bracket_list)):
            if bracket_list[i] == paired_bracket[0] or bracket_list[i]== paired_bracket[1]:
                print("papa")

                bracket_list.pop(i)
                print(bracket_list)

solution()
