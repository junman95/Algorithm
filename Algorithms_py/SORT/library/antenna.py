n = int(input())
house = sorted(list(map(int,input().split(' '))))
spot = house[(n-1)//2]
print(spot)
