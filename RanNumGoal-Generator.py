import random


# The Generator
def gen():
    try:
        num1 = int(input("Input Min = "))
        num2 = int(input("Input Max = "))
        num3 = int(input("What Number to Stop on? = "))
        # Generates until desired number
        generator = random.randrange(num1, num2)
        while generator != num3:
            print(generator)
            generator = random.randrange(num1, num2)
        else:
            print([generator], "Done!")
    except Exception as e:
        print("Did you input a digit?", e)
        gen()


# Asks if the user wants to run the program
def the_input():
    while True:
        statement = str(input("Run the Random Number Goal Generator? (Y/N)\n"))
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
