number = int(input())

inputNumbers = list(map(int,input().split()))

a_num = 0
b_num = 0

for i in range(number):
    count = 0
    ind_max = 0
    max_num = 0
    for j in inputNumbers:
        if j > max_num:
            max_num = j
            ind_max = count
        count = count + 1
    
    if i % 2 == 0:
        a_num = a_num + max_num
    else:
        b_num = b_num + max_num
    del inputNumbers[ind_max]

print(a_num - b_num)
