import random

number_of_attempts = 0

number = random.randint(1, 5)
while number_of_attempts < 5:
    name = int(input("Угадай число от 1 - 50: "))
    number_of_attempts += 1
    if name < number:
        print("Твое число меньше, чем я загадала")
    if name > number:
        print("Твое число больше")
    if name == number:
        print("Ты угадал!")
        break
else:
    print("Не угадал, мое число {0}".format(number))