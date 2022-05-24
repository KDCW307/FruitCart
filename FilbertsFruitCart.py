""" This program is to count numbers based off of user input.  """
import time
import sys

def main():
    print('Welcome to Filbert\'s Fruit Cart!')
    time.sleep(2)
    print('Today\'s special is watermelons.')
    time.sleep(2)
    print('We supply the tristate area with the freshest fruits straight to your door daily!')
    time.sleep(2)
    print('After filling out the following form you will be delievered the best fruit according to your needs...')
    time.sleep(2)

    while True:
        try:
            starting_value = int(input('How many watermelons do you currently have?: '))
            end_value = int(input('How many watermelons would you like to order?: '))
            if starting_value >= end_value:
                print('Hmmm, you seem confused. Please enter a number greater than the number of melons you currently have.')
            elif starting_value <= end_value:
                break
        except ValueError:
            print('Hmmm... I\'m not sure what that means... Please enter a number.')
    while True:
        try:
            step_value = int(input('How many melons do you want a day?: '))
            break
        except ValueError:
            print('Sorry I don\'t understand I need an actual number.')

    print('Here is the amount of watermelons you will have a day until your order is complete:')
    for x in range(starting_value, end_value, step_value):
        print(x)
        time.sleep(1)

    print('Thank you for shopping with Filbert\'s Fruit Cart!')
    time.sleep(2)
    print('All sales and orders are final.')
    time.sleep(2)
    print('We take no responsibilty for any hardship experienced from eating too much fruit.')
    time.sleep(2)
    sys.exit()


if __name__ == '__main__':
    main()
