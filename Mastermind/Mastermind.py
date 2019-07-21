from random import randint


def set_code(length):
    code = ""
    for i in range(length):
        rand_index = randint(0, len(colors))
        code += colors[rand_index] + ","

    return code


def how_right(code):
    code_arr = code.split(",")
    compute_arr = computer_code.split(",")
    black_pegs = 0
    white_pegs = 0

    for c in code_arr:
        if compute_arr.__contains__(c):
            if code_arr.index(c) == compute_arr.index(c):
                black_pegs = black_pegs + 1
            else:
                white_pegs = white_pegs + 1

    return [black_pegs, white_pegs]


colors = ("red", "green", "blue", "yellow", "white", "black")
guessed_right = False

computer_code = set_code(4)

print("Begin and enter your guess (e.g. red,yellow,green,blue).")

while not guessed_right:
    user_guess = input()
    correctness = how_right(user_guess)

    if user_guess == "debug":
        print(computer_code)
        guessed_right = True
    elif correctness[0] == 4:
        print("Correct!")
        break
    else:
        print(str(correctness[1]) + " white pegs and " + str(correctness[0]) + " black pegs")

