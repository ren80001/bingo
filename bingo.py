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
count_up_bingo = 0
count_up_reach = 0


'''各判定処理'''
for b_num in num:
    count_up = count_up + 1
    if b_num in df1.values:
        df1 = df1.replace(b_num, '{' + str(b_num) + '}')
        df = df1.astype(str)
        print('')
        print(str(count_up) + '回目！')
        print('ボールの番号は' + str(b_num) + 'です。当たりなので穴を開けます！')
        print(df1)
        print('ーーーーーーーーーーーーーーーーーーーーーーーー')

        '''列判定'''
        for c in df.columns:
            count = sum(df[c].str.endswith('}')) + sum(df[c] == 'FREE')
            if count == 5:
                print(f'{c}:ビンゴ！')
            elif count == 4:
                print(f'{c}:リーチ！')

        '''行判定'''
        for r in df.index:
            count = sum(df.loc[r].str.endswith('}')) + sum(df.loc[r] == 'FREE')
            if count == 5:
                print(f'{r}:ビンゴ！')
            elif count == 4:
                print(f'{r}:リーチ！')

        '''斜め判定＼'''
        diagonal_r = list(np.diag(df1))
        lst = [i for i in diagonal_r if isinstance(i, str)]  # 文字列のみ
        cnt = len(lst)
        if cnt == 5:
            print('斜め＼ビンゴ！')
        elif cnt == 4:
            print('斜め＼リーチ！')

        '''斜め判定2／'''
        diagonal_l = list(np.diag(np.fliplr(df1)))
        lst = [i for i in diagonal_l if isinstance(i, str)]  # 文字列のみ
        cnt2 = len(lst)
        if cnt2 == 5:
            print('斜め／ビンゴ！')
        elif cnt2 == 4:
            print('斜め／リーチ！')

    else:
        print('')
        print(str(count_up) + '回目！')
        print('ボールの番号は' + str(b_num) + 'です。ハズレです！')
        print(df1)
        print('ーーーーーーーーーーーーーーーーーーーーーーーー')

if count_up == 75:
    print('')
    print('＿人人人人人人人人人人人＿')
    print('＞ ビンゴゲーム終了！！ ＜')
    print('￣Y^Y^Y^Y^Y^Y^Y^Y^Y^Y￣')