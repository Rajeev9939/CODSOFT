print("****************  CALCULATOR  ***************")
print("\n")

num1 = float(input("Enter the first number here:"))
num2 = float(input("Enter the second number here:"))

print(
  "Enter 1 for 'Addition' \nEnter 2 for 'Subtraction' \nEnter 3 for 'Multiply' \nEnter 4 for 'Division'"
)

Entered_number = int(input("choice a number from 1 to 4:"))

if Entered_number == 1:
  print("Addition of your first and second number is : ", num1 + num2)

elif Entered_number == 2:
  print("Subtraction of your first and second number is :", num1 - num2)

elif Entered_number == 3:
  print("Multiply of your first and second number is :", num1 * num2)

elif Entered_number == 4:
  print("division of your first and second number is :", num1 / num2)

else:
  print("invaild input")