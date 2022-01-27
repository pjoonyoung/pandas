import random


def lotto_make():
    lotto_list = [] # 빈 리스트 선언

    while(len(lotto_list) < 6):
        lotto_num = random.randint(1,45) # 1~45 사이의 정수 출력

        if lotto_num not in lotto_list:
            lotto_list.append(lotto_num)

    lotto_list.sort() # 로또번호 오름차순 정렬
    print('로또번호:',lotto_list)

game = int(input('게임수 입력:'))
for i in range(game):
    lotto_make()