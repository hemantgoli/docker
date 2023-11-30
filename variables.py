a = input("Enter first number: ")
b = input("Enter second number: ")

c=a
a=b
b=c

print("First = " + a)
print("second = " + b)



total_bill = int(input("total bill ?\n"))
persons = int(input("how many people to split the bill ?\n"))
tip = int(input("what percentage of tip?\n"))

each_persion_pay = (total_bill + (total_bill * (tip/100)))/persons


print("Each person should pay : $"+str(each_persion_pay))