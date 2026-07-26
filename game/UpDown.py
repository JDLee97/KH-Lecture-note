# 업다운 게임
def UpDown() :
    import random

    print('\n\n업다운 게임에 오신걸 환영합니다.')
    answer = random.randint(1, 100)

    numdown = 1
    numup = 100
    count = 5
    while True :
        while True:
            num = int(input('1 - 100 사이숫자를 입력하세요 : '))

            if num > answer:
                numup = num
                count = count - 1
                print(f'숫자가 높습니다. {numup}과 {numdown}사이 숫자중에 다시 고르세요.')
                print(f'기회는 {count}번 남았습니다.')

            elif num < answer:
                numdown = num
                count = count - 1
                print(f'숫자가 높습니다. {numup}과 {numdown}사이 숫자중에 다시 고르세요.')
                print(f'기회는 {count}번 남았습니다.')

            else:
                print('정답입니다!')
                break

            if count == 0:
                print('다음기회에 ')
                break
        retry = input('다시 하시겠습니까? (y/n)').lower()
        if retry == 'y' :
            pass
        elif retry == 'n' :
            break