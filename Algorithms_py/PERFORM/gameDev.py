
# n =세로크기  /  m =가로크기
n, m = map(int,input().split())
# player_pos = 게이머 위치 / d = 방향
player_pos=list([0,0])
player_pos[0],player_pos[1], d = map(int,input().split())

game_map = list()
for i in range(n):
    game_map.append(list(map(int, input().split())))

print(game_map)