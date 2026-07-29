def generate_numbers(num):
    return num

def get_guess():
    guess=int(input("enter your numbers:"))
    return guess

def check_guess(num,guess):
    if num < guess:
        return "Too High"
    elif guess < num:
        return "Too Low"
    else:
        return"Correct"
    
def play_game():
    num= generate_numbers (70)
    attempt = 0
    while True:
        guess=get_guess()
        check=check_guess(num,guess)
        attempt +=1
        print(check)
        if check == "Correct":
            print("attempt is :",attempt)
            break


play_game()
