purchase_price = float(input("Enter the purchase price of the computer: "))

down_payment = 0.10 * purchase_price
balance = purchase_price - down_payment
monthly_payment_rate = 0.05
annual_interest_rate = 0.12

month = 0

print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format("Month", "Balance", "Interest", "Principal", "Payment", "Remaining Balance"))

while balance > 0:
    month += 1

    interest = (balance * annual_interest_rate) / 12
    payment = monthly_payment_rate * (purchase_price - down_payment)
    principal = payment - interest
    
    # Adjust final payment if it's more than remaining balance.
    if payment > balance:
        payment = balance
        principal = payment - interest

    balance -= payment
    
    print("{:<10} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f}".format(month, balance + payment, interest, principal, payment, balance))
