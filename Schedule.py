from datetime import date, timedelta
start = date(2018, 7, 11)
for d in range(7):
    cur = start + timedelta(days=d)
    print(cur)


from datetime import date, timedelta
week = "月火水木金土日"
start = date(2018, 7, 11)
for d in range(7):
    cur = start + timedelta(days=d)
    wd = cur.weekday()
    print(cur, week[wd])