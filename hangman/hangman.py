import random

file = open('words.txt','r')
words = random.choice(file.readlines())

split_char = []
hyphen = ['_']
user_entries = []

for char in words:
    if char == '\n':
        continue
    split_char.append(char)

hyphen_word = hyphen * len(split_char)
print(hyphen_word)


def start_game():

    count = 1
    left_chances = len(split_char)+3

    while count <= len(split_char)+3:

        print('')
        user_value = input("Enter character:")
        left_chances = left_chances - 1

        if user_value not in user_entries:
            user_entries.append(user_value)

            indexs = [index for index, char in enumerate(split_char) if char == user_value]

            # checking for empty list
            if not indexs:
                print('')
                print('Invalid character entered'',''Left chaces are:{}'.format(left_chances))

            for ele in indexs:
                hyphen_word[ele] = split_char[ele]
            print(hyphen_word)

            if '_' not in hyphen_word:
                print('')
                print('You won the game')
                break
            if left_chances == 0:
                print('You loose the game')
                print('The screat word is:{}'.format(split_char))
                break

            count = count + 1
        else:
            print('')
            print('Entered element is already used'',''Enter different element'',''Left chances are :{}'.format(left_chances))
            if left_chances == 0:
                print('')
                print('You loose the game')
                print('The screat word is:{}'.format(split_char))
            count = count + 1

            
start_game()