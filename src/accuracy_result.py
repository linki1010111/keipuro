def evaluate(a :list[list[str]],b:list[list[str]]):
    cnt,ac =0,0
    for i in range(len(a)):
        if a[i]==b[i]:
            ac = ac+1
        cnt = cnt+1
    return ac/cnt*100
