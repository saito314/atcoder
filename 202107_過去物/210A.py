n, a, x, y = map(int, input().split())

ans = 0
cnt = 1

for i in range(n):
    if cnt <= a:
        ans += x
    else:
        ans += y
    cnt += 1

print(ans)