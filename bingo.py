import pandas as pd
import random
import numpy as np

'''ビンゴ表のリスト'''
b = random.sample(range(1, 16), k=5)
i = random.sample(range(16, 31), k=5)
n = random.sample(range(31, 46), k=5)
n[2] = 'FREE' #三行目の真ん中をFREEにする。
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

for b_num in num:
    count_up = count_up + 1
    if b_num in df1.values:
        df1 = df1.replace(b_num, 'X')

        print(str(count_up) + '回目！')
        print('ボールの番号は' + str(b_num) + 'です。当たりなので穴を開けます！')

        '''縦判定'''
        for c in df1.columns:
            count = sum(df1[c] == 'X') + sum(df1[c] == 'FREE')
            if count == 5:
                print(f'{c}:ビンゴ！')
            elif count == 4:
                print(f'{c}:リーチ！')

        '''横判定'''
        for r in df1.index:
            count = sum(df1.loc[r] == 'X') + sum(df1.loc[r] == 'FREE')
            if count == 5:
                print(f'{r}:ビンゴ！')
            elif count == 4:
                print(f'{r}:リーチ！')

        '''斜め判定'''
        diagonal_r = list(np.diag(df1))
        count_r = diagonal_r.count('X')

        diagonal_l = list(np.diag(np.fliplr(df1)))
        count2 = len(set(diagonal_l))


        print(count2)


    else:
        print(str(count_up) + '回目！')
        print('ボールの番号は' + str(b_num) + 'です。ハズレです！')
        print(df1)