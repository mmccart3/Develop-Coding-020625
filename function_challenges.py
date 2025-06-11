# def take_order(topping1, topping2, topping3):
#     global order_count
#     print(f"Your order is a pizza with {topping1}, {topping2} and {topping3}. Your order is {order_count}")
#     order_count += 1

# order_count = 1

# take_order("Ham", "Mushroom", "Extra Cheese")
# take_order("Ham", "pineapple", "banana")
# take_order("chicken", "mushroom", "extra cheese")

def withdraw_cash(PIN, amount):
    global account_balance, stored_PIN
    if PIN == stored_PIN and amount <= account_balance:
        account_balance -= amount
        print(f"{amount} being dispensed. Your new account balance is {account_balance}")
    else:
        print(f"Either insufficient funds or incorrect PIN")
stored_PIN = 9876
account_balance = 500

withdraw_cash(9876, 200)
withdraw_cash(9875,200)
withdraw_cash(9876, 250)
withdraw_cash(9876, 150)