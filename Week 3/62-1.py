"""
1. define the constants
2. request user input
3. compute the income tax
4. print the results
"""

# Intialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE

# Display the income tax with two zeros in the cents place
roundedTax = round(incomeTax, 2)
roundedTaxString = "{:.2f}".format(roundedTax)
print("The income tax is $" + roundedTaxString)
