import random


def gen():
    num1 = int(input("Input Min = "))
    num2 = int(input("Input Max = "))
    num3 = int(input("How Many Results? = "))
    for generator in range(num3):
        generator = random.randrange(num1, num2)
        print(generator)


def theinput():
    while True:
        statement = str(input("Run the Random Number Generator? (Y/N)\n"))
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
