import random

#opening a text file to read a list of words into a list
my_file = open("hangman_words.txt", "r")
data = my_file.read()

#reads the file into a list, replacing new line ('\n') to empty string
words = data.replace('\n', ' ').split(" ")
#close file 
my_file.close()

#chose a random word for the list
chosen_word = random.choice(words)

display = ['_' for char in chosen_word]
attempts = 8
start_red = '\033[91m'
start_cyan = '\033[36m'
end = '\033[0m'
print(start_red + "-----------------------------")
print("Starting hang man game! \nMay luck be in your favour.")
print("-----------------------------" + end)

while attempts > 0 and '_' in display:
    print("You have " + '\033[95m' + '\033[1m' + str(attempts) + '\033[0m' + " tries left. \nMay luck be in your favour")
    print("\n" + ' '.join(display))
    user_guess = input("Input your guess: ").lower()
    print("-----------------------------")
    if user_guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == user_guess:
                display[index] = user_guess
    else:
        print("Unlucky, your guess wasn't in the word.")
        attempts -= 1
print(start_red + "------------------------------------------------------------" + end)
if '_' not in display:
    print("Luck was " + start_cyan + "indeed in your favour!" + end + " You've won. See you next game")
else:
    print("Seems like luck " + start_cyan + "wasn't" + end + " in your favour. \nYou've lost the game.")
    print("The word was " + "".join(chosen_word) + ". Better luck next time you're back.")

print(start_red + "------------------------------------------------------------" + end)
