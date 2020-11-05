n,k=map(int,input().split())
s=input()
ans=3000000
letter=[[] for i in range(26)]
for i in range(n):
    index=ord(s[i])-ord("a")
    letter[index].append(i)
    if len(letter[index])>=k:
        l=len(letter[index])
        ans=min(ans,letter[index][-1]-letter[index][l-k]+1)
if ans==3000000:
    print("-1")
else:
    print(ans)



