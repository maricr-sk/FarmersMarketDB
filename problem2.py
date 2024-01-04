import random


def read_dict(filename):
    words = []
    with open(filename, 'r') as file:
        for line in file:
            words.append(line.lower().strip())
    file.close()
    return words


if __name__ == "__main__":
    words = read_dict("dict.txt")

    rand = random.randint(0, len(words))
    word = list(words[rand])
    print("Welcome to Hangman! You have 5 wrong guesses. Your secret word is below. Time to start guessing, good luck!")
    count = 5
    check = True
    se = set()
    inte = 0
    nice = "".join(word)
    guess = []
    n = 0

    for n in range(len(word)):
        guess = guess + ["_ "]
        n = n + 1
    print("".join(guess))
    
    while count > 0 and check:
        if (inte == len(word) - 1):
            check = False
        inp = input("\nYour guess: ")
        if inp in word and inp not in se:
            i = 0
            for t in word:
                if inp is t:
                    guess[i] = t + " "
                    se.add(t)
                    inte = inte + 1
                i = i + 1
            print("\nNice!")
        else:
            count = count - 1
            if count > 1:
                print("\nWrong! You have", count, "wrong guesses left. Try again:")
            elif count == 1:
                print("\nWrong! You have 1 wrong guess left. Choose carefully:")
        print("".join(guess))
    if count == 0:
        print("\nSorry you lost! This is the word: \n", nice)
    else:
        print("\nYAY you won!!!")