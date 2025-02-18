import datetime
# 예제 3번
# 오늘부터 어버이날 며칠 남았는지, 무슨 요일인지
parents = datetime.date(2025,5,8)
today = datetime.datetime.now().date()
count = parents - today
print(f"오늘부터 어버이날까지 {count.days}일 남았습니다.")

days = ['월', '화', '수', '목', '금', '토', '일']
print("어버이날은 " + days[parents.weekday()] + "요일 입니다.")