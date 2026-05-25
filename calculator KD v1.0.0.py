print("*************CALCULATOR****************")
num1 = int(input("enter 1st number to contune: "))
num2 = int(input("enter 2nd number to contune: "))
print("what you want to do?")
print("1. '+' (add)")
print("2. '-' (subtract)")
print("3.' ×'(multuply)")
print("4. '÷'(divide)")
ques = int(input("enter number only \n>>>: "))
if ques == 1:
    print("the addition of", num1, "+", num2, "is", num1 + num2)
elif ques == 2:
    print("the subtraction of", num1, '-', num2, "is", num1-num2)
elif ques == 3:
    print("the multiplication of", num1, "×", num2, "is", num1*num2)
elif ques == 4:
    print("the divison of", num1, "÷", num2, "is", num1/num2)          