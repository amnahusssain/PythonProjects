heading= "Welcome to this calculator"
h1=(heading.title())
print(h1.center(50,"-"))

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))


print("Enter a number for a appropriate operation as mentioned below:\n")
print("Enter \"1\" for Addition")
print("Enter \"2\" for Subraction")
print("Enter \"3\" for Division")
print("Enter \"4\" for Multiplication")
print("Enter \"5\" for Floor Division")
print("Enter \"6\" for Power")
print("Enter \"7\" for Modulus")
print("\n")
operation=int(input("Select the number: "))
print("\n")

match operation:
 case 1:
  print("The addition of ",num1," and ",num2," results in ",num1+num2)
 case 2:
  print("The subtraction of ",num1," and ",num2," results in ",num1-num2)
 case 3:
  print("The division of ",num1," by ",num2," results in ",num1/num2)
 case 4:
  print("The multiplication of ",num1," and ",num2," results in ",num1*num2)
 case 5:
  print(f"The floor division of {num1} and {num2} results in {num1//num2}")
 case 6:
  print(f"The power of {num1} to {num2} results in {num1**num2}")
 case 7:
  print(f"The reminder you get after dividing {num1} to {num2} is {num1%num2}")
 case _:
  print("Select a appropriate number")

  print("\n")



