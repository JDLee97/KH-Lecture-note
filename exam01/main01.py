import csv

with open('sales.csv','r',encoding='utf-8') as f:
    data = csv.DictReader(f)
    data = list(data)

# 전체 매출
total = 0
for row in data:
    qty = int(row['수량'])
    price = int(row['단가'])
    total += qty * price
# print(total)

# 메뉴별 판매량
qty_by_menu = {}
for row in data:
    menu = row['메뉴']
    qty = int(row['수량'])
    qty_by_menu[menu] = qty_by_menu.get(menu,0) + qty
# print(qty_by_menu)

# 카테고리별 매출
qty_by_category = {}
for row in data:
    category = row['카테고리']
    qty = int(row['수량'])
    price = int(row['단가'])
    qty_by_category[category] = qty_by_category.get(category,0) + qty*price

# print(qty_by_category)

# 월별 매출
sales_by_month = {}
for row in data:
    date = row['날짜'][0:7]
    qty = int(row['수량'])
    price = int(row['단가'])
    sales_by_month[date] = sales_by_month.get(date,0) + qty*price

# print(sales_by_month)

# 가장 많이 팔린 메뉴
best_menu = ''
max_value_menu = -1
for k,v in qty_by_menu.items():
    if max_value_menu < v:
        best_menu = k
        max_value_menu = v
# print(best_menu, max_value)

# 매출 1위 카테고리
best_category = ''
max_value_cate = -1
for k,v in qty_by_category.items():
    if max_value_cate < v:
        best_category = k
        max_value_cate = v
# print(best_category, max_value)

# 리포트에 저장
with open('report01.txt','w',encoding='utf-8') as f:
    f.write('=== 파이빈 카페 매출 리포트 (2025.01 ~ 03) ===\n\n')
    f.write(f'[전체 매출] {total :,}원\n\n')
    f.write('[메뉴별 판매량]\n')
    for k,v in sorted(qty_by_menu.items(),key =lambda x: x[1], reverse=True):
        f.write(f'{k}: {v}잔\n')
    f.write('\n[카테고리별 매출]\n')
    for k,v in sorted(qty_by_category.items(),key =lambda x: x[1], reverse=True):
        f.write(f'{k}: {v:,}원\n')
    f.write('\n[월별 매출]\n')
    for k,v in sales_by_month.items():
        f.write(f'{k}: {v:,}원\n')
    f.write('\n[분석 결과]\n')
    f.write(f'가장 많이 팔린 메뉴: {best_menu} ({max_value_menu}잔)\n')
    f.write(f'매출 1위 카테고리: {best_category} ({max_value_cate:,})원\n')