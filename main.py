import random

words = ['ricks', 'morty', 'space', 'ships', 'robot', 'pizza', 'lived', 'drink', 'phone']

lives = 9

secret_word = random.choice(words)

clue = list('?????')

heart = u'\u2764'

guessed_word_correctly = False


def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1

while lives > 0:
    print(clue)
    print('elämiä jäljellä: ', heart * lives)
    
    guess = input('arvaa kirjain tai koko sana: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('väärin, menetit elämän.')
        lives -= 1

if guessed_word_correctly:
    print('VOITIT! Sana oli', secret_word)

else:
    print('Hävisit! :( Sana oli', secret_word)
