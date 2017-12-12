"""Simulate the Monty Hall problem.

"""

import argparse, random

def simulate(num_doors, switch,num_car,num_open):
    """(int, bool): bool

    Carry out the game for one contestant.  If 'switch' is True,
    the contestant will switch their chosen door when offered the chance.
    Returns a Boolean value telling whether the simulated contestant won.
    """

    # Doors are numbered from 0 up to num_doors-1 (inclusive).
    # Randomly choose the doors hiding the prize.
    winning_door = random.sample(list(range(num_doors)), num_car)
    # The contestant picks a random door, too.
    choice = random.randint(0, num_doors-1)

    # The host opens num_open doors from the rest doors.
    closed_doors = list(range(num_doors))
    monty_doors=[x for x in closed_doors if x not in winning_door and x != choice]

    monty_choice=random.sample(monty_doors,num_open)


    #while True:
        # Monty randomly choose doors to open.
     #   door_to_remove = random.choice(closed_doors)
      #  if door_to_remove not in winning_door and door_to_remove !=choice:
       #     break


    # Remove the door from the list of closed doors.
    for i in monty_choice:
        closed_doors.remove(i)

    # Does the contestant want to switch their choice?
    if switch:
        # The contestant will choose from the remaining doors
        available_doors = list(closed_doors) # Make a copy of the list.
        available_doors.remove(choice)
        choice = random.choice(available_doors)


    # Did the contestant win?
    won = (choice in winning_door)

    return won


def main():
    # Get command-line arguments
    parser = argparse.ArgumentParser(
        description='simulate the Monty Hall problem')

    parser.add_argument('--doors', default=10, type=int, metavar='int',
                        help='number of doors offered to the contestant')

    parser.add_argument('--trials', default=10000, type=int, metavar='int',
                        help='number of trials to perform')

    parser.add_argument('--cars', default=2, type=int, metavar='int',
                        help='number of doors that have a car behind')

    parser.add_argument('--open', default=2, type=int, metavar='int',
                        help='number of doors that have a car behind')

    args = parser.parse_args()

    print('Simulating {} trials...'.format(args.trials))

    # Carry out the trials
    winning_non_switchers = 0
    winning_switchers = 0
    for i in range(args.trials):
        # First, do a trial where the contestant never switches.

        won = simulate(args.doors,False,args.cars,args.open)
        if won:
            winning_non_switchers += 1

        # Next, try one where the contestant switches.
        won = simulate(args.doors, True,args.cars,args.open)
        if won:
            winning_switchers += 1

    print('    Switching won {0:5} times out of {1} ({2}% of the time)'.format(
            winning_switchers, args.trials,
            (winning_switchers / args.trials * 100 ) ))
    print('Not switching won {0:5} times out of {1} ({2}% of the time)'.format(
            winning_non_switchers, args.trials,
            (winning_non_switchers / args.trials * 100 ) ))


if __name__ == '__main__':
    main()

