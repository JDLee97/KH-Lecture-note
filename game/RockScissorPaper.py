def RSP():
    import random


    while True:
        randRSP = random.randint(1, 3)
        if randRSP == 1:
            randRSP = '바위'
        elif randRSP == 2:
            randRSP = '가위'
        elif randRSP == 3:
            randRSP = '보'

        myRSP = input('가위 바위 보 중 하나를 고르세요: ')

        if myRSP == '가위':
            print(f'나 : {myRSP} / 상대 : {randRSP}')
            if randRSP == '가위':
                print('무승부')

            elif randRSP == '바위':
                print('패')

            elif randRSP == '보':
                print('승')


        elif myRSP == '바위':
            print(f'나 : {myRSP} / 상대 : {randRSP}')
            if randRSP == '가위':
                print('승')

            elif randRSP == '바위':
                print('무승부')

            elif randRSP == '보':
                print('패')


        elif myRSP == '보':
            print(f'나 : {myRSP} / 상대 : {randRSP}')
            if randRSP == '가위':
                print('패')

            elif randRSP == '바위':
                print('승')

            elif randRSP == '보':
                print('무승부')

        else :
            print('가위 바위 보 중에서 골라주세요.')
            pass
        contin = input('다시 하시겠습니까? (y/n)').lower()

        if contin == 'y':
            pass
        elif contin == 'n':
            break