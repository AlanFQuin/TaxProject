grossIncome = float(input("Enter the gross income: "))

dependents = int(input("Enter the number of dependents: "))

dependentDeductions = dependents * 3000

taxRate = .20

taxIncome = (grossIncome * taxRate) - dependentDeductions

print("The income tax is $", taxIncome)













