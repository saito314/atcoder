def main():
    num = int(input())

    print(func(num))

def func(x):
    if x == 0:
        return 1
    return x + func(x - 1)

if __name__ == "__main__":
    main()