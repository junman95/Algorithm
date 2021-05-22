n = int(input())
number_raw = list()

for _ in range(n):
  number_raw.append(input())

number_raw.sort(reverse=True)

print(number_raw)

