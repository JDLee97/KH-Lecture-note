import csv

with open('loans.csv','r',encoding='utf-8') as f:
    data = csv.DictReader(f)
    data = list(data)

#총 대출건수
total_rent = len(data)

#평균 대출일수
total_rent_days = 0
for row in data:
    date = int(row['대출일수'])
    total_rent_days += date
    avg_rent = total_rent_days / total_rent

# {변수:.xf} 소수점 x자리

#분야별 대출건수
section_loan = {}
for row in data:
    section = row['분야']
    section_loan[section] = section_loan.get(section,0) + 1

# 대출자 유형별
type_loan = {}
for row in data:
    type = row['대출자유형']
    type_loan[type] = type_loan.get(type,0) + 1

# 월별
loan_by_month = {}
for row in data:
    loan_date = row['대출일'][0:7]
    loan_by_month[loan_date] = loan_by_month.get(loan_date,0) + 1

# 최다 대출도서

best_book = ''
best_book_count = 0

loan_book = {}
for row in data:
    book = row['도서명']
    loan_book[book] = loan_book.get(book,0) + 1

for k,v in loan_book.items():
    if v > best_book_count:
        best_book = k
        best_book_count = v

# 인기분야 1위

best_section =''
best_section_count = 0

for k,v in section_loan.items():
    if v > best_section_count:
        best_section = k
        best_section_count = v


with open('report02.txt','w',encoding='utf-8') as f:
    f.write('=== 한빛도서관 대출 리포트 (2025.03 ~ 05) ===\n\n')
    f.write(f'[총 대출 건수] {total_rent}건\n')
    f.write(f'[평균 대출일수] {avg_rent:.1f}일\n\n')
    f.write('[분야별 대출 건수]\n')
    for k,v in sorted(section_loan.items(),key = lambda x: x[1], reverse = True):
        f.write(f'{k}: {v}건\n')
    f.write('\n[대출자 유형별]\n')
    for k,v in sorted(type_loan.items(),key = lambda x: x[1], reverse = True):
        f.write(f'{k}: {v}건\n')
    f.write('\n[분석 결과]\n')
    f.write(f'최다 대출 도서: {best_book} ({best_book_count}건)\n')
    f.write(f'인기 분야 1위: {best_section} ({best_section_count}건)')












