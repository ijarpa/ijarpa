# Shopping Cart

# Libraries
import numpy as np
import pandas as pd

# Code for shopping cart
print("Welcome to the Shopping Cart Program!")

shopping = 1
cart = []
prices = []

while shopping != 5:

    dict = {
        "item": cart,
        "price": prices
    }

    df = pd.DataFrame(dict, index=np.arange(1,len(cart)+1))

    print("""
###################################
Please select one of the following:
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Quit
###################################
""")
    shopping = int(input("Please enter an action: "))
    print()

    if shopping == 1:
        item = input("What item would you like to add?: ")
        cart.append(item)
        print(f"You add to the cart: {cart[-1]}")
        price = float(input("how much cost the product that you added to the cart?: "))
        prices.append(price)
        print(f"You add to the cart: {cart[-1]} and the prices is: {prices[-1]:.2f}")
    
    elif shopping == 2:
        print("You have the following items in the cart:")
        print(df)
        #for x in range(0,len(cart)):
        #    cart_2 = cart[x]
        #    price_2 = prices[x]
        #    print(cart_2, price_2)
        
        move_on = input("press a key to continue")

    elif shopping == 3:
        number_removed = int(input("Enter the number of the item that you want to remove: "))
        number_removed = number_removed-1
        cart.pop(number_removed)
        prices.pop(number_removed)
        #print(cart[number_removed])

    elif shopping == 4:
        total = df['price'].sum()
        print(f"Your total is: ${total}")
        print()
        move_on = input("press a key to continue")

    elif shopping == 5:
        print("Thank you for visiting my shopping cart")
        shopping = 5
