from collections import defaultdict

h, w, n = map(int, input().split())
d = defaultdict(int)

for _ in range(n):
  a, b = map(int, input().split())
  
  for i in range(-2, 1):
    for j in range(-2, 1):
      a_i = a + i
      b_j = b + j
      if (0 < a + 2 + i < h + 1 and 0 < b + 2 + j < w + 1) and (0 < a_i < h + 1 and 0 < b_j < w + 1):
        d[(a_i, b_j)] += 1

res = [0] * 10

print(d)

for key, value in d.items():
  res[value] += 1
res[0] = (h - 2)*(w - 2) - sum(res)

for i in range(10):
  print(res[i])