def get_delivery_price(deliv, weight):
    if deliv==2:
        if weight < 1.99:
            return 7.95
        else:
            extra=int(weight-1.99)
            return 7.99 + extra
    else:
        if weight < 1.99:
            return 9.95
        else:
            extra=int(weight-1.99)
            return 9.95 + extra

def display_title():
    print("ISQA 3900 Metro Courier Service Delivery Calculator ")
    print()

def main():
        display_title()
        while True:
            try:
                print("Base delivery of a 1lb package is $7.95 for a 2 hour or less delivery. Add $2 for 1 hour or less delivery")
                hour=int(input("Enter 2 for 2 hour or less or a 1 hour or less: "))

                if hour > 2 or hour < 0:
                    print('The delivery time indicator must be 1 or 2')
                    continue
                weight = float(input("Enter weight of package in POUND NUMBER ONLY PLEASE!. $1 per pound starting at 2 lbs up to 50 lbs:  "))
                if weight > 50 or weight < 0:
                    print("The company does not accept a single package over 50 lbs.")
                    continue
                print("The total delivery price for the package: ",get_delivery_price(hour, weight))
            except ValueError:
                print(" Invalid input.")
            print()
            choice = input("Continue (y/n)?: ")

            if choice == 'y':
                continue
            elif choice == 'n':
                print()
                print("Bye!")
                break
main()

