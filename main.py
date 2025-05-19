import random

clrs = ('red', 'blue', 'green', 'yellow', 'purple')

def ask_input():
    gsed_clrs = [input(f"Enter your {i + 1}. guessed color here: ") for i in range(len(clrs))]

    while not (len(gsed_clrs) == 5 and all(clr in clrs for clr in gsed_clrs)):
        print("Invalid input, try again.")
        print(gsed_clrs)
        gsed_clrs = [input(f"Enter your {i + 1}. guessed color here: ") for i in range(len(clrs))]
    
    return gsed_clrs

def is_correct(gsed: list[str], picked: list[str]):
    if gsed == picked:
        return True
    
    res = [''] * len(gsed)
    p_cp = picked.copy()

    for i in range(len(gsed)):
        if gsed[i] == picked[i]:
            res[i] = '🟢'
            p_cp[i] = None
    
    for i in range(len(gsed)):
        if res[i] == '':
            if gsed[i] in picked:
                res[i] = '🟡'
                p_cp[p_cp.index(gsed[i])] = None
            else:
                res[i] = '⚪'

    return res
    

def main():
    playing = True
    clrs_picked = [random.choice(clrs) for _ in range(5)]
    print(clrs_picked)

    while playing:
        gsed_clrs = ask_input()
        output = is_correct(gsed_clrs, clrs_picked)
        if output is True:
            print("Eltaláltad, nyertél!")
            playing = False
        else:
            print(output)

if __name__ == '__main__':
    main()