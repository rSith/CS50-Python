def main():
    camelcase = input("camelCase: ")
    snakecase = camel_to_snake(camelcase)
    print(f"snake_case: {snakecase}")

def camel_to_snake(camelcase):
    snakecase = ""
    for ch in camelcase:
        if ch.isupper():
            snakecase += "_" + ch.lower()
        else:
            snakecase += ch
    return snakecase

main()
