import pandas as pd
import random
import numpy as np


'''ビンゴ表のリスト'''
b = random.sample(range(1, 16), k=5)
i = random.sample(range(16, 31), k=5)
n = random.sample(range(31, 46), k=5)
n[2] = 'FREE'                         #三行目の真ん中をFREEにする。
g = random.sample(range(46, 61), k=5)
o = random.sample(range(61, 76), k=5)
table = [b, i, n, g, o]


'''リストを表にして表示'''
df1 = pd.DataFrame(table,
                   index=['b', 'i', 'n', 'g', 'o'],
                   columns=['v', 'w', 'x', 'y', 'z'])


'''ビンゴのボール(1~75までの数字を用意し、シャッフルする)'''
num = list(range(1, 76))
random.shuffle(num)


'''各カウントアップ'''
count_up = 0
count_up_bingo= 0
count_up_reach = 0

'''各判定処理'''
for b_num in num:
    count_up = count_up + 1

    '''当たりが出た場合の処理'''
    if b_num in df1.values:
        count_up_bingo = 0
        count_up_reach = 0
        df1 = df1.replace(b_num, '{' + str(b_num) + '}')
        df = df1.astype(str)
        print('')
        print(str(count_up) + '回目！')
        print('ボールの番号は' + str(b_num) + 'です。当たりなので穴を開けます！')
        print(df1)

        '''列判定'''
        for c in df.columns:
            count = sum(df[c].str.endswith('}')) + sum(df[c] == 'FREE')
            if count == 5:
                count_up_bingo = count_up_bingo + 1
            elif count == 4:
                count_up_reach = count_up_reach + 1

        '''行判定'''
        for r in df.index:
            count = sum(df.loc[r].str.endswith('}')) + sum(df.loc[r] == 'FREE')
            if count == 5:
                count_up_bingo = count_up_bingo + 1
            elif count == 4:
                count_up_reach = count_up_reach + 1

        '''斜め判定1＼'''
        diagonal_r = list(np.diag(df1))
        lst = [i for i in diagonal_r if isinstance(i, str)]  # 文字列のみ
        cnt = len(lst)
        if cnt == 5:
            count_up_bingo = count_up_bingo + 1
        elif cnt == 4:
            count_up_reach = count_up_reach + 1

        '''斜め判定2／'''
        diagonal_l = list(np.diag(np.fliplr(df1)))
        lst = [i for i in diagonal_l if isinstance(i, str)]  # 文字列のみ
        cnt2 = len(lst)
        if cnt2 == 5:
            count_up_bingo = count_up_bingo + 1
        elif cnt2 == 4:
            count_up_reach = count_up_reach + 1

        '''ビンゴ、リーチのカウント'''
        print('')
        print('ビンゴ数：' + str(count_up_bingo))
        print('リーチ数：' + str(count_up_reach))
        print('ーーーーーーーーーーーーーーーーーーーーーーーー')

    #ハズレが出た場合の処理
    else:
        print('')
        print(str(count_up) + '回目！')
        print('ボールの番号は' + str(b_num) + 'です。ハズレです！')
        print(df1)
        print('')
        print('ビンゴ数：' + str(count_up_bingo))
        print('リーチ数：' + str(count_up_reach))
        print('ーーーーーーーーーーーーーーーーーーーーーーーー')

if count_up == 75:
    print('')
    print('＿人人人人人人人人人人人＿')
    print('＞ ビンゴゲーム終了！！ ＜')
    print('￣Y^Y^Y^Y^Y^Y^Y^Y^Y^Y￣')