from os import system

print("\n"*100)

continue_auction = True

name_bid = {}

def find_highest_bidder(bid_dict):
    max_bid = 0
    max_name = ''
    for name in bid_dict:
        if bid_dict[name] > max_bid:
            max_bid = bid_dict[name]
            max_name = name
    print(f"Auction ends, {max_name} wins for ${max_bid} ")

while continue_auction:
    name = input("What is your name? ")
    while True:
        try:
            bid = int(input("How much are you willing to pay: $"))
            break
        except ValueError:
            print("It should be digits, not letters!")
            continue
    name_bid[name] = bid
    while True:
        ask = input("Are there any other bidders? (Y/N)").lower()
        if ask in ['y','n']:
            break
        else:
            print("Please enter only 'Y' or 'N'")
    if ask == 'n':
        find_highest_bidder(name_bid)
        continue_auction = False
    else:
        print("\n"*100)