def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")
    
print ("We can just give the functions numbers directly:")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 110
amount_of_crackers = 550

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can fo math inside too:")
cheese_and_crackers(1453+1352, 6207+2516)

print("And we can combine the two, varaibles and math:")
cheese_and_crackers(amount_of_cheese+24682, amount_of_crackers+24537)