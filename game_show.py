from random import shuffle, choice


def main():
    switch_win = 0
    dont_switch_win = 0
    for i in range(1_000_000):
        # lists the possibilities of goat, goat, or a car
        list_of_possibilities = ['goat', 'goat', 'car']
        # Shuffles so it doesn't stay in the same place (door)
        shuffle(list_of_possibilities)
        door_a, door_b, door_c = [list_of_possibilities[i] for i in range(0,3)]

        choices = {'door_a': door_a, 
                    'door_b': door_b,
                    'door_c': door_c
                    }

        print("Choose a door")
        cpu_input = choice(list(choices.keys()))
        print(cpu_input)

        # Removes the user's door from the list of doors to avoid conflict
        del choices[cpu_input]
        for key, val in choices.items():
            # If the other doors have a goat, it will open the door with a goat or if both it will just choose one of them
            if val == 'goat':
                print(f"{key} has a goat in it.")
                # Deletes the door with the goat in it to leave one remaining door to see if the cpu will win
                del choices[key]
                break
            pass

        list_of_choices = ['y', 'n']
        print("Would you like to switch or stay with your original door?")
        cpu_input2 = choice(list_of_choices)
        print(cpu_input2)
        for key1, val1 in choices.items():
            print(key1, val1)
            if cpu_input2 == 'y':
                # If the last door has a car and the cpu picks to switch, it will win
                if val1 == 'car':
                    print("You win")
                    switch_win += 1
                else:
                    print("You lose")
            if cpu_input2 == 'n':
                # If the last door has a car and the cpu chose not to switch, it will lose
                if val1 == 'car':
                    print("You lose")
                else:
                    print("You win")
                    dont_switch_win += 1
    percent_switched = (switch_win / (switch_win + dont_switch_win)) * 100 
    percent_dont_switched = (dont_switch_win / (switch_win + dont_switch_win)) * 100
    print(f"Number of Wins when you switched: {switch_win}")
    print(f"Number of Wins when you didn't: {dont_switch_win}")
    print(f"Percentage chance if you switch: {percent_switched} %")
    print(f"Percentage chance if you don't switch: {percent_dont_switched} %")


main()

















