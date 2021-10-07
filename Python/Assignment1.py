temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) :\n ")
degree = int(temp[:-1])
input_convention = temp[-1]

if input_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  output_convention = "Fahrenheit"
elif input_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  output_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", output_convention, "is", result, "degrees.")
