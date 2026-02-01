import art
print(art.logo)

dict={}
continue_bidding = True

def max(dict):
    heigest = 0
    for bidder in dict :
        if dict[bidder]>heigest:
            heigest = dict[bidder]

    print(f"The Maximum bidder is {heigest}")
while continue_bidding:
    should_continue = input("Are their any biders if yes type 'YES' OR 'NO' ")
    if should_continue == "yes":
        name = input("Enter the name : ")
        price = int(input("Enter the price"))
        dict[name] = price
        print(dict)
    else:
        continue_bidding = False
        max(dict)