import datetime
day1 = datetime.date(2025,5,5)
diff = day1 - datetime.datetime.now().date()
print("어린이날까지 남은 기간:", diff.days,"일")
days = ['월','화','수','목','금','토','일']
day = datetime.date(2025,5,5)
print("그날은 "+days[day.weekday()]+"요일입니다.")