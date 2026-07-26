# 로또번호 - 6개 추첨
def lotto() :

  print('=====로또추첨=====')

  import random
  number_list =random.sample(range(1,46),7)

  x = ''
  i = 0

  for number in number_list :
    i += 1
    print(f'\n당신의  {i}번째 숫자는 {number}입니다. ')

    if i == 7 :
      print('이용해주셔서 감사합니다.')
      break

    keepgo = input('다음숫자를 보시려면 Enter를 입력해주세요')
    if keepgo == x :
      pass