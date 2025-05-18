import random

clrs = ('red', 'blue', 'green', 'yellow', 'purple')

def ask_input():
    gses = input("Input your list of colors here [clr1, clr2, ... clr5]: ")
    gsed_clrs = gses.split()

    while len(gsed_clrs) != 5:
        print("Invalid input, try again.")
        gses = input("Input your list of colors here [clr1, clr2, ... clr5]: ")
    
    return gsed_clrs

def compare_input(gsed: list[str]):
    


def main():
    clrs_picked = [random.choice(clrs) for _ in range(5)]
    print(clrs_picked)

    gsed_clrs = ask_input()


if __name__ == '__main__':
    main()