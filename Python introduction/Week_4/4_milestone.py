
milestone = 0
while milestone == 0:
    # Ask the user for variables
    price_child_meal = float(input("\nWhat is the price of a child's meal?:"))
    price_adult_meal = float(input("What is the price of an adult's meal?:"))
    amount_child = int(input("How many children are there?:"))
    amount_adult = int(input("How many adults are there?:"))
    rate_tax = float(input("What is the sales tax rate?:"))
    rate_tip = float(input("What is the tip rate?:"))
    print()

    # Calculate the amounts
    subtotal = round((amount_child * price_child_meal) + (amount_adult * price_adult_meal),2)
    sales_tax = round(subtotal*(rate_tax/100),2)
    sales_tip = round((subtotal+sales_tax)*(rate_tax/100),2)
    amount_total = round((subtotal+sales_tax+sales_tip),2)
    print()

    # Show the variables
    print(f"Subtotal: ${subtotal}")
    print(f"Sales tax: ${sales_tax}")
    print(f"Tip: ${sales_tip}")
    print("______________________")
    print(f"Total: ${amount_total}")
    print()
    print(f"""
    Detail:
    price child meal: {round((amount_child*price_child_meal),2)}
    price adult meal: {round((amount_adult * price_adult_meal),2)}
    sales tax: {sales_tax}
    sales tip: {sales_tip}
    """)

    # Ask the user for the payment amount
    amount_payment = float(input("What is the payment amount?: "))

    # Calculate the change and display it
    amount_change = amount_payment-amount_total
    print()
    print(f"Change: ${amount_change:.2f}")
    print()

    result = input("It is okay the amount? Yes/No:").capitalize()

    if result == "Yes":
        print("\n Thank you for your purchase")
        milestone = 1
    elif result == "No":
        print("Enter the prices again\n")
        milestone = 0
        
    else:
        print("Error")