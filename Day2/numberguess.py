secret_number = 7
guess = 0
while guess !=secret_number:
    guess = int(input("guess the number (1-10)"))
    if guess < secret_number:
        print("too low")
    elif guess > secret_number:
        print("too high")
    else:
        print("congratulation! you guessed it.")
            
