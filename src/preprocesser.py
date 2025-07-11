def preprocesser(x,z):#x辞書 z文章
    hiteiwords=[['ない',2],['なく',2]]#否定の辞書(否定の場合一旦極性を2にする)
    dictionarygen=x
    dictionary=[]
    for w in dictionarygen:
        if w[1]=='n':
            dictionary.append([w[0],-1])
        elif w[1]=='p':
            dictionary.append([w[0],1])
        else:
            dictionary.append([w[0],0])#辞書の極性を整数に変換
    dictionary=sorted(dictionary,key=lambda x: len(x[0]),reverse=True)#単語の長さでsort
    ans=[]#ここに文章,p,n,e、p-n、p+n,p+n+eのリストを追加していく
    for s in z:#文章の個数分for loop
        det=['u' for _ in range(len(s))]#文章の長さのリストではじめは全部undetected
        for w in dictionary:#dictionaryの中の単語の個数分for loop　wごとにこの単語がsのundetected領域に含まれているかどうかを判定してあったらdetにその情報を入れる
            state=0#stateは今単語wの何文字目を見ているか
            posi=0#posiは今文章sの何文字目を見ているか
            while state!=len(w[0]) and posi!=len(s):#単語の最後の文字を見終えるか文章の最後を身終えるかまで繰り返す
                if det[posi]=='u' and s[posi]==w[0][state]:#もしsの中の見ている文字のdetがundetectedでありsの中の見ている文字がwの中の見ている文字と一致しているならば
                    state=state+1#wの次の文字を見る
                    posi=posi+1#sの次の文字を見る
                elif det[posi]=='u' and s[posi]=='く' and w[0][state]=='い' and state==len(w[0])-1:#形容詞の語尾いがくに変わったものを認識する
                    state=state+1
                    posi=posi+1
                else:#もしそうでなかったら
                    state=0#wの最初の文字に戻る
                    posi=posi+1#sの次の文字を見る
            if state!=len(w[0]):#もしwの文字を見終わっていない
                pass#sの中にw花買ったから何もしない
            else:#もしwの文字を見終わった
                det[posi-1]=w[1]#sの中でwの最後の文字があるところのdetをその単語の極性の整数にする
                for i in range(1,len(w[0])):#wの最後の文字でないところのdetはdetectedにする
                    det[posi-1-i]='d'
        for h in hiteiwords:#上と同様の方法で否定を処理
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
        psum=0#読み取ったpositiveの個数
        nsum=0#読み取ったnegetiveの個数
        esum=0#読み取ったeの個数
        target=0#detで今読んでいるところ
        hitei=1#今否定が効いているかどうか
        det.reverse()#detを後ろから読む
        while target!=len(det):#detの一番後ろまで
            if det[target]=='u' or det[target]=='d':#極性のないところ
                pass
            if det[target]==2:#否定があるところ
                hitei=hitei*(-1)#hiteiを−１ばい
            if det[target]==1 or det[target]==0 or det[target]==-1:#極性のあるところ
                kyokusei=det[target]*hitei#否定も込めた極性
                hitei=1#否定をリセット
                
                if kyokusei==1:#極性が１
                    psum=psum+1#positiveの個数を一つ追加
                if kyokusei==-1:#極性が-1
                    nsum=nsum+1#negativeの個数を一つ追加
                if kyokusei==0:#極性が0
                    esum=esum+1#eの個数を一つ追加
            target=target+1#次を読む
        ans.append([s,psum,nsum,esum,psum-nsum,psum+nsum,psum+nsum+esum])
    return (ans)


                
            