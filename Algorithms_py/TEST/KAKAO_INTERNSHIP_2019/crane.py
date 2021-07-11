boards = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves =	[1,5,3,5,1,2,1,4]	

#4


def solution(board, moves):
    answer = 0
    bracket = []
    temp_board = board
    for i in moves: # moves순차탐색
        for j in range(len(temp_board)): # 줄
            if temp_board[j][i-1] != 0:
                bracket.append(temp_board[j][i-1])
                temp_board[j][i-1]=0
              
                if len(bracket)>1 and bracket[-1]==bracket[-2]:
                    bracket.pop()
                    bracket.pop()
                    answer+=2
                break
    return answer

print(solution(boards,moves))