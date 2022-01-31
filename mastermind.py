import random

def create_code(avilable_colors, lenght):
    code = random.choices(avilable_colors, k=lenght)
    print(f"code {code}")
    return code

def get_guess(avilable_colors, lenght_of_code):
    while True:
        guess = input("Make your guess: ").upper()
        if len(guess) == lenght_of_code and set(guess) <= set(avilable_colors):
            break
        print(f" Please write {lenght_of_code}-letter words using the characters {', '.join(avilable_colors)}!")
    return guess

def check_guess(guess, secret):
    hits = sum(guess[i] == secret[i] for i in range(len(secret)))
    close = sum(min(secret.count(color), guess.count(color)) for color in set(secret))
    close = close - hits  # Don't count HITS again
    return hits, close

def game():
    avilable_colors = "BWR"
    rounds = 12
    lenght_of_code = 4
    secret_code = create_code(avilable_colors, lenght_of_code)
    actual_round = 1
    while actual_round <= rounds:
        print(f"Round {actual_round}")
        guess = get_guess(avilable_colors, lenght_of_code)
        hits, close = check_guess(guess, secret_code)
        print(f"Hits: {hits}, Close: {close}")


#game()
print(get_guess("ASDFG", 4))