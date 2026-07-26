import UpDown
import lotto
import RockScissorPaper as RSP

while True:
    print('=====미니게임=====')
    print('1. 가위바위보')
    print('2. 업다운')
    print('3. 로또추첨')
    print('4. 게임 종료')
    print('=================')

    menu = int(input('메뉴에 숫자를 입력하세요 : '))
    if menu == 1:
        RSP.RSP()
    elif menu == 2:
        UpDown.UpDown()
    elif menu == 3:
        lotto.lotto()
    elif menu == 4:
        print('게임종료')
        break
    else:
        print('1에서 4사이 숫자만 입력해주세요')

