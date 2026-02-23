import random
color_list = ["R", "G", "B", "Y", "O", "W"]

def guess_brain(guess, secret):
    corect_pos = 0
    exist_incorect_pos = 0
    guess_copy = list(guess)
    secret_copy = list(secret)

    for i, color in enumerate(guess):
        if secret[i] == color:
            corect_pos += 1
            # guess_copy.pop(i)
            # secret_copy.pop(i)
            # print(secret_copy,guess_copy)
        if color in secret_copy:
            secret_copy.remove(color)
            exist_incorect_pos += 1
    else:
        print(
            f"wronge full answer corect posetion= {corect_pos} - esist in secret but not in right pleass= {exist_incorect_pos}",
        )


def guess_code():
    while True:
        guess = input("inter your guess of 4 color: ").upper().replace(" ", "")
        if len(guess) != 4:
            print("invaled range of input shoud be 4 char")
            continue
        for color in guess:
            if color not in color_list:
                print(f"invaled {color} not in secret color try agin ")
                continue
        else:
            break
    return guess


def main():
    time_try = 3
    secret_list = random.choices(color_list, k=4)
    print(secret_list)
    while time_try > 0:
        guess = guess_code()
        guess_list = list(guess)

        if guess_list == secret_list:
            print("you win :) ")
            break
        else:
            # print("try agin ")
            guess_brain(guess_list, secret_list)
            time_try -= 1
    else:
        print("you lose the code was",*secret_list)


main()
