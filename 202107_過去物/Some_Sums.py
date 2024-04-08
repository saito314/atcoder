inputStr = input()
n = int(inputStr.split()[0])
a = int(inputStr.split()[1])
b = int(inputStr.split()[2])

global_sum = 0
for i in range(1, n+1):
    c = str(i)
    local_sum = 0
    for j in c:
        local_sum = local_sum + int(j)
    else:
        if a <= local_sum and local_sum <= b:
            global_sum = global_sum + i

print(global_sum)