import csv

with open('weather.csv','r',encoding='utf-8') as f:
    data = csv.DictReader(f)
    data = list(data)

# 전체 관측
total_day = len(data)

# 비온날
rainy_day = 0
for row in data:
    rain = int(row['강수량'])
    if rain > 0 :
        rainy_day += 1
rain_percent = rainy_day/total_day * 100
# print(rainy_day)
# print(rain_percent)

#도시별 갯수 합계
city_temp_count = {}
for row in data:
    city = row['도시']
    temp_high = int(row['최고기온'])
    city_temp_count[city] = city_temp_count.get(city,0) + 1

# 도시별 평균 최고기온 합계
city_temp_high = {}
for row in data:
    city = row['도시']
    temp_high = int(row['최고기온'])
    city_temp_high[city] = (city_temp_high.get(city,0) + temp_high)

#도시별 최고기온평균 dict
city_values = zip(city_temp_count.values(),city_temp_high.values())
city_values = list(city_values)
i = 0
avg_temp_list = []
for i in range(len(city_values)):
    avg_temp_city = city_values[i][1]/city_values[i][0]
    avg_temp_list.append(avg_temp_city)
# print(avg_temp_list)

high_temp_avg = zip(city_temp_count.keys(),avg_temp_list)
high_temp_avg = dict(high_temp_avg)

# print(high_temp_avg)

# 가장 더웠던 날
hottest_day = ''
hottest_city = ''
hottest_temp = 0

for row in data:
    day = row['날짜']
    city = row['도시']
    temp = int(row['최고기온'])
    if temp > hottest_temp:
        hottest_city = city
        hottest_day = day
        hottest_temp = temp
# print(hottest_city,hottest_day,hottest_temp)

#일교차가 가장큰날
gap_day = ''
gap_city =''
gap_temp = 0
for row in data:
    day = row['날짜']
    city = row['도시']
    temp = int(row['최고기온']) - int(row['최저기온'])
    if temp > gap_temp:
        gap_city = city
        gap_day = day
        gap_temp = temp
# print(gap_city,gap_day,gap_temp)


with open('report03.txt','w',encoding='utf-8') as f:
    f.write('=== 여름 날씨 분석 리포트 (2025.06 ~ 08) ===\n\n')
    f.write(f'[전체 관측] {total_day}건\n')
    f.write(f'[비 온 날] {rainy_day}건 ({rain_percent:.1f}%)\n\n')
    f.write('[도시별 평균 최고기온]\n')
    for row in sorted(high_temp_avg.items(),key = lambda x: x[1], reverse = True):
        f.write(f'{row[0]}: {row[1]:.1f}℃\n')
    f.write('\n[분석 결과]\n')
    f.write(f'가장 더웠던 날: {hottest_day} {hottest_city} ({hottest_temp}℃)\n')
    f.write(f'일교차가 가장 큰 날: {gap_day} {gap_city} ({gap_temp})℃)')