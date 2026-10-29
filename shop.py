from classes import Item, Player, add_item


small_medicine = Item("Small Medicine",1,"health",15,0,30)
medium_medicine = Item("Medium Medicine",1,"health",30,0,60)
large_medicine = Item("Large Medicine",1,"health",45,0,100)
Bead = Item("Bead", 1, "health", 9999, 0, 300)
Snuff_Bull = Item("Snuff Bull", 1, "sp", 30, 0, 60)
SP_Bead = Item("SP Bead", 1, "sp", 50, 0, 100)
SP_Artifact = Item("SP Artifact", 1, "sp", 100, 0, 100),


shop_items = [small_medicine, medium_medicine, large_medicine, Bead, Snuff_Bull, SP_Bead, SP_Artifact]

def shop_display():
    print(r"""
==========================
  _____ __ __   ___   ____  
 / ___/|  |  | /   \ |    \ 
(   \_ |  |  ||     ||  o  )
 \__  ||  _  ||  O  ||   _/ 
 /  \ ||  |  ||     ||  |   
 \    ||  |  ||     ||  |   
  \___||__|__| \___/ |__|   
===========================      
""")

def show_items(item_list):
    print("=======ITEMS=======")
    for index, item in enumerate(item_list):
        print(f"{index + 1} - {item.name} | Cost: {item.price}")
    print("===================")
    print(f"{len(item_list) + 1} - Return")

def inspect_item(shop_items):
    while True:
        try:
            selection = int(input("What would you like to inspect?\n"))
        except ValueError:
            print("Please enter a valid input!")
        else:
            if 1 <= selection <= len(shop_items):
                item = shop_items[selection-1]
                print(f"""
Item: {item.name}
Cost: {item.price}
Type: {item.type}
Effect: {item.effect}
""")
                continue
            elif selection == (len(shop_items)+1):
                break
            else:
                print("Please enter a valid input!")
def buy_items(shop_items, Makoto):
    while True:
        try:
            selection = int(input("What would you like to buy?\n"))
        except ValueError:
            print("Please enter a valid input!")
        else:
            if 1 <= selection <= len(shop_items):
                if shop_items[selection-1].price > Makoto.coins:
                    print("Not enough coins!")
                    continue
                else:
                    confirm = input(f"Are you sure you want to buy {shop_items[selection-1].name}? Y/N\n")
                    if confirm.strip().lower() == "y":
                        add_item(Makoto, shop_items[selection-1])
                        Makoto.coins -= shop_items[selection-1].price
                        print(f"Successfuly bought {shop_items[selection-1].name}! You paid {shop_items[selection-1].price} coins.")
                        return
                    elif confirm.strip().lower() == "n":
                        continue
                    else:
                        print("Please enter a valid input!")
            elif selection == (len(shop_items)+1):
                break
            else:
                print("Please enter a valid input!")

def decide_action(shop_items, Makoto):
    while True:
        print(f"Coins: {Makoto.coins}")
        decision = input("What would you like to do?\n1 - Inspect Item\n2 - Buy Item\n3 - Check Inventory\n4 - Move to the next level\n")
        if decision == "1":
            show_items(shop_items)
            inspect_item(shop_items)
        elif decision == "2":
            show_items(shop_items)
            buy_items(shop_items, Makoto)
        elif decision == "3":
            Makoto.check_inventory()
        elif decision == "4":
            confirm = input("Are you sure you are ready to proceed? Y/N\n")
            if confirm.strip().lower() == "y":
                print("cool")
                return
            elif confirm.strip().lower() == "n":
                continue
            else:
                print("Please enter a valid input!")


def shop_call(Makoto):
    shop_display()
    decide_action(shop_items, Makoto)

if __name__ == "__main__":
    shop_call()
