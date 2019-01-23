import random


# The Generator
def gen():
    try:
        num1 = int(input("Input Min = "))
        num2 = int(input("Input Max = "))
        num3 = int(input("How Many Results? = "))
        # Generates until desired number of results
        for generator in range(num3):
            generator = random.randrange(num1, num2)
            print(generator)
    except Exception as e:
        print("Did you input a digit?", e)
        gen()


# Asks if the user wants to run the program
def the_input():
    while True:
        statement = str(input("Run the Random Number Generator? (Y/N)\n"))
        if statement == 'y':
            gen()
        elif statement == 'n':
            print("Closing...\n")
            exit()
        else:
            print("Unknown Command\n")
            continue
        return


the_input()
