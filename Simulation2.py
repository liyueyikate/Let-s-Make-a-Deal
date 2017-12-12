"""Simulate the Monty Hall problem.

"""

import argparse, random

def simulate(num_doors, switch,num_car,num_open):
    """(int, bool,int): bool
    Simulate the game for one contestant.  Given the number of doors in total and the number of doors Monty
    opens, the contestant can choose whether to switch. Returns a Boolean value telling whether the
    simulated contestant won.
    """

    # Doors are numbered from 0 up to num_doors-1 (inclusive).
    # Randomly choose the doors hiding the car.
    winning_door = random.sample(list(range(num_doors)), num_car)

    # The contestant picks a random door.
    choice = random.randint(0, num_doors-1)

    # The host opens num_open doors from the rest doors.
    closed_doors = list(range(num_doors))
    monty_doors=[x for x in closed_doors if x not in winning_door and x != choice]
    monty_choice=random.sample(monty_doors,num_open)

    # Remove the door from the list of closed doors.
    for i in monty_choice:
        closed_doors.remove(i)

    # If switch, the contestant chooses from the closed doors
    if switch:
        closed_doors.remove(choice)
        choice = random.choice(closed_doors)

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
        # simulate not switching.
        won = simulate(args.doors,False,args.cars,args.open)
        if won:
            winning_non_switchers += 1

        # simulate switching.
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

