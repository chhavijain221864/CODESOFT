#Calculator Task(Codesoft task)
print(''' 
      + ADD
      - SUBTRACT
      * MULTIPLY
      / DIVIDE
    ''')
num1=int(input("Enter the  First Number:-"))
num2=int(input("Enter the  Second Number:-"))
opr=input("Enter the opr:-")
if opr=="+":
  print("Addition is:-",num1+num2)
elif opr=="-":
  print("Subtraction is:-",num1-num2)
elif opr=="*":
  print("Multiplication is:-",num1*num2)
elif opr=="/":
  print("Divide is:-" ,num1/num2)  
else:
  print("invalid operation.....")