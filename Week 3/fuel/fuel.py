def main():
    while True:
        try:

            fraction = input("Fraction: ").strip()

            parts = fraction.split('/')

            if len(parts) != 2:
                raise ValueError("Invalid fraction format")

            x, y = parts

            x = int(x)
            y = int(y)


            if x < 0 or y < 0:
                raise ValueError("X and Y must be positive integers")

            if y == 0:
                raise ZeroDivisionError("Y cannot be 0")

            if x > y:
                raise ValueError("X cannot be greater than Y")

            percentage = round((x / y) * 100)

            if percentage <= 1:
                print("E")
                break
            elif percentage >= 99:
                print("F")
                break
            else:
                print(f"{percentage}%")
                break

        except (ValueError, ZeroDivisionError):

            continue

if __name__ == "__main__":
    main()
