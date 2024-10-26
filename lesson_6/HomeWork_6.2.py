number = input("Enter number: ")
number = int(number)

days = (number // 60 // 60 // 24)    # дни
days = str(days)

hours = (number // 60 // 60 % 24)    # часы
hours = str(hours)

minutes = (number // 60 % 60)        # минуты
minutes = str(minutes)

seconds = (number % 60)              # секунды
seconds = str(seconds)

finish = days + " days, " + hours.zfill(2) + ':' + minutes.zfill(2) + ':' + seconds.zfill(2)
print(finish)