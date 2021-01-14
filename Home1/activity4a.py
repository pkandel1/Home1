def main():
    display_title()
    get_grade()
def display_title():
        print("ISQA 3900 Letter Grade Calculator")
        print()

def get_grade():
    while True:
        # get input from the user
            total_points = int(input("Enter total number points earned: "))
            if  total_points  >= 920 and total_points  <= 1000:
                print ("Letter grade: A")
            elif total_points  >= 880 and  total_points  <= 9199:
                print ("Letter grade: B+")
            elif total_points  >= 820 and  total_points  <= 8799:
                print  ("Letter grade: B")
            elif total_points  >= 780 and  total_points  <= 8199:
                print ("Letter grade: C+")
            elif total_points  >= 700 and   total_points <= 7799:
                print ("Letter grade: C")
            elif total_points  >= 600 and  total_points  <= 6999:
                print( "Letter grade: D")
            elif total_points  <= 600 and  total_points  >= 0:
                print("Letter grade: F")
            else:
                print("The point you must typed  has be  from 0 - 1000.")
            print()
            choice = input("Continue (y/n)?: ")
            if choice == 'y':
                continue
            elif choice == 'n':
                print()
                print("Bye!")
                break



main()