list=[2,7,9,3,1,4]

print("Original list ",list)
sum=0

for number in list:

    sum+=number

avr=sum/len(list)

print("Sum=",sum,'and average=',avr)

list.sort()

print('smallest elment is',list[0])
print("Largest number is :",list[-1])


