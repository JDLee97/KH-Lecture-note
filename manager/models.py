'''
- 등록
- 목록조회
- 상세조회
- 삭제
- 반복문 적용
'''
from word_file import WordFile

word_list = []

def print_menu():
    print('\n===== 백과 사전 =====')
    print('1. 단어 등록')
    print('2. 목록 조회')
    print('3. 목록 삭제')
    print('0. 종료')

def choose_number():
    num = int(input('번호를 입력하세요 : '))
    return num

def register():
    print('\n===== 단어 등록 =====')
    word_kr = input('한국어 표기 : ')
    word_eng = input('영어 표기 : ')
    meaning = input('의미 : ')
    image = input('사진파일 : ')
    b = WordFile(word_kr, word_eng, meaning, image)
    word_list.append(b)

def searching():
    print('\n===== 목록조회 =====')

    while True:
        for idx, word in enumerate(word_list):
            print(idx , word.word_kr)

        num = int(input('몇번 목록을 조회하시겠습니까? : '))
        if num > idx or num < 0 :
            print('제대로 된 숫자를 입력해주세요.\n')
            continue

        con_or_stop = details(num)
        if con_or_stop == 'y' :
            continue
        if con_or_stop == 'n' :
            break

def details(num):
    print(word_list[num])
    while True:
        con_or_stop = input('계속 조회하시겠습니까? (y/n) ').lower()
        match con_or_stop:
            case 'y':
                break
            case 'n':
                break
            case _:
                print('다시 입력해주세요.\n')
    return con_or_stop

def delete():
    while True:
        print('\n===== 목록 삭제 =====')
        for idx, word in enumerate(word_list):
            print(idx, word.word_kr)
        num = int(input('삭제하고 싶은 책의 번호를 입력해주세요.'))
        del word_list[num]

        while True :
            con_or_stop = input('계속 삭제하시겠습니까? (y/n) ').lower()
            match con_or_stop:
                case 'y':
                    break
                case 'n':
                    break
                case _:
                    print('다시 입력해주세요. ')

        if con_or_stop == 'y':
            continue
        if con_or_stop == 'n':
            break

def manage_program():

    while True:
        print_menu()
        num = choose_number()
        match num :
            case 1 :
                register()
            case 2 :
                searching()
            case 3 :
                delete()
            case 0 :
                break
            case _ :
                print('\n번호를 다시 선택해주세요.\n')
                continue


