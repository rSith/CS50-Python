d = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

d = d.lower().strip()

match d:
    case "42" | "forty two" | "forty-two" | "fortytwo":
        print("Yes")
    case _:
        print("No")

