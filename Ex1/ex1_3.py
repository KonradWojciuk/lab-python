def calculate_tax(income):
    if income <= 50000:
        tax = income * 0.12
    else:
        tax = 50000 * 0.12 + (income - 50000) * 0.32
    return tax

def main():
    income_type = input("Enter 'M' for monthly income or 'Y' for yearly income: ")
    if income_type.upper() == 'M':
        monthly_income = float(input("Enter your monthly income: "))
        yearly_income = monthly_income * 12
    elif income_type.upper() == 'Y':
        yearly_income = float(input("Enter your yearly income: "))
    else:
        print("Invalid input. Please enter 'M' or 'Y'.")
        return
    
    tax_amount = calculate_tax(yearly_income)
    print("Your yearly income tax is:", tax_amount)

if __name__ == "__main__":
    main()
