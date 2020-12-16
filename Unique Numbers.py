X = list(map(int, input().split()))
Y = list(map(int, input().split()))
ANS1 = set()
ANS2 = set()
ANS12 = set()
for i in range(len(X)):
    ANS1.add(X[i])
    ANS12.add(X[i])
for i in range(len(Y)):
    ANS2.add(Y[i])
    ANS12.add(Y[i])
print(ANS1, ANS2, ANS12)