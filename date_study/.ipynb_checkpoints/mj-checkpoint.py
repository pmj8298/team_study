import datetime
day1 = datetime.datetime.now().date()
day2 = datetime.date(2025,12,25)
diff = (day2 - day1).days
days = ['월','화','수','목','금','토','일']
print(f'{day1}에서 크리스마스까지 {diff}일 남았습니다 그 날은 {days[day2.weekday()]}요일 입니다')