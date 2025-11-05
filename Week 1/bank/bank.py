Greeting = input("Greeting: ").strip().capitalize()

if Greeting.startswith("Hello"):
    print("$0")
elif Greeting.startswith("H"):
    print("$20")
else:
    print("$100")
