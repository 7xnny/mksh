scores = list()
n = int(input("n="))
while n>=0:
    scores.append(n)
    n = int(input("n="))
print(sorted(scores))
print("最高分是",max(score))
print("最低分是",min(score))
print("總分是",sum(score))
print("平均是",sum(score)/len(scores))