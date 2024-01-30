numDays = int(input("How many day's temperature? "))
total = 0
temp = []
for i in range(numDays):
    nextDay = int(input("Day " + str(i+1) + "'s high temp:"))
    temp.append(nextDay)
    total += temp[i]
    
average = round(total/numDays, 2)
print("\nAverage = " + str(average))

above = 0
for i in temp:
    if i > average:
        above += 1
        
print(str(above) + " day(s) above average")