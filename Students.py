ans = []
for i in pianists:
    if i in swimmers and i not in learners_french:
        ans.append(i)
print(*ans)