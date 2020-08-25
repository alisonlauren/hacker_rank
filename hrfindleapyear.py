import calendar

def is_leap(num):
    if num % 4 == 0 and num % 400 == 0:
        return True
    else:
        return False

    


def main():

    try:
        a = int(input("Which year should I process? ").replace(',','.'))
        b = calendar.isleap(a)
        if not b:
                print(a,"is not a leap year")
        else:
                print(a,"is a leap year")
    except ValueError:
        print("Invalid input!")
        main()

main()