import random


# The Generator
def gen():
    num1 = int(input("Input Min = "))
    num2 = int(input("Input Max = "))
    num3 = int(input("What Number to Stop on? = "))
    # Generates until desiered number
    generator = random.randrange(num1, num2)
    while generator != num3:
        print(generator)
        generator = random.randrange(num1, num2)
    else:
        print([generator], "Done!")


# Asks if the user wants to run the program
def theinput():
    while True:
        statement = str(input("Run the Random Number Goal Generator? (Y/N)\n"))
        if statement == ('y'):
            gen()
        elif statement == ('n'):
            print("Closing...\n")
            exit()
        else:
            print("Unknown Command\n")
            continue
        return


theinput()
