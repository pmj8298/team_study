#1번 
import datetime
inp = input("생일을 년월일 형식으로 입력해주세요")

year = inp[:4]
year = int(year)

month = inp[4:6]
month = int(month)

day = inp[6:]
day = int(day)

birth = datetime.date(year,month,day)
today = datetime.datetime.now().date()
howlong = (today - birth).days 

days = ['월','화','수','목','금','토','일']
print("당신의 생일은 " + days[birth.weekday()]+"요일 입니다")
print("오늘로 태어난 지",howlong," 일 입니다")
print(birth)
print(today)