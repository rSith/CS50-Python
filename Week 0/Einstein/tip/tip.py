def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d_= d.replace("$","")
    return float(d_)

def percent_to_float(p):
    p_ = p.replace("%","")
    return float(p_)/100

main()