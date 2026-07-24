import random

question_list = ['현재위치에서 다른 위치로 이동하는 명령어?','현재폴더를 의미하는 기호?','유저를 추가하는 명령어?', '계정을 변경하는 명령어?', '파일위치를 최상위 폴더부터 검색하는 방법?', '파일위치를 현재 폴더부터 검색하는 방법?', '파일을 복사해주는 명령어?' , '파일을 이동하는 명령어?' ]
answer_list = ['cd', '.', 'adduser','su','절대경로','상대경로','cp','mv']
set_list = list(zip(question_list,answer_list))

i = 0 #문제 인덱스

while True :
    print('\n\n문제를 시작하겠습니다.')
    print('종료 버튼은 0 입니다.')
    typeAnswer = input('문제를 시작하고싶으면 0을 제외한 아무버튼을 누르세요 : ')

    problem_index = list(range(0, 7))  # 문제 인덱스 생성
    random.shuffle(problem_index)  # 랜덤하게 섞어서 앞에 3개만 뽑아 쓸 예정
    count = 0  # 문제 맞춘횟수

    if typeAnswer == '0' :
        break

    while i < 3 :


        p = set_list[problem_index[i]][0]
        a = set_list[problem_index[i]][1]
        print(p)
        answer = input('\n정답을 입력하세요 : ')

        if answer.lower() == a.lower() :
            print('정답입니다.\n')
            count = count + 1
            i = i + 1
        else :
            print(f'오답입니다. 정답은 {a} 입니다.\n')
            i = i + 1

    print(f'{count}문제 맞추셨습니다.')

    if count == 0:
        print('성적은 F 입니다.')
    elif count == 1:
        print('성적은 C 입니다.')
    elif count == 2:
        print('성적은 B 입니다.')
    else :
        print('성적은 A 입니다.')
