import sys,random

rounds = 10000
wins = 0

random.seed()

# The "-n" commandline option makes us run without ever switching.
if len(sys.argv) > 1 and sys.argv[1] == "-n":
    swap = False
else:
    swap = True

for i in range(rounds) :

    # Generate random door contents
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)

    # Pick a door
    door_choice = random.randrange(3)
    print("Selecting door", door_choice)

    # Show a door with a goat
    for j, contents in enumerate(doors):
        if j != door_choice and contents == "goat":
            goat_door = j
            print("The host reveals a goat behind door", goat_door)
            break

    if swap:
        # Swap to the other door
        for j, contents in enumerate(doors):
            if j != door_choice and j != goat_door:
                swap_to = j
                print("Swapping to door", swap_to)
    else:
        swap_to = door_choice

    if doors[swap_to] == "car":
        wins += 1
        print("You won the car!!")
    else:
        print("Sorry, but you're stuck with a goat")

print("You played", rounds, "rounds, and won", wins, "of them!")

