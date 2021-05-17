brackets = input()
bracket_list = list(brackets)
visited = [False] * (len(bracket_list))

print(bracket_list)
print(visited)

start_node = 0
pairs = [[[]for _ in range(2)] for _ in range(int(len(brackets)/2))]
print(pairs)
current_pos = 0


def brackets(bracket_list, current_node, pairs, current_pos):
    visited[current_node] = True
    print(current_node, " : ", bracket_list[current_node])

    if bracket_list[current_node] == "(":
        pairs[current_pos][0] = current_node
        current_pos += 1
    elif bracket_list[current_node] == ")":
        for i in range(int(len(bracket_list)/ 2)):
            if pairs[i][0] != '' and pairs[i][1] == []:
                print("apss")
                pairs[i][1] = current_node
                break

    current_node += 1
    if current_node < len(bracket_list):
        brackets(bracket_list, current_node,pairs,current_pos)

    return 



brackets(bracket_list, start_node, pairs,current_pos)

print(pairs)