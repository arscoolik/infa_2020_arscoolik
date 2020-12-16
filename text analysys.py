s = list(input().split())
dic = {}
for i in s:
    if not i[-1].isalpha():
        i = i[:-1:]
    if i.lower() in dic:
        dic[i.lower()] += 1
    else:
        dic[i.lower()] = 1

list_d = list(dic.items())
print(list_d)
list_d.sort(key=lambda i: i[1], reverse= True)
for i in range(len(list_d)):
    print(list_d[i][0])