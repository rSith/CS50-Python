def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    if not s[:2].isalpha():
        return False

    if not s.isalnum():
        return False

    i = 0
    while i < len(s) and s[i].isalpha():
        i += 1

    remaining = s[i:]
    if any(char.isalpha() for char in remaining):
        return False

    if remaining and remaining[0] == '0':
        return False

    return True


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
