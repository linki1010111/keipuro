def yosoku(x,y,z):
    hitei=[['ない',2],['なく',2]]
    dictionarygen=x+y
    dictionary=[]
    for w in dictionarygen:
        if w[1]=='n':
            dictionary.append([w[0],-1])
        elif w[1]=='p':
            dictionary.append([w[0],1])
        else:
            dictionary.append([w[0],0])
    dictionary=sorted(dictionary,key=lambda x: len(x[0]),reverse=True)
    ans=[]
    for s in z:
        det=['u' for _ in range(len(s))]
        for w in dictionary:
            state=0
            posi=0
            while state!=len(w[0]) and posi!=len(s):
                if det[posi]=='u' and s[posi]==w[0][state]:
                    state=state+1
                    posi=posi+1
                else:
                    state=0
                    posi=posi+1
            if state!=len(w[0]):
                pass
            else:
                det[posi-1]=w[1]
                for i in range(1,len(w[0])):
                    det[posi-1-i]='d'
        for h in hitei:
            state=0
            posi=0
            while state!=len(h[0]) and posi!=len(s):
                if det[posi]=='u' and s[posi]==h[0][state]:
                    state=state+1
                    posi=posi+1
                else:
                    state=0
                    posi=posi+1
            if state!=len(h[0]):
                pass
            else:
                det[posi-1]=h[1]
                for i in range(1,len(h[0])):
                    det[posi-1-i]='d'
        kyokusei=0
        det.reverse()
        for i in range(len(det)):
            first=2
            gyaku=1
            if det[i]==2:
                gyaku=gyaku*(-1)
            elif det[i]==-1:
                if gyaku==-1:
                    kyokusei=kyokusei+det[i]*gyaku*first
                    first=1
                    gyaku=1
                elif gyaku==1:
                    kyokusei=kyokusei+det[i]*gyaku*first
                    first=1
            elif det[i]==1:
                if gyaku==-1:
                    kyokusei=kyokusei+det[i]*gyaku*first
                    first=1
                    gyaku=1
                elif gyaku==1:
                    kyokusei=kyokusei+det[i]*gyaku*first
                    first=1
            elif det[i]==0:
                if gyaku==-1:
                    kyokusei=kyokusei+det[i]*gyaku*first
                    first=1
                    gyaku=1
                elif gyaku==1:
                    kyokusei=kyokusei+det[i]*gyaku*first
                    first=1
            else:
                pass
        if kyokusei>0:
            ans.append([s,'p'])
        elif kyokusei<0:
            ans.append([s,'n'])
        else:
            ans.append([s,'e'])
    return ans
    
