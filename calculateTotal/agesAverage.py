ages =[2, 13, 56, 78, 44, 27, 19, 11]
sum = 0
length = len(ages)
for number in range(len(ages)):
  sum += ages[number]
average = sum/length
print(average)
