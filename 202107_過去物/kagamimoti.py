number = int(input())

inputList = []
for i in range(number):
    inputList.append(input())
moti = list(map(int, inputList))
remoti = set(moti)
moti = list(remoti)

print(len(moti))