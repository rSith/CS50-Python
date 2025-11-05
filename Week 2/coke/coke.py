print("Amount Due: 50")

amount_due = 50
coin_type = [25,10,5]

while amount_due > 0:
    coin = int(input("Insert Coin: "))
    if coin in coin_type:
        amount_due = amount_due - coin
        if amount_due == 0:
            print("Change Owed: 0")
        elif amount_due < 0:
            change_owed = abs(amount_due)
            print(f"Change Owed: {change_owed}")
        else:
            print(f"Amount Due: {amount_due}")

    else:
        print(f"Amount Due: {amount_due}")

