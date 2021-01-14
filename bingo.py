import pandas as pd
import random
import numpy as np


b = random.sample(range(1, 16), k=5)
i = random.sample(range(16, 31), k=5)
n = random.sample(range(31, 46), k=5)
n[2] = 'FREE'                         #三行目の真ん中をFREEにする。
g = random.sample(range(46, 61), k=5)
o = random.sample(range(61, 76), k=5)
table = [b, i, n, g, o]

df1 = pd.DataFrame(table,
                   index=['b', 'i', 'n', 'g', 'o'],
                   columns=['v', 'w', 'x', 'y', 'z']).T

bingo_ball = list(range(1, 76))
random.shuffle(bingo_ball)

count_up = 0
count_up_bingo= 0
count_up_reach = 0

'''各判定処理'''
for b_num in bingo_ball:
    count_up = count_up + 1

    if b_num in df1.values:
        count_up_bingo = 0
        count_up_reach = 0
        df1 = df1.replace(b_num, '{' + str(b_num) + '}')
        df = df1.astype(str)
        result　= 'ボールの番号は' + str(b_num) + 'です。当たりなので表に穴を開けます！'

        for c in df.columns:
            count = sum(df[c].str.endswith('}')) + sum(df[c] == 'FREE')
            if count == 5:
                count_up_bingo = count_up_bingo + 1
            elif count == 4:
                count_up_reach = count_up_reach + 1

        for r in df.index:
            count = sum(df.loc[r].str.endswith('}')) + sum(df.loc[r] == 'FREE')
            if count == 5:
                count_up_bingo = count_up_bingo + 1
            elif count == 4:
                count_up_reach = count_up_reach + 1

        diagonal_r = list(np.diag(df1))
        lst = [i for i in diagonal_r if isinstance(i, str)]  # 文字列のみ
        cnt = len(lst)
        if cnt == 5:
            count_up_bingo = count_up_bingo + 1
        elif cnt == 4:
            count_up_reach = count_up_reach + 1

        diagonal_l = list(np.diag(np.fliplr(df1)))
        lst = [i for i in diagonal_l if isinstance(i, str)]  # 文字列のみ
        cnt2 = len(lst)
        if cnt2 == 5:
            count_up_bingo = count_up_bingo + 1
        elif cnt2 == 4:
            count_up_reach = count_up_reach + 1

    else:
      result　= 'ボールの番号は' + str(b_num) + 'です。ハズレです！'
      
    print('')
    print(str(count_up) + '回目！')
    print(result)
    print(df1)
    print('')
    print('ビンゴ数：' + str(count_up_bingo))
    print('リーチ数：' + str(count_up_reach))
    print('ーーーーーーーーーーーーーーーーーーーーーーーー')
