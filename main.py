import random
import re
import sys


def start():
    print("Нажмите С для старта  или В для выхода")
    s = input()
    if s == "С" or s == "с":
        start_game()
    elif s == "В" or s == "в":
        sys.exit()
    else:
        print("Некорректный ввод!")
        start()


def start_game():
    word = get_word()
    masked_word = get_masked_word(word)
    print("Необходимо отгадать слова: ", masked_word)
    mistake = 0
    game_over = False
    used_letters = []
    while not game_over:
        if mistake < 5:
            round_result = play_round(word, mistake, masked_word, used_letters)
            mistake = round_result[0]
            masked_word = show_chars(word, round_result[3], round_result[1])
            if is_win(mistake, masked_word):
                print("""
                ----------------
                Вы победили!
                ----------------
                """)
                game_over = True
        else:
            game_over = True

            print(f"""
            ----------------
            Вы проиграли! Загаданное слово было: {word}
            ----------------
            """)
    start()


def get_word():
    with open("dictionary.txt","r", encoding="utf-8") as file:
        lines = file.readlines()
        line = random.randint(1, len(lines))
        word = lines[line-1]
    return word


def get_masked_word(word):
    length = len(word)
    masked_word = ""
    for i in range(length-1):
        masked_word += '*'
    return masked_word


def play_round(word, mistake, masked_word, used_letters):

    if used_letters:
        print("Вы уже использовали следующие буквы: ",used_letters)


    char = input("Введите букву: ")
    if not validate_letter(char):
        print("Некорректный ввод символа!")
        return mistake, masked_word, word, char, used_letters



    if char in used_letters:
        print("Вы уже использовали эту букву!")
        return mistake, masked_word, word, char, used_letters

    else:
        if char in word:
            print("Вы угадали букву!")
            print("-----------------")
            used_letters.append(char)
            return mistake, masked_word, word, char, used_letters
        else:
            print("Этой буквы нет в слове")
            print("-----------------")
            show_player_status(mistake + 1)
            used_letters.append(char)
            return mistake + 1, masked_word, word, char, used_letters


def show_chars(word, char, masked_word):
    chars = list(masked_word)
    for i in range(len(word)):
        if word[i] == char:
            chars[i] = char
    print("Загаданное слово: ", "".join(chars))
    return "".join(chars)


def show_player_status(mistake):
    if mistake == 1:
        print("""
            ┌───┐
            │   │
                │
                │
                │
                │
          ══════╧══""")
    elif mistake == 2:
        print("""
            ┌───┐
            │   │
            O   │
                │
                │
                │
          ══════╧══""")
    elif mistake == 3:
        print("""
          ┌───┐
          │   │
          O   │
          │   │
          │   │
              │
        ══════╧══""")
    elif mistake == 4:
        print("""
          ┌───┐
          │   │
          O   │
         /│\\  │
          │   │
              │
        ══════╧══""")
    elif mistake == 5:
        print("""
          ┌───┐
          │   │
          O   │
         /│\\  │
          │   │
         / \\  │
        ══════╧══""")

def validate_letter(char):
    return bool(re.fullmatch(r'[а-яёА-ЯЁ]+', char))


def is_win(mistake, masked_word):
    if '*' not in masked_word and mistake < 5:
        return True
    else:
        return False


start()
