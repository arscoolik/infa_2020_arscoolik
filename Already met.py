dict = {}
while True:
    a = int(input())
    if a in dict:
        print(1)
    else:
        dict[a] = 1
        print(0)