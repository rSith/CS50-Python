def main():
    time = input("What time is it? ")
    time_as_float = convert(time)

    if 7 <= time_as_float <= 8:
        print("breakfast time")
    elif 12 <= time_as_float <= 13:
        print("lunch time")
    elif 18 <= time_as_float <= 19:
        print("dinner time")
    else:
        return


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    minutes_as_float = minutes/60

    return hours + minutes_as_float

if __name__ == "__main__":
    main()
