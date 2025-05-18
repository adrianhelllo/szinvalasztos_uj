import random

clrs = ('red', 'blue', 'green', 'yellow', 'purple')

def ask_input():
    gsed_clrs = [input(f"Enter your {i + 1}. guessed color here: ") for i in range(len(clrs))]

    while len(gsed_clrs) != 5 or not all(clr in gsed_clrs for clr in clrs):
        print("Invalid input, try again.")
        print(gsed_clrs)
        gsed_clrs = [input(f"Enter your {i + 1}. guessed color here: ") for i in range(len(clrs))]
    
    return gsed_clrs

def is_correct(gsed: list[str], picked: list[str]):
    res = []


    if gsed != picked:
        for clr in gsed:
            if clr in picked:
                if gsed[clr] == picked[clr]:
                    res.append('🟢')
                else:
                    res.append('🟡')
            else:
                res.append('⚪')
        return res
    else:
        return True


    




def main():
    clrs_picked = [random.choice(clrs) for _ in range(5)]
    print(clrs_picked)

    gsed_clrs = ask_input()

    while not is_correct(gsed_clrs, clrs_picked):
        print(is_correct)
    
    print("Eltaláltad, nyertél!")





if __name__ == '__main__':
    main()