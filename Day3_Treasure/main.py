print("Welcome to Treasure Island. Your mission is to find the treasure.")
direction = input("You are at end of a hallway do you turn right or left?\n")
gameover = "You are dead. Gameover."
if direction == "left":
    decision = input("Now do you swim or wait?\n")

    if decision == "wait":
        door = input("What color door do you pick Blue or Yellow?\n")

        if door == "yellow":
            print("You won!")
        else:
            print(gameover)

    else:
        print(gameover)
else:
    print(gameover)