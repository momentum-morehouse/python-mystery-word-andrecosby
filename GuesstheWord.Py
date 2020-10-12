import random


def Play_game():
    file_object = open('words.txt','r')
    words_list = file_object.readlines()
    random_word = random.choice(words_list)

#print(random_word)

greeting = str(input("Guess the Word Choose Your level of Difficulty. Easy, Medium, Hard: ").upper())
if greeting == "Easy":
    easy_list = [word for word in words_list if len(word) >= 4 and len(word) <= 6]
    random_word = random.choice(easy_list).strip()


elif greeting == "Medium":
    medium_list = [word for word in words_list if len(word) >= 6 and len(word) <= 8]
    random_word = random.choice(medium_list).strip()


elif greeting == "Hard":
    Hard_list = [word for word in words_list if len(word) >= 8 ]
    random_word = random.choice(Hard_list).strip()


else:
    print("Please enter Easy, Medium, Hard")

Print("The Random word Contains", len(random_word), "Letters")

Guesses_remaining = 8
Used_letters = []
Building_word = []
Building_Word_String = ''
Print("You Have", guesses_remaining, "Guesses Left, Keep Trying")

while Guesses_remaining >= 1:
    user_guess = str(input("Select a Letter: ").lower())
    if user_guess in random_word.lower():
        print(user_guess)
        original_len = len(random_word)
        print(user_guess)
        print("_ "*original_len)
        print(random_word.index(user_guess))
        x = random_word.index(user_guess)
        Building_word = []
        