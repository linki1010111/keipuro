def yosoku(x,y,z):#x辞書１y辞書２z文章
    hitei=[['ない',2],['なく',2]]#否定の辞書(否定の場合一旦極性を2にする)
    dictionarygen=x+y#辞書の結合
    dictionary=[]
    for w in dictionarygen:
        if w[1]=='n':
            dictionary.append([w[0],-1])
        elif w[1]=='p':
            dictionary.append([w[0],1])
        else:
            dictionary.append([w[0],0])#辞書の極性を整数に変換
    dictionary=sorted(dictionary,key=lambda x: len(x[0]),reverse=True)#単語の長さでsort
    ans=[]#ここに文章とその極性のリストを追加していく
    for s in z:#文章の個数分for loop
        det=['u' for _ in range(len(s))]#文章の長さのリストではじめは全部undetected
        for w in dictionary:#dictionaryの中の単語の個数分for loop　wごとにこの単語がsのundetected領域に含まれているかどうかを判定してあったらdetにその情報を入れる
            state=0#stateは今単語wの何文字目を見ているか
            posi=0#posiは今文章sの何文字目を見ているか
            while state!=len(w[0]) and posi!=len(s):#単語の最後の文字を見終えるか文章の最後を身終えるかまで繰り返す
                if det[posi]=='u' and s[posi]==w[0][state]:#もしsの中の見ている文字のdetがundetectedでありsの中の見ている文字がwの中の見ている文字と一致しているならば
                    state=state+1#wの次の文字を見る
                    posi=posi+1#sの次の文字を見る
                else:#もしそうでなかったら
                    state=0#wの最初の文字に戻る
                    posi=posi+1#sの次の文字を見る
            if state!=len(w[0]):#もしwの文字を見終わっていない
                pass#sの中にw花買ったから何もしない
            else:#もしwの文字を見終わった
                det[posi-1]=w[1]#sの中でwの最後の文字があるところのdetをその単語の極性の整数にする
                for i in range(1,len(w[0])):#wの最後の文字でないところのdetはdetectedにする
                    det[posi-1-i]='d'
        for h in hitei:#上と同様の方法で否定を処理
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
        kyokusei=0#はじめは極性を0にする
        det.reverse()#detを反転してうしろから文章の極性を見ていく
        first=2#一番後ろの極性を持つ単語の極性を二倍にしたいことを反映
        gyaku=1#否定があった時のためのもの
        for i in range(len(det)):
            if det[i]==2:
                gyaku=gyaku*(-1)#否定があったらgyakuを(-1)倍
            elif det[i]==-1:#negativeな単語があった時
                if gyaku==-1:#それまでに否定が奇数回現れた時
                    kyokusei=kyokusei+det[i]*gyaku*first#kyokuseiに否定と最初の単語かどうかを反映させて追加(否定ならば−１倍、はじめに検知したなら2倍)
                    first=1#firstを1にする(元々1でもいい)
                    gyaku=1#否定をリセット
                elif gyaku==1:#それまでに否定が偶数回現れた時
                    kyokusei=kyokusei+det[i]*gyaku*first#kyokuseiに否定と最初の単語かどうかを反映させて追加(否定ならば−１倍、はじめに検知したなら2倍)
                    first=1#firstを1にする(元々1でもいい)
            elif det[i]==1:#positiveな単語があった時(以下は同様)
                if gyaku==-1:
                    kyokusei=kyokusei+det[i]*gyaku*first
                    first=1
                    gyaku=1
                elif gyaku==1:
                    kyokusei=kyokusei+det[i]*gyaku*first
                    first=1
            elif det[i]==0:#neutralな単語があったとき(以下は同様)
                if gyaku==-1:
                    kyokusei=kyokusei+det[i]*gyaku*first
                    first=1
                    gyaku=1
                elif gyaku==1:
                    kyokusei=kyokusei+det[i]*gyaku*first
                    first=1
            else:
                pass
        if kyokusei>0:#最終的な極性が正である
            ans.append([s,'p'])
        elif kyokusei<0:#最終的な極性が負である
            ans.append([s,'n'])
        else:#最終的な極性が0な時
            ans.append([s,'e'])
    return ans
    
