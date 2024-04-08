goukei = int(input())
hatu = int(input())
hatu_m = int(input())
ato_m = int(input())
sumNum = 0

for i in range(goukei):
    if i < hatu:
        sumNum = sumNum + hatu_m
    else:
        sumNum = sumNum + ato_m

print(sumNum)