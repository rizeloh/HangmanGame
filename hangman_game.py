import random

def get_word():
    """
    Возвращает случайное слово из списка слов.
    """
    words = ["python", "hangman", "challenge", "programming", "development", "algorithm"]
    return random.choice(words).upper()

def display_hangman(tries):
    """
    Возвращает текущее состояние виселицы.
    """
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # голова, торс, обе руки, одна нога
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # голова, торс, обе руки
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # голова, торс и одна рука
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # голова и торс
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # голова
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # начальное пустое состояние
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def play(word):
    """
    Основная логика игры.
    """
    word_completion = "_" * len(word)  # строка, содержащая правильные угаданные буквы
    guessed = False  # флаг, указывающий на то, что слово было угадано
    guessed_letters = []  # список угаданных букв
    guessed_words = []  # список угаданных слов
    tries = 6  # количество попыток

    print("Давайте играть в Виселицу!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Пожалуйста, введите букву или слово: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Вы уже угадали букву", guess)
            elif guess not in word:
                print("Буква", guess, "нет в слове.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Отлично! Буква", guess, "есть в слове!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Вы уже угадали слово", guess)
            elif guess != word:
                print("Слово", guess, "не является правильным.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Недопустимая попытка.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Поздравляем! Вы угадали слово! Вы победили!")
    else:
        print("К сожалению, вы не угадали слово. Загаданное слово было " + word + ". Может быть, в следующий раз!")

if __name__ == "__main__":
    word = get_word()
    play(word)
