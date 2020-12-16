dic = {}
for i in range(kolichestvostudentov):
    print("What is your favourite movie?")
    a = input()
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

list_d = list(dic.items())
list_d.sort(key=lambda i: i[1], reverse= True)
for i in range(len(list_d)):
    print(list_d[0])
