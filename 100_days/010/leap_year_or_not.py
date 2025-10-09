def is_leap_year(year):
    """Takes an year and return True if year is leap"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return (True)
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    print("Let's check if year is a leap or not?")
    try:
        while True:
            try:
                year_to_check = int(input("What year should I check? "))
                break
            except ValueError:
                print("Please enter digits, like 0000, try again!")
                continue
        if is_leap_year(year_to_check) == True:
            print(f"{year_to_check} is a leap year")
        else:
            print(f"{year_to_check} isn't a leap year")
    except KeyboardInterrupt:
        print("\nBye")

if __name__ == "__main__":
    main()